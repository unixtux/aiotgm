#!/bin/python3

__version__ = '1.0.9'

__all__ = [
    'Client',
    'NextManager',
    'TelegramError',
    'MARKDOWN_ESCAPES'
]

MARKDOWN_ESCAPES = {
    '_':'\_',
    '*':'\*',
    '[':'\[',
    ']':'\]',
    '(':'\(',
    ')':'\)',
    '~':'\~',
    '`':'\`',
    '>':'\>',
    '#':'\#',
    '+':'\+',
    '-':'\-',
    '=':'\=',
    '|':'\|',
    '{':'\{',
    '}':'\}',
    '.':'\.',
    '!':'\!'
}

import re
import asyncio
from typing import (Any,
                    Union,
                    Literal,
                    Optional,
                    Callable,
                    Coroutine)

from .api import (
    TelegramApi,
    TelegramError
)
from .objects import *
from .update_manager import *

from .logger import get_logger
logger = get_logger('TelegramApi')


class Client(TelegramApi):

    def __init__(
        self,
        token: str,
        parse_mode: Optional[str] = None,
        protect_content: Optional[bool] = None,
        *,
        proxy: Optional[str] = None
    ):
        super().__init__(token, proxy)

        self.__offset = None

        self.parse_mode = parse_mode
        self.protect_content = protect_content

        self.__message_manager = UpdateManager(MESSAGE_MANAGER, Message)
        self.__edited_message_manager = UpdateManager(EDITED_MESSAGE_MANAGER, Message)
        self.__channel_post_manager = UpdateManager(CHANNEL_POST_MANAGER, Message)
        self.__edited_channel_post_manager = UpdateManager(EDITED_CHANNEL_POST_MANAGER, Message)
        self.__inline_query_manager = UpdateManager(INLINE_QUERY_MANAGER, InlineQuery)
        self.__chosen_inline_result_manager = UpdateManager(CHOSEN_INLINE_RESULT_MANAGER, ChosenInlineResult)
        self.__callback_query_manager = UpdateManager(CALLBACK_QUERY_MANAGER, CallbackQuery)
        self.__shipping_query_manager = UpdateManager(SHIPPING_QUERY_MANAGER, ShippingQuery)
        self.__pre_checkout_query_manager = UpdateManager(PRE_CHECKOUT_QUERY_MANAGER, PreCheckoutQuery)
        self.__poll_manager = UpdateManager(POLL_MANAGER, Poll)
        self.__poll_answer_manager = UpdateManager(POLL_ANSWER_MANAGER, PollAnswer)
        self.__my_chat_member_manager = UpdateManager(MY_CHAT_MEMBER_MANAGER, ChatMemberUpdated)
        self.__chat_member_manager = UpdateManager(CHAT_MEMBER_MANAGER, ChatMemberUpdated)
        self.__chat_join_request_manager = UpdateManager(CHAT_JOIN_REQUEST_MANAGER, ChatJoinRequest)


    @property
    def parse_mode(self) -> Optional[str]:
        return self.__parse_mode

    @parse_mode.setter
    def parse_mode(self, val: Optional[str]) -> None:
        if not isinstance(val, (str, type(None))):
            raise TypeError(f'parse_mode must be str or None, got {val.__class__}')
        self.__parse_mode = val

    @property
    def protect_content(self) -> Optional[bool]:
        return self.__protect_content

    @protect_content.setter
    def protect_content(self, val: Optional[bool]) -> None:
        val = None if not val else True
        self.__protect_content = val


    # 14 UpdateManagers

    @property
    def message_manager(self) -> UpdateManager:
        return self.__message_manager

    def manage_message(self, checker = lambda message: True):
        def wrap(func: Callable[[Message], Any]):
            self.message_manager.add_rule(checker, func)
        return wrap

    @property
    def edited_message_manager(self) -> UpdateManager:
        return self.__edited_message_manager

    def manage_edited_message(self, checker = lambda edited_message: True):
        def wrap(func: Callable[[Message], Any]):
            self.edited_message_manager.add_rule(checker, func)
        return wrap

    @property
    def channel_post_manager(self) -> UpdateManager:
        return self.__channel_post_manager

    def manage_channel_post(self, checker = lambda channel_post: True):
        def wrap(func: Callable[[Message], Any]):
            self.channel_post_manager.add_rule(checker, func)
        return wrap

    @property
    def edited_channel_post_manager(self) -> UpdateManager:
        return self.__edited_channel_post_manager

    def manage_edited_channel_post(self, checker = lambda edited_channel_post: True):
        def wrap(func: Callable[[Message], Any]):
            self.edited_channel_post_manager.add_rule(checker, func)
        return wrap

    @property
    def inline_query_manager(self) -> UpdateManager:
        return self.__inline_query_manager

    def manage_inline_query(self, checker = lambda inline_query: True):
        def wrap(func: Callable[[InlineQuery], Any]):
            self.inline_query_manager.add_rule(checker, func)
        return wrap

    @property
    def chosen_inline_result_manager(self) -> UpdateManager:
        return self.__chosen_inline_result_manager

    def manage_chosen_inline_result(self, checker = lambda chosen_inline_result: True):
        def wrap(func: Callable[[ChosenInlineResult], Any]):
            self.chosen_inline_result_manager.add_rule(checker, func)
        return wrap

    @property
    def callback_query_manager(self) -> UpdateManager:
        return self.__callback_query_manager

    def manage_callback_query(self, checker = lambda callback_query: True):
        def wrap(func: Callable[[CallbackQuery], Any]):
            self.callback_query_manager.add_rule(checker, func)
        return wrap

    @property
    def shipping_query_manager(self) -> UpdateManager:
        return self.__shipping_query_manager

    def manage_shipping_query(self, checker = lambda shipping_query: True):
        def wrap(func: Callable[[ShippingQuery], Any]):
            self.shipping_query_manager.add_rule(checker, func)
        return wrap

    @property
    def pre_checkout_query_manager(self) -> UpdateManager:
        return self.__pre_checkout_query_manager

    def manage_pre_checkout_query(self, checker = lambda pre_checkout_query: True):
        def wrap(func: Callable[[PreCheckoutQuery], Any]):
            self.pre_checkout_query_manager.add_rule(checker, func)
        return wrap

    @property
    def poll_manager(self) -> UpdateManager:
        return self.__poll_manager

    def manage_poll(self, checker = lambda poll: True):
        def wrap(func: Callable[[Poll], Any]):
            self.poll_manager.add_rule(checker, func)
        return wrap

    @property
    def poll_answer_manager(self) -> UpdateManager:
        return self.__poll_answer_manager

    def manage_poll_answer(self, checker = lambda poll_answer: True):
        def wrap(func: Callable[[PollAnswer], Any]):
            self.poll_answer_manager.add_rule(checker, func)
        return wrap

    @property
    def my_chat_member_manager(self) -> UpdateManager:
        return self.__my_chat_member_manager

    def manage_my_chat_member(self, checker = lambda my_chat_member: True):
        def wrap(func: Callable[[ChatMemberUpdated], Any]):
            self.my_chat_member_manager.add_rule(checker, func)
        return wrap

    @property
    def chat_member_manager(self) -> UpdateManager:
        return self.__chat_member_manager

    def manage_chat_member(self, checker = lambda chat_member: True):
        def wrap(func: Callable[[ChatMemberUpdated], Any]):
            self.chat_member_manager.add_rule(checker, func)
        return wrap

    @property
    def chat_join_request_manager(self) -> UpdateManager:
        return self.__chat_join_request_manager

    def manage_chat_join_request(self, checker = lambda chat_join_request: True):
        def wrap(func: Callable[[ChatJoinRequest], Any]):
            self.chat_join_request_manager.add_rule(checker, func)
        return wrap


    # Processing new updates

    async def long_polling(self, timeout: int = 60):
        unlimited = float('inf')
        params = {'timeout': timeout}
        while True:
            try:
                if self.__offset is not None:
                    params['offset'] = self.__offset

                result = await super().get_updates(
                    params = params,
                    max_retries = unlimited,
                    keep_session = True
                )
                updates = [Update.dese(update) for update in result]

            except TelegramError as exc:
                if not re.search(r'bad.*gateway', str(exc), re.IGNORECASE):
                    await self.session.close()
                    return logger.info('long polling was interrupted.')

            except:
                await self.session.close()
                return logger.info('long polling was interrupted.')
            else:
                if updates:
                    self.__offset = updates[-1].update_id + 1
                    for update in updates:
                        asyncio.create_task(self.__process_update(update))


    async def __process_update(self, update: Update):

        if update.message:
            obj: Message = update.message
            for rule in self.message_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.edited_message:
            obj: Message = update.edited_message
            for rule in self.edited_message_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.channel_post:
            obj: Message = update.channel_post
            for rule in self.channel_post_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.edited_channel_post:
            obj: Message = update.edited_channel_post
            for rule in self.edited_channel_post_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.inline_query:
            obj: InlineQuery = update.inline_query
            for rule in self.inline_query_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.chosen_inline_result:
            obj: ChosenInlineResult = update.chosen_inline_result
            for rule in self.chosen_inline_result_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.callback_query:
            obj: CallbackQuery = update.callback_query
            for rule in self.callback_query_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.shipping_query:
            obj: ShippingQuery = update.shipping_query
            for rule in self.shipping_query_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.pre_checkout_query:
            obj: PreCheckoutQuery = update.pre_checkout_query
            for rule in self.pre_checkout_query_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.poll:
            obj: Poll = update.poll
            for rule in self.poll_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.poll_answer:
            obj: PollAnswer = update.poll_answer
            for rule in self.poll_answer_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.my_chat_member:
            obj: ChatMemberUpdated = update.my_chat_member
            for rule in self.my_chat_member_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.chat_member:
            obj: ChatMemberUpdated = update.chat_member
            for rule in self.chat_member_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return

        elif update.chat_join_request:
            obj: ChatJoinRequest = update.chat_join_request
            for rule in self.chat_join_request_manager:
                try:
                    result = await _run_coroutine(rule, obj)
                    if not isinstance(result, NextManager):
                       return
                except:
                    return


    # Available methods

    async def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[list[str]] = None
    ) -> list[Update]:
        '''\
        https://core.telegram.org/bots/api#getupdates
        Use this method to receive incoming updates using long polling. Returns an Array of Update objects.'''
        params = {}
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        if timeout is not None: params['timeout'] = timeout
        if allowed_updates is not None: params['allowed_updates'] = allowed_updates
        result = await super().get_updates(params)
        return [Update.dese(update) for update in result]


    async def get_me(self) -> User:
        '''\
        https://core.telegram.org/bots/api#getme
        A simple method for testing your bot's authentication token. Requires
        no parameters. Returns basic information about the bot in form of a User object.'''
        result = await super().get_me()
        return User.dese(result)


    async def log_out(self) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#logout
        Use this method to log out from the cloud Bot API server before launching the bot locally.
        You must log out the bot before running it locally, otherwise there is no guarantee that the
        bot will receive updates. After a successful call, you can immediately log in on a local server, but will
        not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters.'''
        return await super().log_out()


    async def close(self) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#close
        Use this method to close the bot instance before moving it from one local server to another. You need to delete the
        webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will
        return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters.'''
        return await super().close()


    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        message_thread_id: Optional[int] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[list[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup:  Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendmessage
        Use this method to send text messages. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'text': text
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if entities is not None: params['entities'] = entities
        if disable_web_page_preview is not None: params['disable_web_page_preview'] = disable_web_page_preview
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_message(params)
        return Message.dese(result)


    async def forward_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#forwardmessage
        Use this method to forward messages of any kind. Service messages
        can't be forwarded. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        result = await super().forward_message(params)
        return Message.dese(result)


    async def copy_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> MessageId:
        '''\
        https://core.telegram.org/bots/api#copymessage
        Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. A quiz poll can be
        copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessage,
        but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.'''
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().copy_message(params)
        return MessageId.dese(result)


    async def send_photo(
        self,
        chat_id: Union[int, str],
        photo: Union[InputFile, str],
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendphoto
        Use this method to send photos. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'photo': photo
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if has_spoiler is not None: params['has_spoiler'] = has_spoiler
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_photo(params)
        return Message.dese(result)


    async def send_audio(
        self,
        chat_id: Union[int, str],
        audio: Union[InputFile, str],
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendaudio
        Use this method to send audio files, if you want Telegram clients to display them in the music
        player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned.
        Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the sendVoice method instead.'''
        params = {
            'chat_id': chat_id,
            'audio': audio
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if duration is not None: params['duration'] = duration
        if performer is not None: params['performer'] = performer
        if title is not None: params['title'] = title
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_audio(params)
        return Message.dese(result)


    async def send_document(
        self,
        chat_id: Union[int, str],
        document: Union[InputFile, str],
        message_thread_id: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        disable_content_type_detection: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#senddocument
        Use this method to send general files. On success, the sent Message is returned. Bots can
        currently send files of any type of up to 50 MB in size, this limit may be changed in the future.'''
        params = {
            'chat_id': chat_id,
            'document': document
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if disable_content_type_detection is not None: params['disable_content_type_detection'] = disable_content_type_detection
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_document(params)
        return Message.dese(result)


    async def send_video(
        self,
        chat_id: Union[int, str],
        video: Union[InputFile, str],
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        has_spoiler: Optional[bool] = None,
        supports_streaming: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendvideo
        Use this method to send video files, Telegram clients support
        MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned.
        Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.'''
        params = {
            'chat_id': chat_id,
            'video': video
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if duration is not None: params['duration'] = duration
        if width is not None: params['width'] = width
        if height is not None: params['height'] = height
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if has_spoiler is not None: params['has_spoiler'] = has_spoiler
        if supports_streaming is not None: params['supports_streaming'] = supports_streaming
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_video(params)
        return Message.dese(result)


    async def send_animation(
        self,
        chat_id: Union[int, str],
        animation: Union[InputFile, str],
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendanimation
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message
        is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.'''
        params = {
            'chat_id': chat_id,
            'animation': animation
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if duration is not None: params['duration'] = duration
        if width is not None: params['width'] = width
        if height is not None: params['height'] = height
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if has_spoiler is not None: params['has_spoiler'] = has_spoiler
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_animation(params)
        return Message.dese(result)


    async def send_voice(
        self,
        chat_id: Union[int, str],
        voice: Union[InputFile, str],
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendvoice
        Use this method to send audio files, if you want Telegram clients to display the file as
        a playable voice message. For this to work, your audio must be in an .OGG file encoded with
        OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned.
        Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.'''
        params = {
            'chat_id': chat_id,
            'voice': voice
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if duration is not None: params['duration'] = duration
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_voice(params)
        return Message.dese(result)


    async def send_video_note(
        self,
        chat_id: Union[int, str],
        video_note: Union[InputFile, str],
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        length: Optional[int] = None,
        thumbnail: Optional[Union[InputFile, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendvideonote
        As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute
        long. Use this method to send video messages. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'video_note': video_note
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if duration is not None: params['duration'] = duration
        if length is not None: params['length'] = length
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_video_note(params)
        return Message.dese(result)


    async def send_media_group(
        self,
        chat_id: Union[int, str],
        media: list[Union[InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo]],
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None
    ) -> list[Message]:
        '''\
        https://core.telegram.org/bots/api#sendmediagroup
        Use this method to send a group of photos, videos, documents or audios as
        an album. Documents and audio files can be only grouped in an album with messages
        of the same type. On success, an array of Messages that were sent is returned.'''
        params = {
            'chat_id': chat_id,
            'media': media
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        result = await super().send_media_group(params)
        return [Message.dese(message) for message in result]


    async def send_location(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        message_thread_id: Optional[int] = None,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendlocation
        Use this method to send point on the map. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if horizontal_accuracy is not None: params['horizontal_accuracy'] = horizontal_accuracy
        if live_period is not None: params['live_period'] = live_period
        if heading is not None: params['heading'] = heading
        if proximity_alert_radius is not None: params['proximity_alert_radius'] = proximity_alert_radius
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_location(params)
        return Message.dese(result)


    async def send_venue(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        message_thread_id: Optional[int] = None,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendvenue
        Use this method to send information about a venue. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'title': title,
            'address': address
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if foursquare_id is not None: params['foursquare_id'] = foursquare_id
        if foursquare_type is not None: params['foursquare_type'] = foursquare_type
        if google_place_id is not None: params['google_place_id'] = google_place_id
        if google_place_type is not None: params['google_place_type'] = google_place_type
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_venue(params)
        return Message.dese(result)


    async def send_contact(
        self,
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        message_thread_id: Optional[int] = None,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendcontact
        Use this method to send phone contacts. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if last_name is not None: params['last_name'] = last_name
        if vcard is not None: params['vcard'] = vcard
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_contact(params)
        return Message.dese(result)


    async def send_poll(
        self,
        chat_id: Union[int, str],
        question: str,
        options: list[str],
        message_thread_id: Optional[int] = None,
        is_anonymous: Optional[bool] = None,
        type: Optional[str] = None,
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = None,
        explanation_entities: Optional[list[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendpoll
        Use this method to send a native poll. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'question': question,
            'options': options
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if is_anonymous is not None: params['is_anonymous'] = is_anonymous
        if type is not None: params['type'] = type
        if allows_multiple_answers is not None: params['allows_multiple_answers'] = allows_multiple_answers
        if correct_option_id is not None: params['correct_option_id'] = correct_option_id
        if explanation is not None: params['explanation'] = explanation
        if explanation_parse_mode is not None: params['explanation_parse_mode'] = explanation_parse_mode
        if explanation_entities is not None: params['explanation_entities'] = explanation_entities
        if open_period is not None: params['open_period'] = open_period
        if close_date is not None: params['close_date'] = close_date
        if is_closed is not None: params['is_closed'] = is_closed
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_poll(params)
        return Message.dese(result)


    async def send_dice(
        self,
        chat_id: Union[int, str],
        message_thread_id: Optional[int] = None,
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#senddice
        Use this method to send an animated emoji that will
        display a random value. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if emoji is not None: params['emoji'] = emoji
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_dice(params)
        return Message.dese(result)


    async def send_chat_action(
        self,
        chat_id: Union[int, str],
        action: str,
        message_thread_id: Optional[int] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#sendchataction
        Use this method when you need to tell the user that something is happening on
        the bot's side. The status is set for 5 seconds or less (when a message arrives
        from your bot, Telegram clients clear its typing status). Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'action': action
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        return await super().send_chat_action(params)


    async def get_user_profile_photos(
        self,
        user_id: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None
    ) -> UserProfilePhotos:
        '''\
        https://core.telegram.org/bots/api#getuserprofilephotos
        Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.'''
        params = {
            'user_id': user_id
        }
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        result = await super().get_user_profile_photos(params)
        return UserProfilePhotos.dese(result)


    async def get_file(
        self,
        file_id: str
    ) -> File:
        '''\
        https://core.telegram.org/bots/api#getfile
        Use this method to get basic information about a file and prepare it for
        downloading. For the moment, bots can download files of up to 20MB in size.
        On success, a File object is returned. The file can then be downloaded via the
        link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is
        taken from the response. It is guaranteed that the link will be valid for at least
        1 hour. When the link expires, a new one can be requested by calling getFile again.'''
        params = {
            'file_id': file_id
        }
        result = await super().get_file(params)
        return File.dese(result)


    async def ban_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#banchatmember
        Use this method to ban a user in a group, a supergroup or a channel. In the case
        of supergroups and channels, the user will not be able to return to the chat on their
        own using invite links, etc., unless unbanned first. The bot must be an administrator
        in the chat for this to work and must have the appropriate administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        if until_date is not None: params['until_date'] = until_date
        if revoke_messages is not None: params['revoke_messages'] = revoke_messages
        return await super().ban_chat_member(params)


    async def unban_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: Optional[bool] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#unbanchatmember
        Use this method to unban a previously banned user in a supergroup or channel. The user will not return
        to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator
        for this to work. By default, this method guarantees that after the call the user is not a member of the chat,
        but will be able to join it. So if the user is a member of the chat they will also be removed from the chat.
        If you don't want this, use the parameter only_if_banned. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        if only_if_banned is not None: params['only_if_banned'] = only_if_banned
        return await super().unban_chat_member(params)


    async def restrict_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: Optional[bool] = None,
        until_date: Optional[int] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#restrictchatmember
        Use this method to restrict a user in a supergroup. The bot must be an administrator in
        the supergroup for this to work and must have the appropriate administrator rights.
        Pass True for all permissions to lift restrictions from a user. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'permissions': permissions
        }
        if use_independent_chat_permissions is not None: params['use_independent_chat_permissions'] = use_independent_chat_permissions
        if until_date is not None: params['until_date'] = until_date
        return await super().restrict_chat_member(params)


    async def promote_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: Optional[bool] = None,
        can_manage_chat: Optional[bool] = None,
        can_delete_messages: Optional[bool] = None,
        can_manage_video_chats: Optional[bool] = None,
        can_restrict_members: Optional[bool] = None,
        can_promote_members: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_post_stories: Optional[bool] = None,
        can_edit_stories: Optional[bool] = None,
        can_delete_stories: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#promotechatmember
        Use this method to promote or demote a user in a supergroup or a channel. The bot must be
        an administrator in the chat for this to work and must have the appropriate administrator
        rights. Pass False for all boolean parameters to demote a user. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        if is_anonymous is not None: params['is_anonymous'] = is_anonymous
        if can_manage_chat is not None: params['can_manage_chat'] = can_manage_chat
        if can_delete_messages is not None: params['can_delete_messages'] = can_delete_messages
        if can_manage_video_chats is not None: params['can_manage_video_chats'] = can_manage_video_chats
        if can_restrict_members is not None: params['can_restrict_members'] = can_restrict_members
        if can_promote_members is not None: params['can_promote_members'] = can_promote_members
        if can_change_info is not None: params['can_change_info'] = can_change_info
        if can_invite_users is not None: params['can_invite_users'] = can_invite_users
        if can_post_messages is not None: params['can_post_messages'] = can_post_messages
        if can_edit_messages is not None: params['can_edit_messages'] = can_edit_messages
        if can_pin_messages is not None: params['can_pin_messages'] = can_pin_messages
        if can_post_stories is not None: params['can_post_stories'] = can_post_stories
        if can_edit_stories is not None: params['can_edit_stories'] = can_edit_stories
        if can_delete_stories is not None: params['can_delete_stories'] = can_delete_stories
        if can_manage_topics is not None: params['can_manage_topics'] = can_manage_topics
        return await super().promote_chat_member(params)


    async def set_chat_administrator_custom_title(
        self,
        chat_id: Union[int, str],
        user_id: int,
        custom_title: str
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setchatadministratorcustomtitle
        Use this method to set a custom title for an administrator
        in a supergroup promoted by the bot. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'custom_title': custom_title
        }
        return await super().set_chat_administrator_custom_title(params)


    async def ban_chat_sender_chat(
        self,
        chat_id: Union[int, str],
        sender_chat_id: int
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#banchatsenderchat
        Use this method to ban a channel chat in a supergroup or a channel. Until
        the chat is unbanned, the owner of the banned chat won't be able to send messages
        on behalf of any of their channels. The bot must be an administrator in the supergroup or
        channel for this to work and must have the appropriate administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id
        }
        return await super().ban_chat_sender_chat(params)


    async def unban_chat_sender_chat(
        self,
        chat_id: Union[int, str],
        sender_chat_id: int
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#unbanchatsenderchat
        Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an
        administrator for this to work and must have the appropriate administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id
        }
        return await super().unban_chat_sender_chat(params)


    async def set_chat_permissions(
        self,
        chat_id: Union[int, str],
        permissions: ChatPermissions,
        use_independent_chat_permissions: Optional[bool] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setchatpermissions
        Use this method to set default chat permissions for all members. The bot
        must be an administrator in the group or a supergroup for this to work and
        must have the can_restrict_members administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'permissions': permissions
        }
        if use_independent_chat_permissions is not None: params['use_independent_chat_permissions'] = use_independent_chat_permissions
        return await super().set_chat_permissions(params)


    async def export_chat_invite_link(
        self,
        chat_id: Union[int, str]
    ) -> str:
        '''\
        https://core.telegram.org/bots/api#exportchatinvitelink
        Use this method to generate a new primary invite link for a chat; any previously generated
        primary link is revoked. The bot must be an administrator in the chat for this to work and must
        have the appropriate administrator rights. Returns the new invite link as String on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().export_chat_invite_link(params)


    async def create_chat_invite_link(
        self,
        chat_id: Union[int, str],
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None
    ) -> ChatInviteLink:
        '''\
        https://core.telegram.org/bots/api#createchatinvitelink
        Use this method to create an additional invite link for a chat. The bot must be an administrator
        in the chat for this to work and must have the appropriate administrator rights. The link can be
        revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object.'''
        params = {
            'chat_id': chat_id
        }
        if name is not None: params['name'] = name
        if expire_date is not None: params['expire_date'] = expire_date
        if member_limit is not None: params['member_limit'] = member_limit
        if creates_join_request is not None: params['creates_join_request'] = creates_join_request
        result = await super().create_chat_invite_link(params)
        return ChatInviteLink.dese(result)


    async def edit_chat_invite_link(
        self,
        chat_id: Union[int, str],
        invite_link: str,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None
    ) -> ChatInviteLink:
        '''\
        https://core.telegram.org/bots/api#editchatinvitelink
        Use this method to edit a non-primary invite link created by the bot. The bot
        must be an administrator in the chat for this to work and must have the appropriate
        administrator rights. Returns the edited invite link as a ChatInviteLink object.'''
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link
        }
        if name is not None: params['name'] = name
        if expire_date is not None: params['expire_date'] = expire_date
        if member_limit is not None: params['member_limit'] = member_limit
        if creates_join_request is not None: params['creates_join_request'] = creates_join_request
        result = await super().edit_chat_invite_link(params)
        return ChatInviteLink.dese(result)


    async def revoke_chat_invite_link(
        self,
        chat_id: Union[int, str],
        invite_link: str
    ) -> ChatInviteLink:
        '''\
        https://core.telegram.org/bots/api#revokechatinvitelink
        Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new
        link is automatically generated. The bot must be an administrator in the chat for this to work and must
        have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object.'''
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link
        }
        result = await super().revoke_chat_invite_link(params)
        return ChatInviteLink.dese(result)


    async def approve_chat_join_request(
        self,
        chat_id: Union[int, str],
        user_id: int
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#approvechatjoinrequest
        Use this method to approve a chat join request. The bot must be an administrator in the chat
        for this to work and must have the can_invite_users administrator right. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await super().approve_chat_join_request(params)


    async def decline_chat_join_request(
        self,
        chat_id: Union[int, str],
        user_id: int
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#declinechatjoinrequest
        Use this method to decline a chat join request. The bot must be an administrator in the chat
        for this to work and must have the can_invite_users administrator right. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await super().decline_chat_join_request(params)


    async def set_chat_photo(
        self,
        chat_id: Union[int, str],
        photo: InputFile
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setchatphoto
        Use this method to set a new profile photo for the chat. Photos can't be changed
        for private chats. The bot must be an administrator in the chat for this to work
        and must have the appropriate administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'photo': photo
        }
        return await super().set_chat_photo(params)


    async def delete_chat_photo(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#deletechatphoto
        Use this method to delete a chat photo. Photos can't be changed for
        private chats. The bot must be an administrator in the chat for this to work
        and must have the appropriate administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().delete_chat_photo(params)


    async def set_chat_title(
        self,
        chat_id: Union[int, str],
        title: str
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setchattitle
        Use this method to change the title of a chat. Titles can't be changed for
        private chats. The bot must be an administrator in the chat for this to work
        and must have the appropriate administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'title': title
        }
        return await super().set_chat_title(params)


    async def set_chat_description(
        self,
        chat_id: Union[int, str],
        description: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setchatdescription
        Use this method to change the description of a group, a supergroup or a
        channel. The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        if description is not None: params['description'] = description
        return await super().set_chat_description(params)


    async def pin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: Optional[bool] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#pinchatmessage
        Use this method to add a message to the list of pinned messages in a chat. If the chat is not a
        private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages'
        administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        if disable_notification is not None: params['disable_notification'] = disable_notification
        return await super().pin_chat_message(params)


    async def unpin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: Optional[int] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#unpinchatmessage
        Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a
        private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages'
        administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        if message_id is not None: params['message_id'] = message_id
        return await super().unpin_chat_message(params)


    async def unpin_all_chat_messages(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#unpinallchatmessages
        Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the
        bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator
        right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().unpin_all_chat_messages(params)


    async def leave_chat(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#leavechat
        Use this method for your bot to leave a group, supergroup or channel. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().leave_chat(params)


    async def get_chat(
        self,
        chat_id: Union[int, str]
    ) -> Chat:
        '''\
        https://core.telegram.org/bots/api#getchat
        Use this method to get up to date information about the chat (current name of the user for one-on-one
        conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.'''
        params = {
            'chat_id': chat_id
        }
        result = await super().get_chat(params)
        return Chat.dese(result)


    async def get_chat_administrators(
        self,
        chat_id: Union[int, str]
    ) -> list[ChatMember]:
        '''\
        https://core.telegram.org/bots/api#getchatadministrators
        Use this method to get a list of administrators in a chat, which aren't bots. Returns an Array of ChatMember objects.'''
        params = {
            'chat_id': chat_id
        }
        result = await super().get_chat_administrators(params)
        return [ChatMember.dese(chat_member) for chat_member in result]


    async def get_chat_member_count(
        self,
        chat_id: Union[int, str]
    ) -> int:
        '''\
        https://core.telegram.org/bots/api#getchatmembercount
        Use this method to get the number of members in a chat. Returns Int on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().get_chat_member_count(params)


    async def get_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int
    ) -> ChatMember:
        '''\
        https://core.telegram.org/bots/api#getchatmember
        Use this method to get information about a member of a chat. The method is only guaranteed to work
        for other users if the bot is an administrator in the chat. Returns a ChatMember object on success.'''
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        result = await super().get_chat_member(params)
        return ChatMember.dese(result)


    async def set_chat_sticker_set(
        self,
        chat_id: Union[int, str],
        sticker_set_name: str
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setchatstickerset
        Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the
        chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set
        optionally returned in getChat requests to check if the bot can use this method. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'sticker_set_name': sticker_set_name
        }
        return await super().set_chat_sticker_set(params)


    async def delete_chat_sticker_set(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#deletechatstickerset
        Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the
        chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set
        optionally returned in getChat requests to check if the bot can use this method. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().delete_chat_sticker_set(params)


    async def get_forum_topic_icon_stickers(self) -> list[Sticker]:
        '''\
        https://core.telegram.org/bots/api#getforumtopiciconstickers
        Use this method to get custom emoji stickers, which can be used as a forum topic
        icon by any user. Requires no parameters. Returns an Array of Sticker objects.'''
        result = await super().get_forum_topic_icon_stickers()
        return [Sticker.dese(sticker) for sticker in result]


    async def create_forum_topic(
        self,
        chat_id: Union[int, str],
        name: str,
        icon_color: Optional[int] = None,
        icon_custom_emoji_id: Optional[str] = None
    ) -> ForumTopic:
        '''\
        https://core.telegram.org/bots/api#createforumtopic
        Use this method to create a topic in a forum supergroup chat. The bot must be
        an administrator in the chat for this to work and must have the can_manage_topics
        administrator rights. Returns information about the created topic as a ForumTopic object.'''
        params = {
            'chat_id': chat_id,
            'name': name
        }
        if icon_color is not None: params['icon_color'] = icon_color
        if icon_custom_emoji_id is not None: params['icon_custom_emoji_id'] = icon_custom_emoji_id
        result = await super().create_forum_topic(params)
        return ForumTopic.dese(result)


    async def edit_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int,
        name: Optional[str] = None,
        icon_custom_emoji_id: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#editforumtopic
        Use this method to edit name and icon of a topic in a forum supergroup chat. The bot
        must be an administrator in the chat for this to work and must have can_manage_topics
        administrator rights, unless it is the creator of the topic. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        if name is not None: params['name'] = name
        if icon_custom_emoji_id is not None: params['icon_custom_emoji_id'] = icon_custom_emoji_id
        return await super().edit_forum_topic(params)


    async def close_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#closeforumtopic
        Use this method to close an open topic in a forum supergroup chat. The bot must
        be an administrator in the chat for this to work and must have the can_manage_topics
        administrator rights, unless it is the creator of the topic. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await super().close_forum_topic(params)


    async def reopen_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#reopenforumtopic
        Use this method to reopen a closed topic in a forum supergroup chat. The bot must
        be an administrator in the chat for this to work and must have the can_manage_topics
        administrator rights, unless it is the creator of the topic. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await super().reopen_forum_topic(params)


    async def delete_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#deleteforumtopic
        Use this method to delete a forum topic along with all its messages in a forum
        supergroup chat. The bot must be an administrator in the chat for this to work and
        must have the can_delete_messages administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await super().delete_forum_topic(params)


    async def unpin_all_forum_topic_messages(
        self,
        chat_id: Union[int, str],
        message_thread_id: int
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#unpinallforumtopicmessages
        Use this method to clear the list of pinned messages in a forum topic.
        The bot must be an administrator in the chat for this to work and must have the
        can_pin_messages administrator right in the supergroup. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await super().unpin_all_forum_topic_messages(params)


    async def edit_general_forum_topic(
        self,
        chat_id: Union[int, str],
        name: str
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#editgeneralforumtopic
        Use this method to edit the name of the 'General' topic in a forum supergroup
        chat. The bot must be an administrator in the chat for this to work and must
        have can_manage_topics administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'name': name
        }
        return await super().edit_general_forum_topic(params)


    async def close_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#closegeneralforumtopic
        Use this method to close an open 'General' topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have
        the can_manage_topics administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().close_general_forum_topic(params)


    async def reopen_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#reopengeneralforumtopic
        Use this method to reopen a closed 'General' topic in a forum supergroup chat. The bot must be
        an administrator in the chat for this to work and must have the can_manage_topics administrator
        rights. The topic will be automatically unhidden if it was hidden. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().reopen_general_forum_topic(params)


    async def hide_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#hidegeneralforumtopic
        Use this method to hide the 'General' topic in a forum supergroup chat. The bot must be an
        administrator in the chat for this to work and must have the can_manage_topics administrator
        rights. The topic will be automatically closed if it was open. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().hide_general_forum_topic(params)


    async def unhide_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#unhidegeneralforumtopic
        Use this method to unhide the 'General' topic in a forum supergroup
        chat. The bot must be an administrator in the chat for this to work and must
        have the can_manage_topics administrator rights. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().unhide_general_forum_topic(params)


    async def unpin_all_general_forum_topic_messages(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#unpinallgeneralforumtopicmessages
        Use this method to clear the list of pinned messages in a General forum topic.
        The bot must be an administrator in the chat for this to work and must have the
        can_pin_messages administrator right in the supergroup. Returns True on success.'''
        params = {
            'chat_id': chat_id
        }
        return await super().unpin_all_general_forum_topic_messages(params)


    async def answer_callback_query(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#answercallbackquery
        Use this method to send answers to callback queries sent from inline
        keyboards. The answer will be displayed to the user as a notification at
        the top of the chat screen or as an alert. On success, True is returned.'''
        params = {
            'callback_query_id': callback_query_id
        }
        if text is not None: params['text'] = text
        if show_alert is not None: params['show_alert'] = show_alert
        if url is not None: params['url'] = url
        if cache_time is not None: params['cache_time'] = cache_time
        return await super().answer_callback_query(params)


    async def set_my_commands(
        self,
        commands: list[BotCommand],
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setmycommands
        Use this method to change the list of the bot's commands. See this
        manual for more details about bot commands. Returns True on success.'''
        params = {
            'commands': commands
        }
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_commands(params)


    async def delete_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#deletemycommands
        Use this method to delete the list of the bot's commands for
        the given scope and user language. After deletion, higher level
        commands will be shown to affected users. Returns True on success.'''
        params = {}
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        return await super().delete_my_commands(params)


    async def get_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> list[BotCommand]:
        '''\
        https://core.telegram.org/bots/api#getmycommands
        Use this method to get the current list of the bot's commands for the given scope and user
        language. Returns an Array of BotCommand objects. If commands aren't set, an empty list is returned.'''
        params = {}
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_commands(params)
        return [BotCommand.dese(bot_command) for bot_command in result]


    async def set_my_name(
        self,
        name: Optional[str] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setmyname
        Use this method to change the bot's name. Returns True on success.'''
        params = {}
        if name is not None: params['name'] = name
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_name(params)


    async def get_my_name(
        self,
        language_code: Optional[str] = None
    ) -> BotName:
        '''\
        https://core.telegram.org/bots/api#getmyname
        Use this method to get the current bot name for the given user language. Returns BotName on success.'''
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_name(params)
        return BotName.dese(result)


    async def set_my_description(
        self,
        description: Optional[str] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setmydescription
        Use this method to change the bot's description, which is shown in
        the chat with the bot if the chat is empty. Returns True on success.'''
        params = {}
        if description is not None: params['description'] = description
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_description(params)


    async def get_my_description(
        self,
        language_code: Optional[str] = None
    ) -> BotDescription:
        '''\
        https://core.telegram.org/bots/api#getmydescription
        Use this method to get the current bot description for
        the given user language. Returns BotDescription on success.'''
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_description(params)
        return BotDescription.dese(result)


    async def set_my_short_description(
        self,
        short_description: Optional[str] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setmyshortdescription
        Use this method to change the bot's short description, which is shown on the bot's profile
        page and is sent together with the link when users share the bot. Returns True on success.'''
        params = {}
        if short_description is not None: params['short_description'] = short_description
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_short_description(params)


    async def get_my_short_description(
        self,
        language_code: Optional[str] = None
    ) -> BotShortDescription:
        '''\
        https://core.telegram.org/bots/api#getmyshortdescription
        Use this method to get the current bot short description for
        the given user language. Returns BotShortDescription on success.'''
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_short_description(params)
        return BotShortDescription.dese(result)


    async def set_chat_menu_button(
        self,
        chat_id: Optional[int] = None,
        menu_button: Optional[MenuButton] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setchatmenubutton
        Use this method to change the bot's menu button in a private
        chat, or the default menu button. Returns True on success.'''
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if menu_button is not None: params['menu_button'] = menu_button
        return await super().set_chat_menu_button(params)


    async def get_chat_menu_button(
        self,
        chat_id: Optional[int] = None
    ) -> MenuButton:
        '''\
        https://core.telegram.org/bots/api#getchatmenubutton
        Use this method to get the current value of the bot's menu button in a
        private chat, or the default menu button. Returns MenuButton on success.'''
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        result = await super().get_chat_menu_button(params)
        return MenuButton.dese(result)


    async def set_my_default_administrator_rights(
        self,
        rights: Optional[ChatAdministratorRights] = None,
        for_channels: Optional[bool] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setmydefaultadministratorrights
        Use this method to change the default administrator rights requested by the bot when
        it's added as an administrator to groups or channels. These rights will be suggested to
        users, but they are free to modify the list before adding the bot. Returns True on success.'''
        params = {}
        if rights is not None: params['rights'] = rights
        if for_channels is not None: params['for_channels'] = for_channels
        return await super().set_my_default_administrator_rights(params)


    async def get_my_default_administrator_rights(
        self,
        for_channels: Optional[bool] = None
    ) -> ChatAdministratorRights:
        '''\
        https://core.telegram.org/bots/api#getmydefaultadministratorrights
        Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success.'''
        params = {}
        if for_channels is not None: params['for_channels'] = for_channels
        result = await super().get_my_default_administrator_rights(params)
        return ChatAdministratorRights.dese(result)


    async def edit_message_text(
        self,
        text: str,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[list[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''\
        https://core.telegram.org/bots/api#editmessagetext
        Use this method to edit text and game messages. On success, if the edited message
        is not an inline message, the edited Message is returned, otherwise True is returned.'''
        params = {
            'text', text
        }
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if entities is not None: params['entities'] = entities
        if disable_web_page_preview is not None: params['disable_web_page_preview'] = disable_web_page_preview
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_text(params)
        return Message.dese(result) if result is not True else True


    async def edit_message_caption(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[list[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''\
        https://core.telegram.org/bots/api#editmessagecaption
        Use this method to edit captions of messages. On success, if the edited message is
        not an inline message, the edited Message is returned, otherwise True is returned.'''
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        elif self.parse_mode is not None: params['parse_mode'] = self.parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_caption(params)
        return Message.dese(result) if result is not True else True


    async def edit_message_media(
        self,
        media: InputMedia,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''\
        https://core.telegram.org/bots/api#editmessagemedia
        Use this method to edit animation, audio, document, photo, or video messages. If a message is part
        of a message album, then it can be edited only to an audio for audio albums, only to a document for
        document albums and to a photo or a video otherwise. When an inline message is edited, a new file
        can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the
        edited message is not an inline message, the edited Message is returned, otherwise True is returned.'''
        params = {
            'media': media
        }
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_media(params)
        return Message.dese(result) if result is not True else True


    async def edit_message_live_location(
        self,
        latitude: float,
        longitude: float,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        horizontal_accuracy: Optional[float] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''\
        https://core.telegram.org/bots/api#editmessagelivelocation
        Use this method to edit live location messages. A location can be edited until its live_period
        expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the
        edited message is not an inline message, the edited Message is returned, otherwise True is returned.'''
        params = {
            'latitude': latitude,
            'longitude': longitude
        }
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if horizontal_accuracy is not None: params['horizontal_accuracy'] = horizontal_accuracy
        if heading is not None: params['heading'] = heading
        if proximity_alert_radius is not None: params['proximity_alert_radius'] = proximity_alert_radius
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_live_location(params)
        return Message.dese(result) if result is not True else True


    async def stop_message_live_location(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''\
        https://core.telegram.org/bots/api#stopmessagelivelocation
        Use this method to stop updating a live location message before live_period expires. On success,
        if the message is not an inline message, the edited Message is returned, otherwise True is returned.'''
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().stop_message_live_location(params)
        return Message.dese(result) if result is not True else True


    async def edit_message_reply_markup(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Union[Message, Literal[True]]:
        '''\
        https://core.telegram.org/bots/api#editmessagereplymarkup
        Use this method to edit only the reply markup of messages. On success, if the edited
        message is not an inline message, the edited Message is returned, otherwise True is returned.'''
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_reply_markup(params)
        return Message.dese(result) if result is not True else True


    async def stop_poll(
        self,
        chat_id: Union[int, str],
        message_id: int,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Poll:
        '''\
        https://core.telegram.org/bots/api#stoppoll
        Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.'''
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().stop_poll(params)
        return Poll.dese(result)


    async def delete_message(
        self,
        chat_id: Union[int, str],
        message_id: int
    ) -> Literal[True]:
        '''\
        Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.
        Use this method to delete a message, including service messages, with the following limitations:
        - A message can only be deleted if it was sent less than 48 hours ago.
        - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
        - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted can_post_messages permissions can delete outgoing messages in channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.
        Returns True on success.'''
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        return await super().delete_message(params)


    async def send_sticker(
        self,
        chat_id: Union[int, str],
        sticker: Union[InputFile, str],
        message_thread_id: Optional[int] = None,
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendsticker
        Use this method to send static .WEBP, animated .TGS, or
        video .WEBM stickers. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'sticker': sticker
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if emoji is not None: params['emoji'] = emoji
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_sticker(params)
        return Message.dese(result)


    async def get_sticker_set(
        self,
        name: str
    ) -> StickerSet:
        '''\
        https://core.telegram.org/bots/api#getstickerset
        Use this method to get a sticker set. On success, a StickerSet object is returned.'''
        params = {
            'name': name
        }
        result = await super().get_sticker_set(params)
        return StickerSet.dese(result)


    async def get_custom_emoji_stickers(
        self,
        custom_emoji_ids: list[str]
    ) -> list[Sticker]:
        '''\
        https://core.telegram.org/bots/api#getcustomemojistickers
        Use this method to get information about custom emoji stickers
        by their identifiers. Returns an Array of Sticker objects.'''
        params = {
            'custom_emoji_ids': custom_emoji_ids
        }
        result = await super().get_custom_emoji_stickers(params)
        return [Sticker.dese(sticker) for sticker in result]


    async def upload_sticker_file(
        self,
        user_id: int,
        sticker: InputFile,
        sticker_format: str
    ) -> File:
        '''\
        https://core.telegram.org/bots/api#uploadstickerfile
        Use this method to upload a file with a sticker for later use in the createNewStickerSet and
        addStickerToSet methods (the file can be used multiple times). Returns the uploaded File on success.'''
        params = {
            'user_id': user_id,
            'sticker': sticker,
            'sticker_format': sticker_format
        }
        result = await super().upload_sticker_file(params)
        return File.dese(result)


    async def create_new_sticker_set(
        self,
        user_id: int,
        name: str,
        title: str,
        stickers: list[InputSticker],
        sticker_format: str,
        sticker_type: Optional[str] = None,
        needs_repainting: Optional[bool] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#createnewstickerset
        Use this method to create a new sticker set owned by a user. The bot
        will be able to edit the sticker set thus created. Returns True on success.'''
        params = {
            'user_id': user_id,
            'name': name,
            'title': title,
            'stickers': stickers,
            'sticker_format': sticker_format
        }
        if sticker_type is not None: params['sticker_type'] = sticker_type
        if needs_repainting is not None: params['needs_repainting'] = needs_repainting
        return await super().create_new_sticker_set(params)


    async def add_sticker_to_set(
        self,
        user_id: int,
        name: str,
        sticker: InputSticker
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#addstickertoset
        Use this method to add a new sticker to a set created by the bot. The format of the
        added sticker must match the format of the other stickers in the set. Emoji sticker
        sets can have up to 200 stickers. Animated and video sticker sets can have up to 50
        stickers. Static sticker sets can have up to 120 stickers. Returns True on success.'''
        params = {
            'user_id': user_id,
            'name': name,
            'sticker': sticker
        }
        return await super().add_sticker_to_set(params)


    async def set_sticker_position_in_set(
        self,
        sticker: str,
        position: int
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setstickerpositioninset
        Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.'''
        params = {
            'sticker': sticker,
            'position': position
        }
        return await super().set_sticker_position_in_set(params)


    async def delete_sticker_from_set(
        self,
        sticker: str
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#deletestickerfromset
        Use this method to delete a sticker from a set created by the bot. Returns True on success.'''
        params = {
            'sticker': sticker
        }
        return await super().delete_sticker_from_set(params)


    async def set_sticker_emoji_list(
        self,
        sticker: str,
        emoji_list: list[str]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setstickeremojilist
        Use this method to change the list of emoji assigned to a regular or custom emoji sticker.
        The sticker must belong to a sticker set created by the bot. Returns True on success.'''
        params = {
            'sticker': sticker,
            'emoji_list': emoji_list
        }
        return await super().set_sticker_emoji_list(params)


    async def set_sticker_keywords(
        self,
        sticker: str,
        keywords: Optional[list[str]] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setstickerkeywords
        Use this method to change search keywords assigned to a regular or custom emoji sticker.
        The sticker must belong to a sticker set created by the bot. Returns True on success.'''
        params = {
            'sticker': sticker
        }
        if keywords is not None: params['keywords'] = keywords
        return await super().set_sticker_keywords(params)


    async def set_sticker_mask_position(
        self,
        sticker: str,
        mask_position: Optional[MaskPosition] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setstickermaskposition
        Use this method to change the mask position of a mask sticker. The sticker
        must belong to a sticker set that was created by the bot. Returns True on success.'''
        params = {
            'sticker': sticker
        }
        if mask_position is not None: params['mask_position'] = mask_position
        return await super().set_sticker_mask_position(params)


    async def set_sticker_set_title(
        self,
        name: str,
        title: str
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setstickersettitle
        Use this method to set the title of a created sticker set. Returns True on success.'''
        params = {
            'name': name,
            'title': title
        }
        return await super().set_sticker_set_title(params)


    async def set_sticker_set_thumbnail(
        self,
        name: str,
        user_id: int,
        thumbnail: Optional[Union[InputFile, str]] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setstickersetthumbnail
        Use this method to set the thumbnail of a regular or mask sticker set. The format of the
        thumbnail file must match the format of the stickers in the set. Returns True on success.'''
        params = {
            'name': name,
            'user_id': user_id
        }
        if thumbnail is not None: params['thumbnail'] = thumbnail
        return await super().set_sticker_set_thumbnail(params)


    async def set_custom_emoji_sticker_set_thumbnail(
        self,
        name: str,
        custom_emoji_id: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setcustomemojistickersetthumbnail
        Use this method to set the thumbnail of a custom emoji sticker set. Returns True on success.'''
        params = {
            'name': name
        }
        if custom_emoji_id is not None: params['custom_emoji_id'] = custom_emoji_id
        return await super().set_custom_emoji_sticker_set_thumbnail(params)


    async def delete_sticker_set(
        self,
        name: str
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#deletestickerset
        Use this method to delete a sticker set that was created by the bot. Returns True on success.'''
        params = {
            'name': name
        }
        return await super().delete_sticker_set(params)


    async def answer_inline_query(
        self,
        inline_query_id: str,
        results: list[InlineQueryResult],
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        button: Optional[InlineQueryResultsButton] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#answerinlinequery
        Use this method to send answers to an inline query. On success,
        True is returned. No more than 50 results per query are allowed.'''
        params = {
            'inline_query_id': inline_query_id,
            'results': results
        }
        if cache_time is not None: params['cache_time'] = cache_time
        if is_personal is not None: params['is_personal'] = is_personal
        if next_offset is not None: params['next_offset'] = next_offset
        if button is not None: params['button'] = button
        return await super().answer_inline_query(params)


    async def answer_web_app_query(
        self,
        web_app_query_id: str,
        result: InlineQueryResult
    ) -> SentWebAppMessage:
        '''\
        https://core.telegram.org/bots/api#answerwebappquery
        Use this method to set the result of an interaction with a Web App and
        send a corresponding message on behalf of the user to the chat from which
        the query originated. On success, a SentWebAppMessage object is returned.'''
        params = {
            'web_app_query_id': web_app_query_id,
            'result': result
        }
        result = await super().answer_web_app_query(params)
        return SentWebAppMessage.dese(result)


    async def send_invoice(
        self,
        chat_id: Union[int, str],
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: list[LabeledPrice],
        message_thread_id: Optional[int] = None,
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[list[int]] = None,
        start_parameter: Optional[str] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendinvoice
        Use this method to send invoices. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'title': title,
            'description': description,
            'payload': payload,
            'provider_token': provider_token,
            'currency': currency,
            'prices': prices
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if max_tip_amount is not None: params['max_tip_amount'] = max_tip_amount
        if suggested_tip_amounts is not None: params['suggested_tip_amounts'] = suggested_tip_amounts
        if start_parameter is not None: params['start_parameter'] = start_parameter
        if provider_data is not None: params['provider_data'] = provider_data
        if photo_url is not None: params['photo_url'] = photo_url
        if photo_size is not None: params['photo_size'] = photo_size
        if photo_width is not None: params['photo_width'] = photo_width
        if photo_height is not None: params['photo_height'] = photo_height
        if need_name is not None: params['need_name'] = need_name
        if need_phone_number is not None: params['need_phone_number'] = need_phone_number
        if need_email is not None: params['need_email'] = need_email
        if need_shipping_address is not None: params['need_shipping_address'] = need_shipping_address
        if send_phone_number_to_provider is not None: params['send_phone_number_to_provider'] = send_phone_number_to_provider
        if send_email_to_provider is not None: params['send_email_to_provider'] = send_email_to_provider
        if is_flexible is not None: params['is_flexible'] = is_flexible
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_invoice(params)
        return Message.dese(result)


    async def create_invoice_link(
        self,
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: list[LabeledPrice],
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[list[int]] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None
    ) -> str:
        '''\
        https://core.telegram.org/bots/api#createinvoicelink
        Use this method to create a link for an invoice. Returns the created invoice link as String on success.'''
        params = {
            'title': title,
            'description': description,
            'payload': payload,
            'provider_token': provider_token,
            'currency': currency,
            'prices': prices
        }
        if max_tip_amount is not None: params['max_tip_amount'] = max_tip_amount
        if suggested_tip_amounts is not None: params['suggested_tip_amounts'] = suggested_tip_amounts
        if provider_data is not None: params['provider_data'] = provider_data
        if photo_url is not None: params['photo_url'] = photo_url
        if photo_size is not None: params['photo_size'] = photo_size
        if photo_width is not None: params['photo_width'] = photo_width
        if photo_height is not None: params['photo_height'] = photo_height
        if need_name is not None: params['need_name'] = need_name
        if need_phone_number is not None: params['need_phone_number'] = need_phone_number
        if need_email is not None: params['need_email'] = need_email
        if need_shipping_address is not None: params['need_shipping_address'] = need_shipping_address
        if send_phone_number_to_provider is not None: params['send_phone_number_to_provider'] = send_phone_number_to_provider
        if send_email_to_provider is not None: params['send_email_to_provider'] = send_email_to_provider
        if is_flexible is not None: params['is_flexible'] = is_flexible
        return await super().create_invoice_link(params)


    async def answer_shipping_query(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: Optional[list[ShippingOption]] = None,
        error_message: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#answershippingquery
        If you sent an invoice requesting a shipping address and the parameter is_flexible
        was specified, the Bot API will send an Update with a shipping_query field to the
        bot. Use this method to reply to shipping queries. On success, True is returned.'''
        params = {
            'shipping_query_id': shipping_query_id,
            'ok': ok
        }
        if shipping_options is not None: params['shipping_options'] = shipping_options
        if error_message is not None: params['error_message'] = error_message
        return await super().answer_shipping_query(params)


    async def answer_pre_checkout_query(
        self,
        pre_checkout_query_id: str,
        ok: bool,
        error_message: Optional[str] = None
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#answerprecheckoutquery
        Once the user has confirmed their payment and shipping details, the Bot API sends the
        final confirmation in the form of an Update with the field pre_checkout_query. Use this
        method to respond to such pre-checkout queries. On success, True is returned. Note: The
        Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.'''
        params = {
            'pre_checkout_query_id': pre_checkout_query_id,
            'ok': ok
        }
        if error_message is not None: params['error_message'] = error_message
        return await super().answer_pre_checkout_query(params)


    async def set_passport_data_errors(
        self,
        user_id: int,
        errors: list[PassportElementError]
    ) -> Literal[True]:
        '''\
        https://core.telegram.org/bots/api#setpassportdataerrors
        Informs a user that some of the Telegram Passport elements they provided contains errors. The user
        will not be able to re-submit their Passport to you until the errors are fixed (the contents of the
        field for which you returned the error must change). Returns True on success. Use this if the data
        submitted by the user doesn't satisfy the standards your service requires for any reason. For example,
        if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering,
        etc. Supply some details in the error message to make sure the user knows how to correct the issues.'''
        params = {
            'user_id': user_id,
            'errors': errors
        }
        return await super().set_passport_data_errors(params)


    async def send_game(
        self,
        chat_id: int,
        game_short_name: str,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None
    ) -> Message:
        '''\
        https://core.telegram.org/bots/api#sendgame
        Use this method to send a game. On success, the sent Message is returned.'''
        params = {
            'chat_id': chat_id,
            'game_short_name': game_short_name
        }
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        elif self.protect_content is not None: params['protect_content'] = self.protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_game(params)
        return Message.dese(result)


    async def set_game_score(
        self,
        user_id: int,
        score: int,
        force: Optional[bool] = None,
        disable_edit_message: Optional[bool] = None,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None
    ) -> Union[Message, Literal[True]]:
        '''\
        https://core.telegram.org/bots/api#setgamescore
        Use this method to set the score of the specified user in a game message. On success, if the
        message is not an inline message, the Message is returned, otherwise True is returned. Returns an
        error, if the new score is not greater than the user's current score in the chat and force is False.'''
        params = {
            'user_id': user_id,
            'score': score
        }
        if force is not None: params['force'] = force
        if disable_edit_message is not None: params['disable_edit_message'] = disable_edit_message
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        result = await super().set_game_score(params)
        return Message.dese(result) if result is not True else True


    async def get_game_high_scores(
        self,
        user_id: int,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None
    ) -> list[GameHighScore]:
        '''\
        https://core.telegram.org/bots/api#getgamehighscores
        Use this method to get data for high score tables. Will return the score of the specified
        user and several of their neighbors in a game. Returns an Array of GameHighScore objects.'''
        params = {
            'user_id': user_id
        }
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        result = await super().get_game_high_scores(params)
        return [GameHighScore.dese(score) for score in result]
