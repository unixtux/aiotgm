#!/bin/env python3

if __name__ != '__main__':
    import os
    raise OSError(f'{os.path.basename(__file__)} must be launched from __main__')

import logging
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(20)

from typing import (
    Union,
    Optional,
    Literal
)
from aiotgm.types import *
from aiotgm.types import (
    TelegramType,
    ChatMember,
    MessageOrigin,
    ReactionType,
    ChatBoostSource,
    InputMessageContent,
    MaybeInaccessibleMessage
)
from aiotgm.constants import *

TYPES = {
    Animation: {
        "link": "https://core.telegram.org/bots/api#animation",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "width": None,
            "height": None,
            "duration": None,
            "thumbnail": PhotoSize,
            "file_name": None,
            "mime_type": None,
            "file_size": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Audio: {
        "link": "https://core.telegram.org/bots/api#audio",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "duration": None,
            "performer": None,
            "title": None,
            "file_name": None,
            "mime_type": None,
            "file_size": None,
            "thumbnail": PhotoSize
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotCommand: {
        "link": "https://core.telegram.org/bots/api#botcommand",
        "has_dese": True,
        "dese_kwargs": {
            "command": None,
            "description": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotCommandScopeAllChatAdministrators: {
        "link": "https://core.telegram.org/bots/api#botcommandscopeallchatadministrators",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotCommandScopeAllGroupChats: {
        "link": "https://core.telegram.org/bots/api#botcommandscopeallgroupchats",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotCommandScopeAllPrivateChats: {
        "link": "https://core.telegram.org/bots/api#botcommandscopeallprivatechats",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotCommandScopeChat: {
        "link": "https://core.telegram.org/bots/api#botcommandscopechat",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotCommandScopeChatAdministrators: {
        "link": "https://core.telegram.org/bots/api#botcommandscopechatadministrators",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotCommandScopeChatMember: {
        "link": "https://core.telegram.org/bots/api#botcommandscopechatmember",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotCommandScopeDefault: {
        "link": "https://core.telegram.org/bots/api#botcommandscopedefault",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotDescription: {
        "link": "https://core.telegram.org/bots/api#botdescription",
        "has_dese": True,
        "dese_kwargs": {
            "description": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotName: {
        "link": "https://core.telegram.org/bots/api#botname",
        "has_dese": True,
        "dese_kwargs": {
            "name": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    BotShortDescription: {
        "link": "https://core.telegram.org/bots/api#botshortdescription",
        "has_dese": True,
        "dese_kwargs": {
            "short_description": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    CallbackGame: {
        "link": "https://core.telegram.org/bots/api#callbackgame",
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    CallbackQuery: {
        "link": "https://core.telegram.org/bots/api#callbackquery",
        "has_dese": True,
        "dese_kwargs": {
            "id": None,
            "from_user": User,
            "chat_instance": None,
            "message": MaybeInaccessibleMessage,
            "inline_message_id": None,
            "data": None,
            "game_short_name": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Chat: {
        "link": "https://core.telegram.org/bots/api#chat",
        "has_dese": True,
        "dese_kwargs": {
            "id": None,
            "type": None,
            "title": None,
            "username": None,
            "first_name": None,
            "last_name": None,
            "is_forum": None,
            "photo": ChatPhoto,
            "active_usernames": None,
            "available_reactions": Optional[list[ReactionType]],
            "accent_color_id": None,
            "background_custom_emoji_id": None,
            "profile_accent_color_id": None,
            "profile_background_custom_emoji_id": None,
            "emoji_status_custom_emoji_id": None,
            "emoji_status_expiration_date": None,
            "bio": None,
            "has_private_forwards": None,
            "has_restricted_voice_and_video_messages": None,
            "join_to_send_messages": None,
            "join_by_request": None,
            "description": None,
            "invite_link": None,
            "pinned_message": Message,
            "permissions": ChatPermissions,
            "slow_mode_delay": None,
            "unrestrict_boost_count": None,
            "message_auto_delete_time": None,
            "has_aggressive_anti_spam_enabled": None,
            "has_hidden_members": None,
            "has_protected_content": None,
            "has_visible_history": None,
            "sticker_set_name": None,
            "can_set_sticker_set": None,
            "custom_emoji_sticker_set_name": None,
            "linked_chat_id": None,
            "location": ChatLocation
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatAdministratorRights: {
        "link": "https://core.telegram.org/bots/api#chatadministratorrights",
        "has_dese": True,
        "dese_kwargs": {
            "is_anonymous": None,
            "can_manage_chat": None,
            "can_delete_messages": None,
            "can_manage_video_chats": None,
            "can_restrict_members": None,
            "can_promote_members": None,
            "can_change_info": None,
            "can_invite_users": None,
            "can_post_stories": None,
            "can_edit_stories": None,
            "can_delete_stories": None,
            "can_post_messages": None,
            "can_edit_messages": None,
            "can_pin_messages": None,
            "can_manage_topics": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatBoost: {
        "link": "https://core.telegram.org/bots/api#chatboost",
        "has_dese": True,
        "dese_kwargs": {
            "boost_id": None,
            "add_date": None,
            "expiration_date": None,
            "source": ChatBoostSource
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatBoostAdded: {
        "link": "https://core.telegram.org/bots/api#chatboostadded",
        "has_dese": True,
        "dese_kwargs": {
            "boost_count": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatBoostRemoved: {
        "link": "https://core.telegram.org/bots/api#chatboostremoved",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "boost_id": None,
            "remove_date": None,
            "source": ChatBoostSource
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatBoostSourceGiftCode: {
        "link": "https://core.telegram.org/bots/api#chatboostsourcegiftcode",
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatBoostSourceGiveaway: {
        "link": "https://core.telegram.org/bots/api#chatboostsourcegiveaway",
        "has_dese": True,
        "dese_kwargs": {
            "giveaway_message_id": None,
            "user": User,
            "is_unclaimed": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatBoostSourcePremium: {
        "link": "https://core.telegram.org/bots/api#chatboostsourcepremium",
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatBoostUpdated: {
        "link": "https://core.telegram.org/bots/api#chatboostupdated",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "boost": ChatBoost
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatInviteLink: {
        "link": "https://core.telegram.org/bots/api#chatinvitelink",
        "has_dese": True,
        "dese_kwargs": {
            "invite_link": None,
            "creator": User,
            "creates_join_request": None,
            "is_primary": None,
            "is_revoked": None,
            "name": None,
            "expire_date": None,
            "member_limit": None,
            "pending_join_request_count": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatJoinRequest: {
        "link": "https://core.telegram.org/bots/api#chatjoinrequest",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "from_user": User,
            "user_chat_id": None,
            "date": None,
            "bio": None,
            "invite_link": ChatInviteLink
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatLocation: {
        "link": "https://core.telegram.org/bots/api#chatlocation",
        "has_dese": True,
        "dese_kwargs": {
            "location": Location,
            "address": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatMemberAdministrator: {
        "link": "https://core.telegram.org/bots/api#chatmemberadministrator",
        "has_dese": True,
        "dese_kwargs": {
            "user": User,
            "can_be_edited": None,
            "is_anonymous": None,
            "can_manage_chat": None,
            "can_delete_messages": None,
            "can_manage_video_chats": None,
            "can_restrict_members": None,
            "can_promote_members": None,
            "can_change_info": None,
            "can_invite_users": None,
            "can_post_stories": None,
            "can_edit_stories": None,
            "can_delete_stories": None,
            "can_post_messages": None,
            "can_edit_messages": None,
            "can_pin_messages": None,
            "can_manage_topics": None,
            "custom_title": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatMemberBanned: {
        "link": "https://core.telegram.org/bots/api#chatmemberbanned",
        "has_dese": True,
        "dese_kwargs": {
            "user": User,
            "until_date": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatMemberLeft: {
        "link": "https://core.telegram.org/bots/api#chatmemberleft",
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatMemberMember: {
        "link": "https://core.telegram.org/bots/api#chatmembermember",
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatMemberOwner: {
        "link": "https://core.telegram.org/bots/api#chatmemberowner",
        "has_dese": True,
        "dese_kwargs": {
            "user": User,
            "is_anonymous": None,
            "custom_title": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatMemberRestricted: {
        "link": "https://core.telegram.org/bots/api#chatmemberrestricted",
        "has_dese": True,
        "dese_kwargs": {
            "user": User,
            "is_member": None,
            "can_send_messages": None,
            "can_send_audios": None,
            "can_send_documents": None,
            "can_send_photos": None,
            "can_send_videos": None,
            "can_send_video_notes": None,
            "can_send_voice_notes": None,
            "can_send_polls": None,
            "can_send_other_messages": None,
            "can_add_web_page_previews": None,
            "can_change_info": None,
            "can_invite_users": None,
            "can_pin_messages": None,
            "can_manage_topics": None,
            "until_date": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatPermissions: {
        "link": "https://core.telegram.org/bots/api#chatpermissions",
        "has_dese": True,
        "dese_kwargs": {
            "can_send_messages": None,
            "can_send_audios": None,
            "can_send_documents": None,
            "can_send_photos": None,
            "can_send_videos": None,
            "can_send_video_notes": None,
            "can_send_voice_notes": None,
            "can_send_polls": None,
            "can_send_other_messages": None,
            "can_add_web_page_previews": None,
            "can_change_info": None,
            "can_invite_users": None,
            "can_pin_messages": None,
            "can_manage_topics": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    SwitchInlineQueryChosenChat: {
        "link": "https://core.telegram.org/bots/api#switchinlinequerychosenchat",
        "has_dese": True,
        "dese_kwargs": {
            "query": None,
            "allow_user_chats": None,
            "allow_bot_chats": None,
            "allow_group_chats": None,
            "allow_channel_chats": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputFile: {
        "link": "https://core.telegram.org/bots/api#inputfile",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    LoginUrl: {
        "link": "https://core.telegram.org/bots/api#loginurl",
        "has_dese": True,
        "dese_kwargs": {
            "url": None,
            "forward_text": None,
            "bot_username": None,
            "request_write_access": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    LabeledPrice: {
        "link": "https://core.telegram.org/bots/api#labeledprice",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    LinkPreviewOptions: {
        "link": "https://core.telegram.org/bots/api#linkpreviewoptions",
        "has_dese": True,
        "dese_kwargs": {
            "is_disabled": None,
            "url": None,
            "prefer_small_media": None,
            "prefer_large_media": None,
            "show_above_text": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    User: {
        "link": "https://core.telegram.org/bots/api#user",
        "has_dese": True,
        "dese_kwargs": {
            "id": None,
            "is_bot": None,
            "first_name": None,
            "last_name": None,
            "username": None,
            "language_code": None,
            "is_premium": None,
            "added_to_attachment_menu": None,
            "can_join_groups": None,
            "can_read_all_group_messages": None,
            "supports_inline_queries": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MessageEntity: {
        "link": "https://core.telegram.org/bots/api#messageentity",
        "has_dese": True,
        "dese_kwargs": {
            "type": None,
            "offset": None,
            "length": None,
            "url": None,
            "user": User,
            "language": None,
            "custom_emoji_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    TextQuote: {
        "link": "https://core.telegram.org/bots/api#textquote",
        "has_dese": True,
        "dese_kwargs": {
            "text": None,
            "position": None,
            "entities": Optional[list[MessageEntity]],
            "is_manual": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ReplyParameters: {
        "link": "https://core.telegram.org/bots/api#replyparameters",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InaccessibleMessage: {
        "link": "https://core.telegram.org/bots/api#inaccessiblemessage",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "message_id": None,
            "date": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Message: {
        "link": "https://core.telegram.org/bots/api#message",
        "has_dese": True,
        "dese_kwargs": {
            "message_id": None,
            "date": None,
            "chat": Chat,
            "message_thread_id": None,
            "from_user": User,
            "sender_chat": Chat,
            "sender_boost_count": None,
            "forward_origin": MessageOrigin,
            "is_topic_message": None,
            "is_automatic_forward": None,
            "reply_to_message": Message,
            "external_reply": ExternalReplyInfo,
            "quote": TextQuote,
            "reply_to_story": Story,
            "via_bot": User,
            "edit_date": None,
            "has_protected_content": None,
            "media_group_id": None,
            "author_signature": None,
            "text": None,
            "entities": Optional[list[MessageEntity]],
            "link_preview_options": LinkPreviewOptions,
            "animation": Animation,
            "audio": Audio,
            "document": Document,
            "photo": Optional[list[PhotoSize]],
            "sticker": Sticker,
            "story": Story,
            "video": Video,
            "video_note": VideoNote,
            "voice": Voice,
            "caption": None,
            "caption_entities": Optional[list[MessageEntity]],
            "has_media_spoiler": None,
            "contact": Contact,
            "dice": Dice,
            "game": Game,
            "poll": Poll,
            "venue": Venue,
            "location": Location,
            "new_chat_members": Optional[list[User]],
            "left_chat_member": User,
            "new_chat_title": None,
            "new_chat_photo": Optional[list[PhotoSize]],
            "delete_chat_photo": None,
            "group_chat_created": None,
            "supergroup_chat_created": None,
            "channel_chat_created": None,
            "message_auto_delete_timer_changed": MessageAutoDeleteTimerChanged,
            "migrate_to_chat_id": None,
            "migrate_from_chat_id": None,
            "pinned_message": MaybeInaccessibleMessage,
            "invoice": Invoice,
            "successful_payment": SuccessfulPayment,
            "users_shared": UsersShared,
            "chat_shared": ChatShared,
            "connected_website": None,
            "write_access_allowed": WriteAccessAllowed,
            "passport_data": PassportData,
            "proximity_alert_triggered": ProximityAlertTriggered,
            "boost_added": ChatBoostAdded,
            "forum_topic_created": ForumTopicCreated,
            "forum_topic_edited": ForumTopicEdited,
            "forum_topic_closed": ForumTopicClosed,
            "forum_topic_reopened": ForumTopicReopened,
            "general_forum_topic_hidden": GeneralForumTopicHidden,
            "general_forum_topic_unhidden": GeneralForumTopicUnhidden,
            "giveaway_created": GiveawayCreated,
            "giveaway": Giveaway,
            "giveaway_winners": GiveawayWinners,
            "giveaway_completed": GiveawayCompleted,
            "video_chat_scheduled": VideoChatScheduled,
            "video_chat_started": VideoChatStarted,
            "video_chat_ended": VideoChatEnded,
            "video_chat_participants_invited": VideoChatParticipantsInvited,
            "web_app_data": WebAppData,
            "reply_markup": InlineKeyboardMarkup
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatPhoto: {
        "link": "https://core.telegram.org/bots/api#chatphoto",
        "has_dese": True,
        "dese_kwargs": {
            "small_file_id": None,
            "small_file_unique_id": None,
            "big_file_id": None,
            "big_file_unique_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Location: {
        "link": "https://core.telegram.org/bots/api#location",
        "has_dese": True,
        "dese_kwargs": {
            "longitude": None,
            "latitude": None,
            "horizontal_accuracy": None,
            "live_period": None,
            "heading": None,
            "proximity_alert_radius": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ReactionTypeEmoji: {
        "link": "https://core.telegram.org/bots/api#reactiontypeemoji",
        "has_dese": True,
        "dese_kwargs": {
            "emoji": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ReactionTypeCustomEmoji: {
        "link": "https://core.telegram.org/bots/api#reactiontypecustomemoji",
        "has_dese": True,
        "dese_kwargs": {
            "custom_emoji_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MessageReactionUpdated: {
        "link": "https://core.telegram.org/bots/api#messagereactionupdated",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "message_id": None,
            "date": None,
            "old_reaction": list[ReactionType],
            "new_reaction": list[ReactionType],
            "user": User,
            "actor_chat": Chat
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ReactionCount: {
        "link": "https://core.telegram.org/bots/api#reactioncount",
        "has_dese": True,
        "dese_kwargs": {
            "type": ReactionType,
            "total_count": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MessageReactionCountUpdated: {
        "link": "https://core.telegram.org/bots/api#messagereactioncountupdated",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "message_id": None,
            "date": None,
            "reactions": list[ReactionCount]
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MessageId: {
        "link": "https://core.telegram.org/bots/api#messageid",
        "has_dese": True,
        "dese_kwargs": {
            "message_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PhotoSize: {
        "link": "https://core.telegram.org/bots/api#photosize",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "width": None,
            "height": None,
            "file_size": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Document: {
        "link": "https://core.telegram.org/bots/api#document",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "thumbnail": PhotoSize,
            "file_name": None,
            "mime_type": None,
            "file_size": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Story: {
        "link": "https://core.telegram.org/bots/api#story",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Video: {
        "link": "https://core.telegram.org/bots/api#video",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "width": None,
            "height": None,
            "duration": None,
            "thumbnail": PhotoSize,
            "file_name": None,
            "mime_type": None,
            "file_size": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    VideoNote: {
        "link": "https://core.telegram.org/bots/api#videonote",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "length": None,
            "duration": None,
            "thumbnail": PhotoSize,
            "file_size": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Voice: {
        "link": "https://core.telegram.org/bots/api#voice",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "duration": None,
            "mime_type": None,
            "file_size": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Contact: {
        "link": "https://core.telegram.org/bots/api#contact",
        "has_dese": True,
        "dese_kwargs": {
            "phone_number": None,
            "first_name": None,
            "last_name": None,
            "user_id": None,
            "vcard": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Dice: {
        "link": "https://core.telegram.org/bots/api#dice",
        "has_dese": True,
        "dese_kwargs": {
            "emoji": None,
            "value": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PollOption: {
        "link": "https://core.telegram.org/bots/api#polloption",
        "has_dese": True,
        "dese_kwargs": {
            "text": None,
            "voter_count": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PollAnswer: {
        "link": "https://core.telegram.org/bots/api#pollanswer",
        "has_dese": True,
        "dese_kwargs": {
            "poll_id": None,
            "option_ids": None,
            "voter_chat": Chat,
            "user": User
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Poll: {
        "link": "https://core.telegram.org/bots/api#poll",
        "has_dese": True,
        "dese_kwargs": {
            "id": None,
            "question": None,
            "options": list[PollOption],
            "total_voter_count": None,
            "is_closed": None,
            "is_anonymous": None,
            "type": None,
            "allows_multiple_answers": None,
            "correct_option_id": None,
            "explanation": None,
            "explanation_entities": Optional[list[MessageEntity]],
            "open_period": None,
            "close_date": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Venue: {
        "link": "https://core.telegram.org/bots/api#venue",
        "has_dese": True,
        "dese_kwargs": {
            "location": Location,
            "title": None,
            "address": None,
            "foursquare_id": None,
            "foursquare_type": None,
            "google_place_id": None,
            "google_place_type": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    WebAppData: {
        "link": "https://core.telegram.org/bots/api#webappdata",
        "has_dese": True,
        "dese_kwargs": {
            "data": None,
            "button_text": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ProximityAlertTriggered: {
        "link": "https://core.telegram.org/bots/api#proximityalerttriggered",
        "has_dese": True,
        "dese_kwargs": {
            "traveler": User,
            "watcher": User,
            "distance": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MessageAutoDeleteTimerChanged: {
        "link": "https://core.telegram.org/bots/api#messageautodeletetimerchanged",
        "has_dese": True,
        "dese_kwargs": {
            "message_auto_delete_time": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ForumTopicCreated: {
        "link": "https://core.telegram.org/bots/api#forumtopiccreated",
        "has_dese": True,
        "dese_kwargs": {
            "name": None,
            "icon_color": None,
            "icon_custom_emoji_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ForumTopicClosed: {
        "link": "https://core.telegram.org/bots/api#forumtopicclosed",
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ForumTopicEdited: {
        "link": "https://core.telegram.org/bots/api#forumtopicedited",
        "has_dese": True,
        "dese_kwargs": {
            "name": None,
            "icon_custom_emoji_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ForumTopicReopened: {
        "link": "https://core.telegram.org/bots/api#forumtopicreopened",
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    GeneralForumTopicHidden: {
        "link": "https://core.telegram.org/bots/api#generalforumtopichidden",
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    GeneralForumTopicUnhidden: {
        "link": "https://core.telegram.org/bots/api#generalforumtopicunhidden",
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    UsersShared: {
        "link": "https://core.telegram.org/bots/api#usersshared",
        "has_dese": True,
        "dese_kwargs": {
            "request_id": None,
            "user_ids": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatShared: {
        "link": "https://core.telegram.org/bots/api#chatshared",
        "has_dese": True,
        "dese_kwargs": {
            "request_id": None,
            "chat_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    WriteAccessAllowed: {
        "link": "https://core.telegram.org/bots/api#writeaccessallowed",
        "has_dese": True,
        "dese_kwargs": {
            "from_request": None,
            "web_app_name": None,
            "from_attachment_menu": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    VideoChatScheduled: {
        "link": "https://core.telegram.org/bots/api#videochatscheduled",
        "has_dese": True,
        "dese_kwargs": {
            "start_date": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    VideoChatStarted: {
        "link": "https://core.telegram.org/bots/api#videochatstarted",
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    VideoChatEnded: {
        "link": "https://core.telegram.org/bots/api#videochatended",
        "has_dese": True,
        "dese_kwargs": {
            "duration": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    VideoChatParticipantsInvited: {
        "link": "https://core.telegram.org/bots/api#videochatparticipantsinvited",
        "has_dese": True,
        "dese_kwargs": {
            "users": list[User]
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    UserProfilePhotos: {
        "link": "https://core.telegram.org/bots/api#userprofilephotos",
        "has_dese": True,
        "dese_kwargs": {
            "total_count": None,
            "photos": list[list[PhotoSize]]
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    File: {
        "link": "https://core.telegram.org/bots/api#file",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "file_size": None,
            "file_path": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    WebAppInfo: {
        "link": "https://core.telegram.org/bots/api#webappinfo",
        "has_dese": True,
        "dese_kwargs": {
            "url": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    KeyboardButtonRequestUsers: {
        "link": "https://core.telegram.org/bots/api#keyboardbuttonrequestusers",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    KeyboardButtonRequestChat: {
        "link": "https://core.telegram.org/bots/api#keyboardbuttonrequestchat",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    KeyboardButtonPollType: {
        "link": "https://core.telegram.org/bots/api#keyboardbuttonpolltype",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    KeyboardButton: {
        "link": "https://core.telegram.org/bots/api#keyboardbutton",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ReplyKeyboardMarkup: {
        "link": "https://core.telegram.org/bots/api#replykeyboardmarkup",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ReplyKeyboardRemove: {
        "link": "https://core.telegram.org/bots/api#replykeyboardremove",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineKeyboardButton: {
        "link": "https://core.telegram.org/bots/api#inlinekeyboardbutton",
        "has_dese": True,
        "dese_kwargs": {
            "text": None,
            "url": None,
            "callback_data": None,
            "web_app": WebAppInfo,
            "login_url": LoginUrl,
            "switch_inline_query": None,
            "switch_inline_query_current_chat": None,
            "switch_inline_query_chosen_chat": SwitchInlineQueryChosenChat,
            "callback_game": CallbackGame,
            "pay": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineKeyboardMarkup: {
        "link": "https://core.telegram.org/bots/api#inlinekeyboardmarkup",
        "has_dese": True,
        "dese_kwargs": {
            "inline_keyboard": list[list[InlineKeyboardButton]]
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ForceReply: {
        "link": "https://core.telegram.org/bots/api#forcereply",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChatMemberUpdated: {
        "link": "https://core.telegram.org/bots/api#chatmemberupdated",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "from_user": User,
            "date": None,
            "old_chat_member": ChatMember,
            "new_chat_member": ChatMember,
            "invite_link": ChatInviteLink,
            "via_chat_folder_invite_link": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ForumTopic: {
        "link": "https://core.telegram.org/bots/api#forumtopic",
        "has_dese": True,
        "dese_kwargs": {
            "message_thread_id": None,
            "name": None,
            "icon_color": None,
            "icon_custom_emoji_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MenuButtonCommands: {
        "link": "https://core.telegram.org/bots/api#menubuttoncommands",
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MenuButtonWebApp: {
        "link": "https://core.telegram.org/bots/api#menubuttonwebapp",
        "has_dese": True,
        "dese_kwargs": {
            "text": None,
            "web_app": WebAppInfo
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MenuButtonDefault: {
        "link": "https://core.telegram.org/bots/api#menubuttondefault",
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ResponseParameters: {
        "link": "https://core.telegram.org/bots/api#responseparameters",
        "has_dese": True,
        "dese_kwargs": {
            "migrate_to_chat_id": None,
            "retry_after": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputMediaPhoto: {
        "link": "https://core.telegram.org/bots/api#inputmediaphoto",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputMediaVideo: {
        "link": "https://core.telegram.org/bots/api#inputmediavideo",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputMediaAnimation: {
        "link": "https://core.telegram.org/bots/api#inputmediaanimation",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputMediaAudio: {
        "link": "https://core.telegram.org/bots/api#inputmediaaudio",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputMediaDocument: {
        "link": "https://core.telegram.org/bots/api#inputmediadocument",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MaskPosition: {
        "link": "https://core.telegram.org/bots/api#maskposition",
        "has_dese": True,
        "dese_kwargs": {
            "point": None,
            "x_shift": None,
            "y_shift": None,
            "scale": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Sticker: {
        "link": "https://core.telegram.org/bots/api#sticker",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "type": None,
            "width": None,
            "height": None,
            "is_animated": None,
            "is_video": None,
            "thumbnail": PhotoSize,
            "emoji": None,
            "set_name": None,
            "premium_animation": File,
            "mask_position": MaskPosition,
            "custom_emoji_id": None,
            "needs_repainting": None,
            "file_size": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    StickerSet: {
        "link": "https://core.telegram.org/bots/api#stickerset",
        "has_dese": True,
        "dese_kwargs": {
            "name": None,
            "title": None,
            "sticker_type": None,
            "is_animated": None,
            "is_video": None,
            "stickers": list[Sticker],
            "thumbnail": PhotoSize
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputSticker: {
        "link": "https://core.telegram.org/bots/api#inputsticker",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQuery: {
        "link": "https://core.telegram.org/bots/api#inlinequery",
        "has_dese": True,
        "dese_kwargs": {
            "id": None,
            "from_user": User,
            "query": None,
            "offset": None,
            "chat_type": None,
            "location": Location
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultsButton: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultsbutton",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputTextMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputtextmessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputLocationMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputlocationmessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputVenueMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputvenuemessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputContactMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputcontactmessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputInvoiceMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputinvoicemessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultArticle: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultarticle",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultPhoto: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultphoto",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultGif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultgif",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultMpeg4Gif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultVideo: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultvideo",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultAudio: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultaudio",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultVoice: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultvoice",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultDocument: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultdocument",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultLocation: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultlocation",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultVenue: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultvenue",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultContact: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcontact",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultGame: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultgame",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultCachedPhoto: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedphoto",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultCachedGif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedgif",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultCachedMpeg4Gif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultCachedSticker: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedsticker",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultCachedDocument: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcacheddocument",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultCachedVideo: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedvideo",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultCachedVoice: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedvoice",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InlineQueryResultCachedAudio: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedaudio",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ChosenInlineResult: {
        "link": "https://core.telegram.org/bots/api#choseninlineresult",
        "has_dese": True,
        "dese_kwargs": {
            "result_id": None,
            "from_user": User,
            "location": Location,
            "inline_message_id": None,
            "query": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    SentWebAppMessage: {
        "link": "https://core.telegram.org/bots/api#sentwebappmessage",
        "has_dese": True,
        "dese_kwargs": {
            "inline_message_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Invoice: {
        "link": "https://core.telegram.org/bots/api#invoice",
        "has_dese": True,
        "dese_kwargs": {
            "title": None,
            "description": None,
            "start_parameter": None,
            "currency": None,
            "total_amount": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ShippingAddress: {
        "link": "https://core.telegram.org/bots/api#shippingaddress",
        "has_dese": True,
        "dese_kwargs": {
            "country_code": None,
            "state": None,
            "city": None,
            "street_line1": None,
            "street_line2": None,
            "post_code": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    OrderInfo: {
        "link": "https://core.telegram.org/bots/api#orderinfo",
        "has_dese": True,
        "dese_kwargs": {
            "name": None,
            "phone_number": None,
            "email": None,
            "shipping_address": ShippingAddress
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ShippingOption: {
        "link": "https://core.telegram.org/bots/api#shippingoption",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    SuccessfulPayment: {
        "link": "https://core.telegram.org/bots/api#successfulpayment",
        "has_dese": True,
        "dese_kwargs": {
            "currency": None,
            "total_amount": None,
            "invoice_payload": None,
            "shipping_option_id": None,
            "order_info": OrderInfo,
            "telegram_payment_charge_id": None,
            "provider_payment_charge_id": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ShippingQuery: {
        "link": "https://core.telegram.org/bots/api#shippingquery",
        "has_dese": True,
        "dese_kwargs": {
            "id": None,
            "from_user": User,
            "invoice_payload": None,
            "shipping_address": ShippingAddress
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PreCheckoutQuery: {
        "link": "https://core.telegram.org/bots/api#precheckoutquery",
        "has_dese": True,
        "dese_kwargs": {
            "id": None,
            "from_user": User,
            "currency": None,
            "total_amount": None,
            "invoice_payload": None,
            "shipping_option_id": None,
            "order_info": OrderInfo
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportFile: {
        "link": "https://core.telegram.org/bots/api#passportfile",
        "has_dese": True,
        "dese_kwargs": {
            "file_id": None,
            "file_unique_id": None,
            "file_size": None,
            "file_date": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    EncryptedPassportElement: {
        "link": "https://core.telegram.org/bots/api#encryptedpassportelement",
        "has_dese": True,
        "dese_kwargs": {
            "type": None,
            "hash": None,
            "data": None,
            "phone_number": None,
            "email": None,
            "files": Optional[list[PassportFile]],
            "front_side": PassportFile,
            "reverse_side": PassportFile,
            "selfie": PassportFile,
            "translation": Optional[list[PassportFile]]
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    EncryptedCredentials: {
        "link": "https://core.telegram.org/bots/api#encryptedcredentials",
        "has_dese": True,
        "dese_kwargs": {
            "data": None,
            "hash": None,
            "secret": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportData: {
        "link": "https://core.telegram.org/bots/api#passportdata",
        "has_dese": True,
        "dese_kwargs": {
            "data": list[EncryptedPassportElement],
            "credentials": EncryptedCredentials
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportElementErrorDataField: {
        "link": "https://core.telegram.org/bots/api#passportelementerrordatafield",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportElementErrorFrontSide: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorfrontside",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportElementErrorReverseSide: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorreverseside",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportElementErrorSelfie: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorselfie",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportElementErrorFile: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorfile",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportElementErrorFiles: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorfiles",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportElementErrorTranslationFile: {
        "link": "https://core.telegram.org/bots/api#passportelementerrortranslationfile",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportElementErrorTranslationFiles: {
        "link": "https://core.telegram.org/bots/api#passportelementerrortranslationfiles",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    PassportElementErrorUnspecified: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorunspecified",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Game: {
        "link": "https://core.telegram.org/bots/api#game",
        "has_dese": True,
        "dese_kwargs": {
            "title": None,
            "description": None,
            "photo": list[PhotoSize],
            "text": None,
            "text_entities": Optional[list[MessageEntity]],
            "animation": Animation
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    GameHighScore: {
        "link": "https://core.telegram.org/bots/api#gamehighscore",
        "has_dese": True,
        "dese_kwargs": {
            "position": None,
            "user": User,
            "score": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    GiveawayCreated: {
        "link": "https://core.telegram.org/bots/api#giveawaycreated",
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    GiveawayWinners: {
        "link": "https://core.telegram.org/bots/api#giveawaywinners",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "giveaway_message_id": None,
            "winners_selection_date": None,
            "winner_count": None,
            "winners": list[User],
            "additional_chat_count": None,
            "premium_subscription_month_count": None,
            "unclaimed_prize_count": None,
            "only_new_members": None,
            "was_refunded": None,
            "prize_description": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    GiveawayCompleted: {
        "link": "https://core.telegram.org/bots/api#giveawaycompleted",
        "has_dese": True,
        "dese_kwargs": {
            "winner_count": None,
            "unclaimed_prize_count": None,
            "giveaway_message": Message
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Giveaway: {
        "link": "https://core.telegram.org/bots/api#giveaway",
        "has_dese": True,
        "dese_kwargs": {
            "chats": list[Chat],
            "winners_selection_date": None,
            "winner_count": None,
            "only_new_members": None,
            "has_public_winners": None,
            "prize_description": None,
            "country_codes": None,
            "premium_subscription_month_count": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MessageOriginUser: {
        "link": "https://core.telegram.org/bots/api#messageoriginuser",
        "has_dese": True,
        "dese_kwargs": {
            "date": None,
            "sender_user": User
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MessageOriginHiddenUser: {
        "link": "https://core.telegram.org/bots/api#messageoriginhiddenuser",
        "has_dese": True,
        "dese_kwargs": {
            "date": None,
            "sender_user_name": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MessageOriginChat: {
        "link": "https://core.telegram.org/bots/api#messageoriginchat",
        "has_dese": True,
        "dese_kwargs": {
            "date": None,
            "sender_chat": Chat,
            "author_signature": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    MessageOriginChannel: {
        "link": "https://core.telegram.org/bots/api#messageoriginchannel",
        "has_dese": True,
        "dese_kwargs": {
            "date": None,
            "chat": Chat,
            "message_id": None,
            "author_signature": None
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ExternalReplyInfo: {
        "link": "https://core.telegram.org/bots/api#externalreplyinfo",
        "has_dese": True,
        "dese_kwargs": {
            "origin": MessageOrigin,
            "chat": Chat,
            "message_id": None,
            "link_preview_options": LinkPreviewOptions,
            "animation": Animation,
            "audio": Audio,
            "document": Document,
            "photo": Optional[list[PhotoSize]],
            "sticker": Sticker,
            "story": Story,
            "video": Video,
            "video_note": VideoNote,
            "voice": Voice,
            "has_media_spoiler": None,
            "contact": Contact,
            "dice": Dice,
            "game": Game,
            "giveaway": Giveaway,
            "giveaway_winners": GiveawayWinners,
            "invoice": Invoice,
            "location": Location,
            "poll": Poll,
            "venue": Venue
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    UserChatBoosts: {
        "link": "https://core.telegram.org/bots/api#userchatboosts",
        "has_dese": True,
        "dese_kwargs": {
            "boosts": list[ChatBoost]
        },
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Update: {
        "link": "https://core.telegram.org/bots/api#update",
        "has_dese": True,
        "dese_kwargs": {
            "update_id": None,
            "message": Message,
            "edited_message": Message,
            "channel_post": Message,
            "edited_channel_post": Message,
            "message_reaction": MessageReactionUpdated,
            "message_reaction_count": MessageReactionCountUpdated,
            "inline_query": InlineQuery,
            "chosen_inline_result": ChosenInlineResult,
            "callback_query": CallbackQuery,
            "shipping_query": ShippingQuery,
            "pre_checkout_query": PreCheckoutQuery,
            "poll": Poll,
            "poll_answer": PollAnswer,
            "my_chat_member": ChatMemberUpdated,
            "chat_member": ChatMemberUpdated,
            "chat_join_request": ChatJoinRequest,
            "chat_boost": ChatBoostUpdated,
            "removed_chat_boost": ChatBoostRemoved
        },
        "init_kwargs": {},
        "self_kwargs": {}
    }
}

warnings = []
logger.info('Program finished.')
