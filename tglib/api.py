#!/bin/env python3

REQ_DEBUG = 0
RESP_DEBUG = 0

__all__ = (
    'TelegramApi',
    'TelegramError',
)
from .logger import get_logger
logger = get_logger('TelegramApi')

import os
import re
import time
import asyncio
from typing import (
    Any,
    Union,
    Literal,
    Optional,
    Iterable,
)
from types import UnionType # just for type-checking in _convert_input_media()
from aiohttp import (
    FormData,
    ClientError,
    TCPConnector,
    ClientSession,
    ClientTimeout,
    ClientResponse,
)
from .types import (
    TelegramType, # to serialize Telegram types in _serialize()
    InputFile,
    InputMedia,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
)
try:
    import ssl
except ImportError:
    logger.warning(
        "module 'ssl' not found, SSL_CONTEXT is None."
    )
    SSL_CONTEXT = None
else:
    try:
        import certifi
    except ImportError:
        logger.warning(
            "module 'certifi' not found, using default CA."
        )
        SSL_CONTEXT = ssl.create_default_context()
    else:
        _cafile = certifi.where()
        if not os.path.isfile(_cafile):
            _cafile = None
            logger.warning(
                "CA file not found, try to"
                " reinstall the module 'certifi'."
            )
        SSL_CONTEXT = ssl.create_default_context(
            cafile=_cafile
        )
        del _cafile

try:
    import ujson as json
except ImportError:
    import json
    logger.info(
        "module 'ujson' not found, the"
        " default 'json' was imported."
    )

def _serialize(
    val,
    *,
    last: bool = True,
    ignore: Optional[tuple[type, ...]] = (str,)
) -> Union[Any, str, list, dict]:

    ignore = ignore if ignore is not None else ()

    if isinstance(val, TelegramType):
        val = val.__dict__

    elif hasattr(val, '__dict__'):
        val = '{!r}'.format(val)

    if isinstance(val, dict):
        res = {
            x: _serialize(val[x], last=False) for x in val if val[x] is not None
        }
    elif isinstance(val, Iterable):
        res = [
            _serialize(x, last=False) for x in val
        ]
    else:
        res = val

    if not last:
        return res
    else:
        return res if type(res) in ignore else json.dumps(res, ensure_ascii=False)


def _format_url(token: str, method: str, /) -> str:
    return '/bot{}/{}'.format(token, method)


async def _parse_json(response: ClientResponse, /) -> Any:

    result = await response.json(loads=json.loads)

    if RESP_DEBUG:
        logger.debug(result)

    if result['ok'] is True:
        return result['result']
    else:
        raise TelegramError(
            {
                'error_code': result['error_code'],
                'description': result['description']
            }
        )


def _get_files(
    params: dict,
    *file_keys: str
) -> Optional[dict[str, dict[Literal['content', 'file_name'], Any]]]:

    files = {}
    for key in file_keys:
        if key in params:
            obj = params[key]
            if isinstance(obj, InputFile):
                try:
                    with open(obj.path, 'rb') as rb:
                        content = rb.read()
                except FileNotFoundError:
                    raise FileNotFoundError(
                        f"Inexistent file: {obj.path!r},"
                        ' check your InputFile object.'
                    )
                files[key] = {
                    'content': content,
                    'file_name': obj.file_name
                }
                del params[key]

    return files or None


def _convert_input_media(
    media: InputMedia,
    files: dict,
    types_check: UnionType,
    /
) -> None:
    '''
    Used in _get_input_media_files() to check and add to files InputMedia objects.
    '''
    if not isinstance(media, types_check):
        available_types = ', '.join([t.__name__ for t in types_check.__args__])
        raise TypeError(
            f'Expected one of the following types:'
            f' {available_types}, got {media.__class__.__name__}.'
        )
    if isinstance(media.media, str):
        media_file = re.match(r'attach://(.*)', media.media)
        if media_file:
            path = media_file.group(1)
            try:
                with open(path, 'rb') as rb:
                    content = rb.read()
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Inexistent file: {path!r},"
                    ' check your InputMedia object;'
                    ' InputMedia.media must be in the'
                    ' format "attach://<file_name>" to'
                    ' post a file using multipart/form-data.'
                )
            files[path] = {
                'content': content,
                'file_name': path
            }


def _get_input_media_files(
    params: dict,
    *file_keys: str,
    types_check: UnionType
) -> Optional[dict[str, dict[Literal['content', 'file_name'], Any]]]:

    files = {}
    for key in file_keys:
        if key in params:
            obj = params[key]
            if isinstance(obj, Iterable):
                for t in obj:
                    _convert_input_media(t, files, types_check)
            else:
                _convert_input_media(obj, files, types_check)

    return files or None


def _prepare_data(
    params: Optional[dict],
    files: Optional[dict[str, dict[Literal['content', 'file_name'], Any]]],
    /
) -> Optional[FormData]:

    if params is None:
        return None

    data = FormData(params)

    if files is None:
        return data

    for key in files:

        content = files[key]['content']
        file_name = files[key]['file_name']

        data.add_field(
            key,
            content,
            filename=file_name
        )
    return data


class TelegramError(Exception):
    '''
    Class to handle exceptions during Telegram requests.
    '''

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0'
}
CLIENT_TIMEOUT = ClientTimeout(total=300, connect=3)


class TelegramApi:

    def __init__(
        self,
        token: str,
        proxy: Optional[str] = None,
        debug: Optional[bool] = None
    ):
        if not isinstance(token, str):
            raise TypeError(
                f"'token' must be str, got {token.__class__.__name__}."
            )
        if not isinstance(proxy, (str, type(None))):
            raise TypeError(
                f"'proxy' must be str or None, got {proxy.__class__.__name__}."
            )
        if debug:
            logger.setLevel(10)

        self._token = token
        self._session = None
        self._headers_and_proxy = {
            'proxy': proxy,
            'headers': HEADERS
        }
        logger.debug(self._headers_and_proxy)

    @property
    def session(self) -> Optional[ClientSession]:
        return self._session

    def _get_session(self) -> ClientSession:

        if self.session is None or self.session.closed:
            self._session = ClientSession(
                base_url='https://api.telegram.org',
                timeout=CLIENT_TIMEOUT,
                json_serialize=json.dumps,
                connector=TCPConnector(ssl=SSL_CONTEXT)
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
        keep_alive: bool = False
    ):
        if params is not None:
            for key in params:
                params[key] = _serialize(params[key])

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
                    url=_format_url(self._token, method),
                    data=data,
                    **self._headers_and_proxy
                ) as response:

                    result = await _parse_json(response)

                    if current_try != 1:
                        logger.info(
                            f'Request {method!r} succeeded'
                            f' after {current_try} retries.'
                        )
                    return result

            except (ClientError, TimeoutError) as exc:
                logger.info(
                    f'{exc.__class__.__name__} in {method!r},'
                    f' current try: {current_try}/{max_retries}.'
                )
                await asyncio.sleep(3 - (time.time() - start_time))

            except BaseException as exc:
                exc = type(exc)(*[arg for arg in exc.args])
                # this because it causes too much traceback
                raise exc from None

            finally:
                if self.session.connector is not None:
                    if not (
                        keep_alive
                        or self.session.connector._acquired
                    ):
                        await self.session.close()
                        logger.debug(
                            'Session closed because there'
                            ' are not connections in the pool.'
                        )
        else:
            raise TimeoutError(method)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    async def add_sticker_to_set(self, params):
        method = 'addStickerToSet'
        return await self._request(method, params)

    async def answer_callback_query(self, params):
        method = 'answerCallbackQuery'
        return await self._request(method, params)

    async def answer_inline_query(self, params):
        method = 'answerInlineQuery'
        return await self._request(method, params)

    async def answer_pre_checkout_query(self, params):
        method = 'answerPreCheckoutQuery'
        return await self._request(method, params)

    async def answer_shipping_query(self, params):
        method = 'answerShippingQuery'
        return await self._request(method, params)

    async def answer_web_app_query(self, params):
        method = 'answerWebAppQuery'
        return await self._request(method, params)

    async def approve_chat_join_request(self, params):
        method = 'approveChatJoinRequest'
        return await self._request(method, params)

    async def ban_chat_member(self, params):
        method = 'banChatMember'
        return await self._request(method, params)

    async def ban_chat_sender_chat(self, params):
        method = 'banChatSenderChat'
        return await self._request(method, params)

    async def close(self):
        method = 'close'
        return await self._request(method)

    async def close_forum_topic(self, params):
        method = 'closeForumTopic'
        return await self._request(method, params)

    async def close_general_forum_topic(self, params):
        method = 'closeGeneralForumTopic'
        return await self._request(method, params)

    async def copy_message(self, params):
        method = 'copyMessage'
        return await self._request(method, params)

    async def copy_messages(self, params):
        method = 'copyMessages'
        return await self._request(method, params)

    async def create_chat_invite_link(self, params):
        method = 'createChatInviteLink'
        return await self._request(method, params)

    async def create_forum_topic(self, params):
        method = 'createForumTopic'
        return await self._request(method, params)

    async def create_invoice_link(self, params):
        method = 'createInvoiceLink'
        return await self._request(method, params)

    async def get_updates(self, params, **kwargs):
        method = 'getUpdates'
        return await self._request(method, params, **kwargs)

    async def get_me(self):
        method = 'getMe'
        return await self._request(method)

    async def send_message(self, params):
        method = 'sendMessage'
        return await self._request(method, params)

    async def log_out(self):
        method = 'logOut'
        return await self._request(method)

    async def forward_message(self, params):
        method = 'forwardMessage'
        return await self._request(method, params)

    async def forward_messages(self, params):
        method = 'forwardMessages'
        return await self._request(method, params)

    async def send_photo(self, params):
        method = 'sendPhoto'
        files = _get_files(params, 'photo')
        return await self._request(method, params, files)

    async def send_audio(self, params):
        method = 'sendAudio'
        files = _get_files(params, 'audio', 'thumbnail')
        return await self._request(method, params, files)

    async def send_document(self, params):
        method = 'sendDocument'
        files = _get_files(params, 'document', 'thumbnail')
        return await self._request(method, params, files)

    async def send_video(self, params):
        method = 'sendVideo'
        files = _get_files(params, 'video', 'thumbnail')
        return await self._request(method, params, files)

    async def send_animation(self, params):
        method = 'sendAnimation'
        files = _get_files(params, 'animation', 'thumbnail')
        return await self._request(method, params, files)

    async def send_voice(self, params):
        method = 'sendVoice'
        files = _get_files(params, 'voice')
        return await self._request(method, params, files)

    async def send_video_note(self, params):
        method = 'sendVideoNote'
        files = _get_files(params, 'video_note', 'thumbnail')
        return await self._request(method, params, files)

    async def send_media_group(self, params):
        method = 'sendMediaGroup'
        files = _get_input_media_files(
            params,
            'media',
            types_check=Union[InputMediaPhoto, InputMediaAudio, InputMediaVideo, InputMediaDocument]
        )
        return await self._request(method, params, files)

    async def send_location(self, params):
        method = 'sendLocation'
        return await self._request(method, params)

    async def send_venue(self, params):
        method = 'sendVenue'
        return await self._request(method, params)

    async def send_contact(self, params):
        method = 'sendContact'
        return await self._request(method, params)

    async def send_poll(self, params):
        method = 'sendPoll'
        return await self._request(method, params)

    async def send_dice(self, params):
        method = 'sendDice'
        return await self._request(method, params)

    async def send_chat_action(self, params):
        method = 'sendChatAction'
        return await self._request(method, params)

    async def set_message_reaction(self, params):
        method = 'setMessageReaction'
        return await self._request(method, params)

    async def get_user_profile_photos(self, params):
        method = 'getUserProfilePhotos'
        return await self._request(method, params)

    async def get_file(self, params):
        method = 'getFile'
        return await self._request(method, params)

    async def unban_chat_member(self, params):
        method = 'unbanChatMember'
        return await self._request(method, params)

    async def restrict_chat_member(self, params):
        method = 'restrictChatMember'
        return await self._request(method, params)

    async def promote_chat_member(self, params):
        method = 'promoteChatMember'
        return await self._request(method, params)

    async def set_chat_administrator_custom_title(self, params):
        method = 'setChatAdministratorCustomTitle'
        return await self._request(method, params)

    async def unban_chat_sender_chat(self, params):
        method = 'unbanChatSenderChat'
        return await self._request(method, params)

    async def set_chat_permissions(self, params):
        method = 'setChatPermissions'
        return await self._request(method, params)

    async def export_chat_invite_link(self, params):
        method = 'exportChatInviteLink'
        return await self._request(method, params)

    async def edit_chat_invite_link(self, params):
        method = 'editChatInviteLink'
        return await self._request(method, params)

    async def revoke_chat_invite_link(self, params):
        method = 'revokeChatInviteLink'
        return await self._request(method, params)

    async def decline_chat_join_request(self, params):
        method = 'declineChatJoinRequest'
        return await self._request(method, params)

    async def set_chat_photo(self, params):
        method = 'setChatPhoto'
        files = _get_files(params, 'photo')
        return await self._request(method, params, files)

    async def delete_chat_photo(self, params):
        method = 'deleteChatPhoto'
        return await self._request(method, params)

    async def set_chat_title(self, params):
        method = 'setChatTitle'
        return await self._request(method, params)

    async def set_chat_description(self, params):
        method = 'setChatDescription'
        return await self._request(method, params)

    async def pin_chat_message(self, params):
        method = 'pinChatMessage'
        return await self._request(method, params)

    async def unpin_chat_message(self, params):
        method = 'unpinChatMessage'
        return await self._request(method, params)

    async def unpin_all_chat_messages(self, params):
        method = 'unpinAllChatMessages'
        return await self._request(method, params)

    async def leave_chat(self, params):
        method = 'leaveChat'
        return await self._request(method, params)

    async def get_chat(self, params):
        method = 'getChat'
        return await self._request(method, params)

    async def get_chat_administrators(self, params):
        method = 'getChatAdministrators'
        return await self._request(method, params)

    async def get_chat_member_count(self, params):
        method = 'getChatMemberCount'
        return await self._request(method, params)

    async def get_chat_member(self, params):
        method = 'getChatMember'
        return await self._request(method, params)

    async def set_chat_sticker_set(self, params):
        method = 'setChatStickerSet'
        return await self._request(method, params)

    async def delete_chat_sticker_set(self, params):
        method = 'deleteChatStickerSet'
        return await self._request(method, params)

    async def get_forum_topic_icon_stickers(self):
        method = 'getForumTopicIconStickers'
        return await self._request(method)

    async def edit_forum_topic(self, params):
        method = 'editForumTopic'
        return await self._request(method, params)

    async def reopen_forum_topic(self, params):
        method = 'reopenForumTopic'
        return await self._request(method, params)

    async def delete_forum_topic(self, params):
        method = 'deleteForumTopic'
        return await self._request(method, params)

    async def unpin_all_forum_topic_messages(self, params):
        method = 'unpinAllForumTopicMessages'
        return await self._request(method, params)

    async def edit_general_forum_topic(self, params):
        method = 'editGeneralForumTopic'
        return await self._request(method, params)

    async def reopen_general_forum_topic(self, params):
        method = 'reopenGeneralForumTopic'
        return await self._request(method, params)

    async def hide_general_forum_topic(self, params):
        method = 'hideGeneralForumTopic'
        return await self._request(method, params)

    async def unhide_general_forum_topic(self, params):
        method = 'unhideGeneralForumTopic'
        return await self._request(method, params)

    async def unpin_all_general_forum_topic_messages(self, params):
        method = 'unpinAllGeneralForumTopicMessages'
        return await self._request(method, params)

    async def get_user_chat_boosts(self, params):
        method = 'getUserChatBoosts'
        return await self._request(method, params)

    async def set_my_commands(self, params):
        method = 'setMyCommands'
        return await self._request(method, params)

    async def delete_my_commands(self, params):
        method = 'deleteMyCommands'
        return await self._request(method, params)

    async def get_my_commands(self, params):
        method = 'getMyCommands'
        return await self._request(method, params)

    async def set_my_name(self, params):
        method = 'setMyName'
        return await self._request(method, params)

    async def get_my_name(self, params):
        method = 'getMyName'
        return await self._request(method, params)

    async def set_my_description(self, params):
        method = 'setMyDescription'
        return await self._request(method, params)

    async def get_my_description(self, params):
        method = 'getMyDescription'
        return await self._request(method, params)

    async def set_my_short_description(self, params):
        method = 'setMyShortDescription'
        return await self._request(method, params)

    async def get_my_short_description(self, params):
        method = 'getMyShortDescription'
        return await self._request(method, params)

    async def set_chat_menu_button(self, params):
        method = 'setChatMenuButton'
        return await self._request(method, params)

    async def get_chat_menu_button(self, params):
        method = 'getChatMenuButton'
        return await self._request(method, params)

    async def set_my_default_administrator_rights(self, params):
        method = 'setMyDefaultAdministratorRights'
        return await self._request(method, params)

    async def get_my_default_administrator_rights(self, params):
        method = 'getMyDefaultAdministratorRights'
        return await self._request(method, params)

    async def edit_message_text(self, params):
        method = 'editMessageText'
        return await self._request(method, params)

    async def edit_message_caption(self, params):
        method = 'editMessageCaption'
        return await self._request(method, params)

    async def edit_message_media(self, params):
        method = 'editMessageMedia'
        files = _get_input_media_files(params, 'media', types_check=InputMedia)
        return await self._request(method, params, files)

    async def edit_message_live_location(self, params):
        method = 'editMessageLiveLocation'
        return await self._request(method, params)

    async def stop_message_live_location(self, params):
        method = 'stopMessageLiveLocation'
        return await self._request(method, params)

    async def edit_message_reply_markup(self, params):
        method = 'editMessageReplyMarkup'
        return await self._request(method, params)

    async def stop_poll(self, params):
        method = 'stopPoll'
        return await self._request(method, params)

    async def delete_message(self, params):
        method = 'deleteMessage'
        return await self._request(method, params)

    async def delete_messages(self, params):
        method = 'deleteMessages'
        return await self._request(method, params)

    async def send_sticker(self, params):
        method = 'sendSticker'
        files = _get_files(params, 'sticker')
        return await self._request(method, params, files)

    async def get_sticker_set(self, params):
        method = 'getStickerSet'
        return await self._request(method, params)

    async def get_custom_emoji_stickers(self, params):
        method = 'getCustomEmojiStickers'
        return await self._request(method, params)

    async def upload_sticker_file(self, params):
        method = 'uploadStickerFile'
        files = _get_files(params, 'sticker')
        return await self._request(method, params, files)

    async def create_new_sticker_set(self, params):
        method = 'createNewStickerSet'
        return await self._request(method, params)

    async def set_sticker_position_in_set(self, params):
        method = 'setStickerPositionInSet'
        return await self._request(method, params)

    async def delete_sticker_from_set(self, params):
        method = 'deleteStickerFromSet'
        return await self._request(method, params)

    async def set_sticker_emoji_list(self, params):
        method = 'setStickerEmojiList'
        return await self._request(method, params)

    async def set_sticker_keywords(self, params):
        method = 'setStickerKeywords'
        return await self._request(method, params)

    async def set_sticker_mask_position(self, params):
        method = 'setStickerMaskPosition'
        return await self._request(method, params)

    async def set_sticker_set_title(self, params):
        method = 'setStickerSetTitle'
        return await self._request(method, params)

    async def set_sticker_set_thumbnail(self, params):
        method = 'setStickerSetThumbnail'
        files = _get_files(params, 'thumbnail')
        return await self._request(method, params, files)

    async def set_custom_emoji_sticker_set_thumbnail(self, params):
        method = 'setCustomEmojiStickerSetThumbnail'
        return await self._request(method, params)

    async def delete_sticker_set(self, params):
        method = 'deleteStickerSet'
        return await self._request(method, params)

    async def send_invoice(self, params):
        method = 'sendInvoice'
        return await self._request(method, params)

    async def set_passport_data_errors(self, params):
        method = 'setPassportDataErrors'
        return await self._request(method, params)

    async def send_game(self, params):
        method = 'sendGame'
        return await self._request(method, params)

    async def set_game_score(self, params):
        method = 'setGameScore'
        return await self._request(method, params)

    async def get_game_high_scores(self, params):
        method = 'getGameHighScores'
        return await self._request(method, params)
