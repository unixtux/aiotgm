#!/bin/python3

REQ_DEBUG = False
RESP_DEBUG = False

__all__ = [
    'TelegramApi',
    'TelegramError'
]

from .logger import get_logger
logger = get_logger('TelegramApi')

import re
import time
import asyncio
from typing import (Any,
                    Literal,
                    Optional,
                    Coroutine)

from .http_manager import *
from .objects import InputFile, serialize, json

try:
    import ssl
except ImportError:
    logger.warning(
        "module 'ssl' not found, SSL_CONTEXT is None"
    )
    SSL_CONTEXT = None
else:
    try:
        import certifi
    except ImportError:
        logger.warning(
            "module 'certifi' not found, using default CA"
        )
        SSL_CONTEXT = ssl.create_default_context()
    else:
        SSL_CONTEXT = ssl.create_default_context(
            cafile = certifi.where()
        )


def _get_files(
    params: dict,
    *file_keys: str
) -> Optional[dict[str, dict[Literal['path', 'file_name'], Any]]]:

    files = {}
    for key in file_keys:
        if key in params:
            obj = params[key]
            if isinstance(obj, InputFile):
                files[key] = {
                    'path': obj.path,
                    'file_name': obj.file_name
                }
                del params[key]

    return files if files != {} else None


async def _check_json(response: ClientResponse) -> Any:

    result = await response.json(loads = json.loads)

    if RESP_DEBUG:
        logger.debug(result)

    if response.ok is True:
        return result['result']
    else:
        error_code = result['error_code']
        description = result['description']
        raise TelegramError(
            {'error_code': error_code, 'description': description}
        )


def _format_url(token: str, method: str) -> str:
    return '/bot{}/{}'.format(token, method)


def _prepare_data(
    params: Optional[dict],
    files: Optional[dict[str, dict[Literal['path', 'file_name'], Any]]]
) -> Optional[FormData]:

    if params is None:
        return None

    data = FormData(params)

    if files is None:
        return data

    for key, value in files.items():

        path = value['path']
        file_name = value['file_name']

        try:
            with open(path, 'rb') as rb:
                content = rb.read()

        except FileNotFoundError:
            raise FileNotFoundError(
                f"File {path!r} doesn't"
                ' exist, check your InputFile'
            )
        data.add_field(
            key,
            content,
            filename = file_name
        )
    return data


class TelegramError(Exception):
    """Class to handle exceptions during Telegram requests."""

BASE_URL = 'https://api.telegram.org'
CLIENT_TIMEOUT = ClientTimeout(total = 300, connect = 3)


class TelegramApi:

    def __init__(
        self,
        token: str,
        proxy: Optional[str] = None
    ):
        if not isinstance(token, str):
            raise TypeError(f'token must be str, got {token.__class__}')

        if not isinstance(proxy, (str, type(None))):
            raise TypeError(f'proxy must be str or None, got {proxy.__class__}')

        self.__token = token
        self.__session = None
        self.__headers_and_proxy = {
            'proxy': proxy,
            'headers': HEADERS
        }
        logger.debug(self.__headers_and_proxy)

    @property
    def session(self) -> Optional[ClientSession]:
        return self.__session

    def _get_session(self) -> ClientSession:

        if self.session is None or self.session.closed:
            self.__session = ClientSession(
                base_url = BASE_URL,
                timeout = CLIENT_TIMEOUT,
                json_serialize = json.dumps,
                connector = TCPConnector(ssl = SSL_CONTEXT)
            )
            logger.debug('New session initialized.')

        return self.session


    async def _request(
        self,
        method: str,
        params: Optional[dict] = None,
        files: Optional[dict] = None,
        *,
        max_retries: int = 100,
        keep_session: Optional[bool] = None
    ) -> Coroutine:

        if params is not None:
            for key, val in params.items():
                params[key] = serialize(val, ignore = (str, ))

        if REQ_DEBUG:
            logger.debug(
                f'method: {method!r}, params: {params}, files: {files}'
            )

        current_try = 0

        while current_try < max_retries:

            current_try += 1
            self._get_session()
            start_time = time.time()
            try:
                # Convert the params to
                # a FormData instance at
                # each attempt, to prevent
                # a RuntimeError from aiohttp.
                data = _prepare_data(params, files)

                async with self.session.post(
                    url = _format_url(self.__token, method),
                    data = data,
                    **self.__headers_and_proxy
                ) as response:
                    result = await _check_json(response)
                    if current_try != 1:
                        logger.info(
                            f'Request {method!r} completed'
                            f' after {current_try} retries.'
                        )
                    return result

            except (ClientError, TimeoutError) as err:
                err = type(err)(re.sub(r'bot.*?/', r'bot***/', str(err)))
                logger.warning(
                    f'{err!r} in method'
                    f' {method!r}, current try'
                    f': {current_try}/{max_retries}'
                )
                await asyncio.sleep(
                    3 - (time.time() - start_time)
                )
            except BaseException as err:
                logger.error(f'{err!r} in {method!r}')
                raise

            finally:
                if not (
                    keep_session
                    or self.session.connector._acquired
                ):
                    await self.session.close()
                    logger.debug(
                        'Session closed because there'
                        ' are not connections in the pool.'
                    )
        else:
            raise TimeoutError(
                {'method': method, 'params': params, 'files': files}
            )

###########################################################

    async def get_updates(self, params: dict, **kwargs) -> Coroutine:
        method = 'getUpdates'
        return await self._request(method, params, **kwargs)

    async def get_me(self) -> Coroutine:
        method = 'getMe'
        return await self._request(method)

    async def send_message(self, params: dict) -> Coroutine:
        method = 'sendMessage'
        return await self._request(method, params)

    async def log_out(self) -> Coroutine:
        method = 'logOut'
        return await self._request(method)

    async def close(self) -> Coroutine:
        method = 'close'
        return await self._request(method)

    async def forward_message(self, params: dict) -> Coroutine:
        method = 'forwardMessage'
        return await self._request(method, params)

    async def copy_message(self, params: dict) -> Coroutine:
        method = 'copyMessage'
        return await self._request(method, params)

    async def send_photo(self, params: dict) -> Coroutine:
        method = 'sendPhoto'
        files = _get_files(params, 'photo')
        return await self._request(method, params, files)

    async def send_audio(self, params: dict) -> Coroutine:
        method = 'sendAudio'
        files = _get_files(params, 'audio', 'thumbnail')
        return await self._request(method, params, files)

    async def send_document(self, params: dict) -> Coroutine:
        method = 'sendDocument'
        files = _get_files(params, 'document', 'thumbnail')
        return await self._request(method, params, files)

    async def send_video(self, params: dict) -> Coroutine:
        method = 'sendVideo'
        files = _get_files(params, 'video', 'thumbnail')
        return await self._request(method, params, files)

    async def send_animation(self, params: dict) -> Coroutine:
        method = 'sendAnimation'
        files = _get_files(params, 'animation', 'thumbnail')
        return await self._request(method, params, files)

    async def send_voice(self, params: dict) -> Coroutine:
        method = 'sendVoice'
        files = _get_files(params, 'voice')
        return await self._request(method, params, files)

    async def send_video_note(self, params: dict) -> Coroutine:
        method = 'sendVideoNote'
        files = _get_files(params, 'video_note', 'thumbnail')
        return await self._request(method, params, files)

    async def send_media_group(self, params: dict) -> Coroutine:
        method = 'sendMediaGroup'
        return await self._request(method, params)

    async def send_location(self, params: dict) -> Coroutine:
        method = 'sendLocation'
        return await self._request(method, params)

    async def send_venue(self, params: dict) -> Coroutine:
        method = 'sendVenue'
        return await self._request(method, params)

    async def send_contact(self, params: dict) -> Coroutine:
        method = 'sendContact'
        return await self._request(method, params)

    async def send_poll(self, params: dict) -> Coroutine:
        method = 'sendPoll'
        return await self._request(method, params)

    async def send_dice(self, params: dict) -> Coroutine:
        method = 'sendDice'
        return await self._request(method, params)

    async def send_chat_action(self, params: dict) -> Coroutine:
        method = 'sendChatAction'
        return await self._request(method, params)

    async def get_user_profile_photos(self, params: dict) -> Coroutine:
        method = 'getUserProfilePhotos'
        return await self._request(method, params)

    async def get_file(self, params: dict) -> Coroutine:
        method = 'getFile'
        return await self._request(method, params)

    async def ban_chat_member(self, params: dict) -> Coroutine:
        method = 'banChatMember'
        return await self._request(method, params)

    async def unban_chat_member(self, params: dict) -> Coroutine:
        method = 'unbanChatMember'
        return await self._request(method, params)

    async def restrict_chat_member(self, params: dict) -> Coroutine:
        method = 'restrictChatMember'
        return await self._request(method, params)

    async def promote_chat_member(self, params: dict) -> Coroutine:
        method = 'promoteChatMember'
        return await self._request(method, params)

    async def set_chat_administrator_custom_title(self, params: dict) -> Coroutine:
        method = 'setChatAdministratorCustomTitle'
        return await self._request(method, params)

    async def ban_chat_sender_chat(self, params: dict) -> Coroutine:
        method = 'banChatSenderChat'
        return await self._request(method, params)

    async def unban_chat_sender_chat(self, params: dict) -> Coroutine:
        method = 'unbanChatSenderChat'
        return await self._request(method, params)

    async def set_chat_permissions(self, params: dict) -> Coroutine:
        method = 'setChatPermissions'
        return await self._request(method, params)

    async def export_chat_invite_link(self, params: dict) -> Coroutine:
        method = 'exportChatInviteLink'
        return await self._request(method, params)

    async def create_chat_invite_link(self, params: dict) -> Coroutine:
        method = 'createChatInviteLink'
        return await self._request(method, params)

    async def edit_chat_invite_link(self, params: dict) -> Coroutine:
        method = 'editChatInviteLink'
        return await self._request(method, params)

    async def revoke_chat_invite_link(self, params: dict) -> Coroutine:
        method = 'revokeChatInviteLink'
        return await self._request(method, params)

    async def approve_chat_join_request(self, params: dict) -> Coroutine:
        method = 'approveChatJoinRequest'
        return await self._request(method, params)

    async def decline_chat_join_request(self, params: dict) -> Coroutine:
        method = 'declineChatJoinRequest'
        return await self._request(method, params)

    async def set_chat_photo(self, params: dict) -> Coroutine:
        method = 'setChatPhoto'
        files = _get_files(params, 'photo')
        return await self._request(method, params, files)

    async def delete_chat_photo(self, params: dict) -> Coroutine:
        method = 'deleteChatPhoto'
        return await self._request(method, params)

    async def set_chat_title(self, params: dict) -> Coroutine:
        method = 'setChatTitle'
        return await self._request(method, params)

    async def set_chat_description(self, params: dict) -> Coroutine:
        method = 'setChatDescription'
        return await self._request(method, params)

    async def pin_chat_message(self, params: dict) -> Coroutine:
        method = 'pinChatMessage'
        return await self._request(method, params)

    async def unpin_chat_message(self, params: dict) -> Coroutine:
        method = 'unpinChatMessage'
        return await self._request(method, params)

    async def unpin_all_chat_messages(self, params: dict) -> Coroutine:
        method = 'unpinAllChatMessages'
        return await self._request(method, params)

    async def leave_chat(self, params: dict) -> Coroutine:
        method = 'leaveChat'
        return await self._request(method, params)

    async def get_chat(self, params: dict) -> Coroutine:
        method = 'getChat'
        return await self._request(method, params)

    async def get_chat_administrators(self, params: dict) -> Coroutine:
        method = 'getChatAdministrators'
        return await self._request(method, params)

    async def get_chat_member_count(self, params: dict) -> Coroutine:
        method = 'getChatMemberCount'
        return await self._request(method, params)

    async def get_chat_member(self, params: dict) -> Coroutine:
        method = 'getChatMember'
        return await self._request(method, params)

    async def set_chat_sticker_set(self, params: dict) -> Coroutine:
        method = 'setChatStickerSet'
        return await self._request(method, params)

    async def delete_chat_sticker_set(self, params: dict) -> Coroutine:
        method = 'deleteChatStickerSet'
        return await self._request(method, params)

    async def get_forum_topic_icon_stickers(self) -> Coroutine:
        method = 'getForumTopicIconStickers'
        return await self._request(method)

    async def create_forum_topic(self, params: dict) -> Coroutine:
        method = 'createForumTopic'
        return await self._request(method, params)

    async def edit_forum_topic(self, params: dict) -> Coroutine:
        method = 'editForumTopic'
        return await self._request(method, params)

    async def close_forum_topic(self, params: dict) -> Coroutine:
        method = 'closeForumTopic'
        return await self._request(method, params)

    async def reopen_forum_topic(self, params: dict) -> Coroutine:
        method = 'reopenForumTopic'
        return await self._request(method, params)

    async def delete_forum_topic(self, params: dict) -> Coroutine:
        method = 'deleteForumTopic'
        return await self._request(method, params)

    async def unpin_all_forum_topic_messages(self, params: dict) -> Coroutine:
        method = 'unpinAllForumTopicMessages'
        return await self._request(method, params)

    async def edit_general_forum_topic(self, params: dict) -> Coroutine:
        method = 'editGeneralForumTopic'
        return await self._request(method, params)

    async def close_general_forum_topic(self, params: dict) -> Coroutine:
        method = 'closeGeneralForumTopic'
        return await self._request(method, params)

    async def reopen_general_forum_topic(self, params: dict) -> Coroutine:
        method = 'reopenGeneralForumTopic'
        return await self._request(method, params)

    async def hide_general_forum_topic(self, params: dict) -> Coroutine:
        method = 'hideGeneralForumTopic'
        return await self._request(method, params)

    async def unhide_general_forum_topic(self, params: dict) -> Coroutine:
        method = 'unhideGeneralForumTopic'
        return await self._request(method, params)

    async def unpin_all_general_forum_topic_messages(self, params: dict) -> Coroutine:
        method = 'unpinAllGeneralForumTopicMessages'
        return await self._request(method, params)

    async def answer_callback_query(self, params: dict) -> Coroutine:
        method = 'answerCallbackQuery'
        return await self._request(method, params)

    async def set_my_commands(self, params: dict) -> Coroutine:
        method = 'setMyCommands'
        return await self._request(method, params)

    async def delete_my_commands(self, params: dict) -> Coroutine:
        method = 'deleteMyCommands'
        return await self._request(method, params)

    async def get_my_commands(self, params: dict) -> Coroutine:
        method = 'getMyCommands'
        return await self._request(method, params)

    async def set_my_name(self, params: dict) -> Coroutine:
        method = 'setMyName'
        return await self._request(method, params)

    async def get_my_name(self, params: dict) -> Coroutine:
        method = 'getMyName'
        return await self._request(method, params)

    async def set_my_description(self, params: dict) -> Coroutine:
        method = 'setMyDescription'
        return await self._request(method, params)

    async def get_my_description(self, params: dict) -> Coroutine:
        method = 'getMyDescription'
        return await self._request(method, params)

    async def set_my_short_description(self, params: dict) -> Coroutine:
        method = 'setMyShortDescription'
        return await self._request(method, params)

    async def get_my_short_description(self, params: dict) -> Coroutine:
        method = 'getMyShortDescription'
        return await self._request(method, params)

    async def set_chat_menu_button(self, params: dict) -> Coroutine:
        method = 'setChatMenuButton'
        return await self._request(method, params)

    async def get_chat_menu_button(self, params: dict) -> Coroutine:
        method = 'getChatMenuButton'
        return await self._request(method, params)

    async def set_my_default_administrator_rights(self, params: dict) -> Coroutine:
        method = 'setMyDefaultAdministratorRights'
        return await self._request(method, params)

    async def get_my_default_administrator_rights(self, params: dict) -> Coroutine:
        method = 'getMyDefaultAdministratorRights'
        return await self._request(method, params)

    async def edit_message_text(self, params: dict) -> Coroutine:
        method = 'editMessageText'
        return await self._request(method, params)

    async def edit_message_caption(self, params: dict) -> Coroutine:
        method = 'editMessageCaption'
        return await self._request(method, params)

    async def edit_message_media(self, params: dict) -> Coroutine:
        method = 'editMessageMedia'
        return await self._request(method, params)

    async def edit_message_live_location(self, params: dict) -> Coroutine:
        method = 'editMessageLiveLocation'
        return await self._request(method, params)

    async def stop_message_live_location(self, params: dict) -> Coroutine:
        method = 'stopMessageLiveLocation'
        return await self._request(method, params)

    async def edit_message_reply_markup(self, params: dict) -> Coroutine:
        method = 'editMessageReplyMarkup'
        return await self._request(method, params)

    async def stop_poll(self, params: dict) -> Coroutine:
        method = 'stopPoll'
        return await self._request(method, params)

    async def delete_message(self, params: dict) -> Coroutine:
        method = 'deleteMessage'
        return await self._request(method, params)

    async def send_sticker(self, params: dict) -> Coroutine:
        method = 'sendSticker'
        files = _get_files(params, 'sticker')
        return await self._request(method, params, files)

    async def get_sticker_set(self, params: dict) -> Coroutine:
        method = 'getStickerSet'
        return await self._request(method, params)

    async def get_custom_emoji_stickers(self, params: dict) -> Coroutine:
        method = 'getCustomEmojiStickers'
        return await self._request(method, params)

    async def upload_sticker_file(self, params: dict) -> Coroutine:
        method = 'uploadStickerFile'
        files = _get_files(params, 'sticker')
        return await self._request(method, params, files)

    async def create_new_sticker_set(self, params: dict) -> Coroutine:
        method = 'createNewStickerSet'
        return await self._request(method, params)

    async def add_sticker_to_set(self, params: dict) -> Coroutine:
        method = 'addStickerToSet'
        return await self._request(method, params)

    async def set_sticker_position_in_set(self, params: dict) -> Coroutine:
        method = 'setStickerPositionInSet'
        return await self._request(method, params)

    async def delete_sticker_from_set(self, params: dict) -> Coroutine:
        method = 'deleteStickerFromSet'
        return await self._request(method, params)

    async def set_sticker_emoji_list(self, params: dict) -> Coroutine:
        method = 'setStickerEmojiList'
        return await self._request(method, params)

    async def set_sticker_keywords(self, params: dict) -> Coroutine:
        method = 'setStickerKeywords'
        return await self._request(method, params)

    async def set_sticker_mask_position(self, params: dict) -> Coroutine:
        method = 'setStickerMaskPosition'
        return await self._request(method, params)

    async def set_sticker_set_title(self, params: dict) -> Coroutine:
        method = 'setStickerSetTitle'
        return await self._request(method, params)

    async def set_sticker_set_thumbnail(self, params: dict) -> Coroutine:
        method = 'setStickerSetThumbnail'
        files = _get_files(params, 'thumbnail')
        return await self._request(method, params, files)

    async def set_custom_emoji_sticker_set_thumbnail(self, params: dict) -> Coroutine:
        method = 'setCustomEmojiStickerSetThumbnail'
        return await self._request(method, params)

    async def delete_sticker_set(self, params: dict) -> Coroutine:
        method = 'deleteStickerSet'
        return await self._request(method, params)

    async def answer_inline_query(self, params: dict) -> Coroutine:
        method = 'answerInlineQuery'
        return await self._request(method, params)

    async def answer_web_app_query(self, params: dict) -> Coroutine:
        method = 'answerWebAppQuery'
        return await self._request(method, params)

    async def send_invoice(self, params: dict) -> Coroutine:
        method = 'sendInvoice'
        return await self._request(method, params)

    async def create_invoice_link(self, params: dict) -> Coroutine:
        method = 'createInvoiceLink'
        return await self._request(method, params)

    async def answer_shipping_query(self, params: dict) -> Coroutine:
        method = 'answerShippingQuery'
        return await self._request(method, params)

    async def answer_pre_checkout_query(self, params: dict) -> Coroutine:
        method = 'answerPreCheckoutQuery'
        return await self._request(method, params)

    async def set_passport_data_errors(self, params: dict) -> Coroutine:
        method = 'setPassportDataErrors'
        return await self._request(method, params)

    async def send_game(self, params: dict) -> Coroutine:
        method = 'sendGame'
        return await self._request(method, params)

    async def set_game_score(self, params: dict) -> Coroutine:
        method = 'setGameScore'
        return await self._request(method, params)

    async def get_game_high_scores(self, params: dict) -> Coroutine:
        method = 'getGameHighScores'
        return await self._request(method, params)
