#!/bin/python3

import re
try:
    with open('pyproject.toml') as read_v:
        __version__ = re.search(
            r'version.*=.*"(.*?)"',
            read_v.read()
        ).group(1)
except FileNotFoundError:
    __version__ = None

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

    async def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[list[str]] = None
    ) -> list[Update]:
        params = {}
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        if timeout is not None: params['timeout'] = timeout
        if allowed_updates is not None: params['allowed_updates'] = allowed_updates
        result = await super().get_updates(params)
        return [Update.dese(update) for update in result]

    async def get_me(self) -> User:
        result = await super().get_me()
        return User.dese(result)

    async def log_out(self) -> Literal[True]:
        return await super().log_out()

    async def close(self) -> Literal[True]:
        return await super().close()

    async def delete_message(
        self,
        chat_id: Union[int, str],
        message_id: int
    ) -> Literal[True]:
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        return await super().delete_message(params)

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
        reply_to_message_id: Optional[bool] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
    ) -> Message:
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
        params = {'chat_id': chat_id}
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
        params = {'user_id': user_id}
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        result = await super().get_user_profile_photos(params)
        return UserProfilePhotos.dese(result)

    async def get_file(self, file_id: str) -> File:
        params = {'file_id': file_id}
        result = await super().get_file(params)
        return File.dese(result)

    async def ban_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = None
    ) -> Literal[True]:
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
        params = {
            'chat_id': chat_id,
            'permissions': permissions
        }
        if use_independent_chat_permissions is not None: params['use_independent_chat_permissions'] = use_independent_chat_permissions
        return await super().set_chat_permissions(params)

    async def export_chat_invite_link(self, chat_id: Union[int, str]) -> str:
        params = {'chat_id': chat_id}
        return await super().export_chat_invite_link(params)

    async def create_chat_invite_link(
        self,
        chat_id: Union[int, str],
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None
    ) -> ChatInviteLink:
        params = {'chat_id': chat_id}
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
        params = {
            'chat_id': chat_id,
            'photo': photo
        }
        return await super().set_chat_photo(params)

    async def delete_chat_photo(self, chat_id: Union[int, str]) -> Literal[True]:
        params = {'chat_id': chat_id}
        return await super().delete_chat_photo(params)

    async def set_chat_title(
        self,
        chat_id: Union[int, str],
        title: str
    ) -> Literal[True]:
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
        params = {'chat_id': chat_id}
        if description is not None: params['description'] = description
        return await super().set_chat_description(params)

    async def pin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: Optional[bool] = None
    ) -> Literal[True]:
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
        params = {'chat_id': chat_id}
        if message_id is not None: params['message_id'] = message_id
        return await super().unpin_chat_message(params)

    async def unpin_all_chat_messages(self, chat_id: Union[int, str]) -> Literal[True]:
        params = {'chat_id': chat_id}
        return await super().unpin_all_chat_messages(params)

    async def leave_chat(self, chat_id: Union[int, str]) -> Literal[True]:
        params = {'chat_id': chat_id}
        return await super().leave_chat(params)

    async def get_chat(self, chat_id: Union[int, str]) -> Chat:
        params = {'chat_id': chat_id}
        result = await super().get_chat(params)
        return Chat.dese(result)

    async def get_chat_administrators(self, chat_id: Union[int, str]) -> list[ChatMember]:
        params = {'chat_id': chat_id}
        result = await super().get_chat_administrators(params)
        return [ChatMember.dese(chat_member) for chat_member in result]

    async def get_chat_member_count(self, chat_id: Union[int, str]) -> int:
        params = {'chat_id': chat_id}
        return await super().get_chat_member_count(params)

    async def get_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int
    ) -> ChatMember:
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
        params = {
            'chat_id': chat_id,
            'sticker_set_name': sticker_set_name
        }
        return await super().set_chat_sticker_set(params)

    async def delete_chat_sticker_set(self, chat_id: Union[int, str]) -> Literal[True]:
        params = {'chat_id': chat_id}
        return await super().delete_chat_sticker_set(params)

    async def get_forum_topic_icon_stickers(self) -> list[Sticker]:
        result = await super().get_forum_topic_icon_stickers()
        return [Sticker.dese(sticker) for sticker in result]

    async def create_forum_topic(
        self,
        chat_id: Union[int, str],
        name: str,
        icon_color: Optional[int] = None,
        icon_custom_emoji_id: Optional[str] = None
    ) -> ForumTopic:
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
        params = {
            'chat_id': chat_id,
            'name': name
        }
        return await super().edit_general_forum_topic(params)

    async def close_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        params = {'chat_id': chat_id}
        return await super().close_general_forum_topic(params)

    async def reopen_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        params = {'chat_id': chat_id}
        return await super().reopen_general_forum_topic(params)

    async def hide_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        params = {'chat_id': chat_id}
        return await super().hide_general_forum_topic(params)

    async def unhide_general_forum_topic(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        params = {'chat_id': chat_id}
        return await super().unhide_general_forum_topic(params)

    async def unpin_all_general_forum_topic_messages(
        self,
        chat_id: Union[int, str]
    ) -> Literal[True]:
        params = {'chat_id': chat_id}
        return await super().unpin_all_general_forum_topic_messages(params)

    async def answer_callback_query(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None
    ) -> Literal[True]:
        params = {'callback_query_id': callback_query_id}
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
        params = {'commands': commands}
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_commands(params)

    async def delete_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        params = {}
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        return await super().delete_my_commands(params)

    async def get_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None
    ) -> list[BotCommand]:
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
        params = {}
        if name is not None: params['name'] = name
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_name(params)

    async def get_my_name(self, language_code: Optional[str] = None) -> BotName:
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_name(params)
        return BotName.dese(result)

    async def set_my_description(
        self,
        description: Optional[str] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        params = {}
        if description is not None: params['description'] = description
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_description(params)

    async def get_my_description(self, language_code: Optional[str] = None) -> BotDescription:
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_description(params)
        return BotDescription.dese(result)

    async def set_my_short_description(
        self,
        short_description: Optional[str] = None,
        language_code: Optional[str] = None
    ) -> Literal[True]:
        params = {}
        if short_description is not None: params['short_description'] = short_description
        if language_code is not None: params['language_code'] = language_code
        return await super().set_my_short_description(params)

    async def get_my_short_description(
        self,
        language_code: Optional[str] = None
    ) -> BotShortDescription:
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_short_description(params)
        return BotShortDescription.dese(result)

    async def set_chat_menu_button(
        self,
        chat_id: Optional[int] = None,
        menu_button: Optional[MenuButton] = None
    ) -> Literal[True]:
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if menu_button is not None: params['menu_button'] = menu_button
        return await super().set_chat_menu_button(params)

    async def get_chat_menu_button(self, chat_id: Optional[int] = None) -> MenuButton:
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        result = await super().get_chat_menu_button(params)
        return MenuButton.dese(result)

    async def set_my_default_administrator_rights(
        self,
        rights: Optional[ChatAdministratorRights] = None,
        for_channels: Optional[bool] = None
    ) -> Literal[True]:
        params = {}
        if rights is not None: params['rights'] = rights
        if for_channels is not None: params['for_channels'] = for_channels
        return await super().set_my_default_administrator_rights(params)

    async def get_my_default_administrator_rights(self, for_channels: Optional[bool] = None) -> ChatAdministratorRights:
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
        params = {'text', text}
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
        params = {'media': media}
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
        params = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().stop_poll(params)
        return Poll.dese(result)

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

    async def get_sticker_set(self, name: str) -> StickerSet:
        params = {'name': name}
        result = await super().get_sticker_set(params)
        return StickerSet.dese(result)

    async def get_custom_emoji_stickers(self, custom_emoji_ids: list[str]) -> list[Sticker]:
        params = {'custom_emoji_ids': custom_emoji_ids}
        result = await super().get_custom_emoji_stickers(params)
        return [Sticker.dese(sticker) for sticker in result]

    async def upload_sticker_file(
        self,
        user_id: int,
        sticker: InputFile,
        sticker_format: str
    ) -> File:
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
        params = {
            'sticker': sticker,
            'position': position
        }
        return await super().set_sticker_position_in_set(params)

    async def delete_sticker_from_set(self, sticker: str) -> Literal[True]:
        params = {'sticker': sticker}
        return await super().delete_sticker_from_set(params)

    async def set_sticker_emoji_list(
        self,
        sticker: str,
        emoji_list: list[str]
    ) -> Literal[True]:
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
        params = {'sticker': sticker}
        if keywords is not None: params['keywords'] = keywords
        return await super().set_sticker_keywords(params)

    async def set_sticker_mask_position(
        self,
        sticker: str,
        mask_position: Optional[MarkPosition] = None
    ) -> Literal[True]:
        params = {'sticker': sticker}
        if mask_position is not None: params['mask_position'] = mask_position
        return await super().set_sticker_mask_position(params)

    async def set_sticker_set_title(self, name: str, title: str) -> Literal[True]:
        params = {'name': name, 'title': title}
        return await super().set_sticker_set_title(params)

    async def set_sticker_set_thumbnail(
        self,
        name: str,
        user_id: int,
        thumbnail: Optional[Union[InputFile, str]] = None
    ) -> Literal[True]:
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
        params = {'name': name}
        if custom_emoji_id is not None: params['custom_emoji_id'] = custom_emoji_id
        return await super().set_custom_emoji_sticker_set_thumbnail(params)

    async def delete_sticker_set(self, name: str) -> Literal[True]:
        params = {'name': name}
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
        params = {'user_id': user_id}
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        result = await super().get_game_high_scores(params)
        return [GameHighScore.dese(score) for score in result]


######################################################################

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

    # Incoming updates process

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

