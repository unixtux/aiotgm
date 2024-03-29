#!/bin/env python3

if __name__ != '__main__':
    raise OSError("__name__ is not '__main__'")

from aiotgm._logging import get_logger
logger = get_logger(__name__)

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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "width": {
                "type_hint": int
            },
            "height": {
                "type_hint": int
            },
            "duration": {
                "type_hint": int
            },
            "thumbnail": {
                "type_hint": Optional[PhotoSize],
                "default": None
            },
            "file_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "mime_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            }
        },
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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "duration": {
                "type_hint": int
            },
            "performer": {
                "type_hint": Optional[str],
                "default": None
            },
            "title": {
                "type_hint": Optional[str],
                "default": None
            },
            "file_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "mime_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            },
            "thumbnail": {
                "type_hint": Optional[PhotoSize],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    BotCommand: {
        "link": "https://core.telegram.org/bots/api#botcommand",
        "has_dese": True,
        "dese_kwargs": {
            "command": None,
            "description": None
        },
        "init_kwargs": {
            "command": {
                "type_hint": str
            },
            "description": {
                "type_hint": str
            }
        },
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
        "init_kwargs": {
            "chat_id": {
                "type_hint": Union[int, str]
            }
        },
        "self_kwargs": {}
    },
    BotCommandScopeChatAdministrators: {
        "link": "https://core.telegram.org/bots/api#botcommandscopechatadministrators",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "chat_id": {
                "type_hint": Union[int, str]
            }
        },
        "self_kwargs": {}
    },
    BotCommandScopeChatMember: {
        "link": "https://core.telegram.org/bots/api#botcommandscopechatmember",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "chat_id": {
                "type_hint": Union[int, str]
            },
            "user_id": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "description": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    BotName: {
        "link": "https://core.telegram.org/bots/api#botname",
        "has_dese": True,
        "dese_kwargs": {
            "name": None
        },
        "init_kwargs": {
            "name": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    BotShortDescription: {
        "link": "https://core.telegram.org/bots/api#botshortdescription",
        "has_dese": True,
        "dese_kwargs": {
            "short_description": None
        },
        "init_kwargs": {
            "short_description": {
                "type_hint": str
            }
        },
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
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "from_user": {
                "type_hint": User
            },
            "chat_instance": {
                "type_hint": str
            },
            "message": {
                "type_hint": Optional[MaybeInaccessibleMessage],
                "default": None
            },
            "inline_message_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "data": {
                "type_hint": Optional[str],
                "default": None
            },
            "game_short_name": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "id": {
                "type_hint": int
            },
            "type": {
                "type_hint": str
            },
            "title": {
                "type_hint": Optional[str],
                "default": None
            },
            "username": {
                "type_hint": Optional[str],
                "default": None
            },
            "first_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "last_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "is_forum": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "photo": {
                "type_hint": Optional[ChatPhoto],
                "default": None
            },
            "active_usernames": {
                "type_hint": Optional[list[str]],
                "default": None
            },
            "available_reactions": {
                "type_hint": Optional[list[ReactionType]],
                "default": None
            },
            "accent_color_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "background_custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "profile_accent_color_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "profile_background_custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "emoji_status_custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "emoji_status_expiration_date": {
                "type_hint": Optional[int],
                "default": None
            },
            "bio": {
                "type_hint": Optional[str],
                "default": None
            },
            "has_private_forwards": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "has_restricted_voice_and_video_messages": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "join_to_send_messages": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "join_by_request": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "description": {
                "type_hint": Optional[str],
                "default": None
            },
            "invite_link": {
                "type_hint": Optional[str],
                "default": None
            },
            "pinned_message": {
                "type_hint": Optional[Message],
                "default": None
            },
            "permissions": {
                "type_hint": Optional[ChatPermissions],
                "default": None
            },
            "slow_mode_delay": {
                "type_hint": Optional[int],
                "default": None
            },
            "unrestrict_boost_count": {
                "type_hint": Optional[int],
                "default": None
            },
            "message_auto_delete_time": {
                "type_hint": Optional[int],
                "default": None
            },
            "has_aggressive_anti_spam_enabled": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "has_hidden_members": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "has_protected_content": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "has_visible_history": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "sticker_set_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "can_set_sticker_set": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "custom_emoji_sticker_set_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "linked_chat_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "location": {
                "type_hint": Optional[ChatLocation],
                "default": None
            }
        },
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
        "init_kwargs": {
            "is_anonymous": {
                "type_hint": bool
            },
            "can_manage_chat": {
                "type_hint": bool
            },
            "can_delete_messages": {
                "type_hint": bool
            },
            "can_manage_video_chats": {
                "type_hint": bool
            },
            "can_restrict_members": {
                "type_hint": bool
            },
            "can_promote_members": {
                "type_hint": bool
            },
            "can_change_info": {
                "type_hint": bool
            },
            "can_invite_users": {
                "type_hint": bool
            },
            "can_post_stories": {
                "type_hint": bool
            },
            "can_edit_stories": {
                "type_hint": bool
            },
            "can_delete_stories": {
                "type_hint": bool
            },
            "can_post_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_edit_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_pin_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_manage_topics": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
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
        "init_kwargs": {
            "boost_id": {
                "type_hint": str
            },
            "add_date": {
                "type_hint": int
            },
            "expiration_date": {
                "type_hint": int
            },
            "source": {
                "type_hint": ChatBoostSource
            }
        },
        "self_kwargs": {}
    },
    ChatBoostAdded: {
        "link": "https://core.telegram.org/bots/api#chatboostadded",
        "has_dese": True,
        "dese_kwargs": {
            "boost_count": None
        },
        "init_kwargs": {
            "boost_count": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "boost_id": {
                "type_hint": str
            },
            "remove_date": {
                "type_hint": int
            },
            "source": {
                "type_hint": ChatBoostSource
            }
        },
        "self_kwargs": {}
    },
    ChatBoostSourceGiftCode: {
        "link": "https://core.telegram.org/bots/api#chatboostsourcegiftcode",
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": {
                "type_hint": User
            }
        },
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
        "init_kwargs": {
            "giveaway_message_id": {
                "type_hint": int
            },
            "user": {
                "type_hint": Optional[User],
                "default": None
            },
            "is_unclaimed": {
                "type_hint": Optional[Literal[True]],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ChatBoostSourcePremium: {
        "link": "https://core.telegram.org/bots/api#chatboostsourcepremium",
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "self_kwargs": {}
    },
    ChatBoostUpdated: {
        "link": "https://core.telegram.org/bots/api#chatboostupdated",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "boost": ChatBoost
        },
        "init_kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "boost": {
                "type_hint": ChatBoost
            }
        },
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
        "init_kwargs": {
            "invite_link": {
                "type_hint": str
            },
            "creator": {
                "type_hint": User
            },
            "creates_join_request": {
                "type_hint": bool
            },
            "is_primary": {
                "type_hint": bool
            },
            "is_revoked": {
                "type_hint": bool
            },
            "name": {
                "type_hint": Optional[str],
                "default": None
            },
            "expire_date": {
                "type_hint": Optional[int],
                "default": None
            },
            "member_limit": {
                "type_hint": Optional[int],
                "default": None
            },
            "pending_join_request_count": {
                "type_hint": Optional[int],
                "default": None
            }
        },
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
        "init_kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "from_user": {
                "type_hint": User
            },
            "user_chat_id": {
                "type_hint": int
            },
            "date": {
                "type_hint": int
            },
            "bio": {
                "type_hint": Optional[str],
                "default": None
            },
            "invite_link": {
                "type_hint": Optional[ChatInviteLink],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ChatLocation: {
        "link": "https://core.telegram.org/bots/api#chatlocation",
        "has_dese": True,
        "dese_kwargs": {
            "location": Location,
            "address": None
        },
        "init_kwargs": {
            "location": {
                "type_hint": Location
            },
            "address": {
                "type_hint": str
            }
        },
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
        "init_kwargs": {
            "user": {
                "type_hint": User
            },
            "can_be_edited": {
                "type_hint": bool
            },
            "is_anonymous": {
                "type_hint": bool
            },
            "can_manage_chat": {
                "type_hint": bool
            },
            "can_delete_messages": {
                "type_hint": bool
            },
            "can_manage_video_chats": {
                "type_hint": bool
            },
            "can_restrict_members": {
                "type_hint": bool
            },
            "can_promote_members": {
                "type_hint": bool
            },
            "can_change_info": {
                "type_hint": bool
            },
            "can_invite_users": {
                "type_hint": bool
            },
            "can_post_stories": {
                "type_hint": bool
            },
            "can_edit_stories": {
                "type_hint": bool
            },
            "can_delete_stories": {
                "type_hint": bool
            },
            "can_post_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_edit_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_pin_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_manage_topics": {
                "type_hint": Optional[bool],
                "default": None
            },
            "custom_title": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ChatMemberBanned: {
        "link": "https://core.telegram.org/bots/api#chatmemberbanned",
        "has_dese": True,
        "dese_kwargs": {
            "user": User,
            "until_date": None
        },
        "init_kwargs": {
            "user": {
                "type_hint": User
            },
            "until_date": {
                "type_hint": int
            }
        },
        "self_kwargs": {}
    },
    ChatMemberLeft: {
        "link": "https://core.telegram.org/bots/api#chatmemberleft",
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "self_kwargs": {}
    },
    ChatMemberMember: {
        "link": "https://core.telegram.org/bots/api#chatmembermember",
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": {
                "type_hint": User
            }
        },
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
        "init_kwargs": {
            "user": {
                "type_hint": User
            },
            "is_anonymous": {
                "type_hint": bool
            },
            "custom_title": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "user": {
                "type_hint": User
            },
            "is_member": {
                "type_hint": bool
            },
            "can_send_messages": {
                "type_hint": bool
            },
            "can_send_audios": {
                "type_hint": bool
            },
            "can_send_documents": {
                "type_hint": bool
            },
            "can_send_photos": {
                "type_hint": bool
            },
            "can_send_videos": {
                "type_hint": bool
            },
            "can_send_video_notes": {
                "type_hint": bool
            },
            "can_send_voice_notes": {
                "type_hint": bool
            },
            "can_send_polls": {
                "type_hint": bool
            },
            "can_send_other_messages": {
                "type_hint": bool
            },
            "can_add_web_page_previews": {
                "type_hint": bool
            },
            "can_change_info": {
                "type_hint": bool
            },
            "can_invite_users": {
                "type_hint": bool
            },
            "can_pin_messages": {
                "type_hint": bool
            },
            "can_manage_topics": {
                "type_hint": bool
            },
            "until_date": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "can_send_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_send_audios": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_send_documents": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_send_photos": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_send_videos": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_send_video_notes": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_send_voice_notes": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_send_polls": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_send_other_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_add_web_page_previews": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_change_info": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_invite_users": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_pin_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_manage_topics": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
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
        "init_kwargs": {
            "query": {
                "type_hint": Optional[str],
                "default": None
            },
            "allow_user_chats": {
                "type_hint": Optional[bool],
                "default": None
            },
            "allow_bot_chats": {
                "type_hint": Optional[bool],
                "default": None
            },
            "allow_group_chats": {
                "type_hint": Optional[bool],
                "default": None
            },
            "allow_channel_chats": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputFile: {
        "link": "https://core.telegram.org/bots/api#inputfile",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "path": {
                "type_hint": str
            },
            "file_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "hide_name": {
                "type_hint": bool,
                "default": False
            }
        },
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
        "init_kwargs": {
            "url": {
                "type_hint": str
            },
            "forward_text": {
                "type_hint": Optional[str],
                "default": None
            },
            "bot_username": {
                "type_hint": Optional[str],
                "default": None
            },
            "request_write_access": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    LabeledPrice: {
        "link": "https://core.telegram.org/bots/api#labeledprice",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "label": {
                "type_hint": str
            },
            "amount": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "is_disabled": {
                "type_hint": Optional[bool],
                "default": None
            },
            "url": {
                "type_hint": Optional[str],
                "default": None
            },
            "prefer_small_media": {
                "type_hint": Optional[bool],
                "default": None
            },
            "prefer_large_media": {
                "type_hint": Optional[bool],
                "default": None
            },
            "show_above_text": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
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
        "init_kwargs": {
            "id": {
                "type_hint": int
            },
            "is_bot": {
                "type_hint": bool
            },
            "first_name": {
                "type_hint": str
            },
            "last_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "username": {
                "type_hint": Optional[str],
                "default": None
            },
            "language_code": {
                "type_hint": Optional[str],
                "default": None
            },
            "is_premium": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "added_to_attachment_menu": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "can_join_groups": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_read_all_group_messages": {
                "type_hint": Optional[bool],
                "default": None
            },
            "supports_inline_queries": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
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
        "init_kwargs": {
            "type": {
                "type_hint": str
            },
            "offset": {
                "type_hint": int
            },
            "length": {
                "type_hint": int
            },
            "url": {
                "type_hint": Optional[str],
                "default": None
            },
            "user": {
                "type_hint": Optional[User],
                "default": None
            },
            "language": {
                "type_hint": Optional[str],
                "default": None
            },
            "custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "text": {
                "type_hint": str
            },
            "position": {
                "type_hint": int
            },
            "entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "is_manual": {
                "type_hint": Optional[Literal[True]],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ReplyParameters: {
        "link": "https://core.telegram.org/bots/api#replyparameters",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "message_id": {
                "type_hint": int
            },
            "chat_id": {
                "type_hint": Optional[Union[int, str]],
                "default": None
            },
            "allow_sending_without_reply": {
                "type_hint": Optional[bool],
                "default": None
            },
            "quote": {
                "type_hint": Optional[str],
                "default": None
            },
            "quote_parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "quote_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "quote_position": {
                "type_hint": Optional[int],
                "default": None
            }
        },
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
        "init_kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "message_id": {
                "type_hint": int
            },
            "date": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "message_id": {
                "type_hint": int
            },
            "date": {
                "type_hint": int
            },
            "chat": {
                "type_hint": Chat
            },
            "message_thread_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "from_user": {
                "type_hint": Optional[User],
                "default": None
            },
            "sender_chat": {
                "type_hint": Optional[Chat],
                "default": None
            },
            "sender_boost_count": {
                "type_hint": Optional[int],
                "default": None
            },
            "forward_origin": {
                "type_hint": Optional[MessageOrigin],
                "default": None
            },
            "is_topic_message": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "is_automatic_forward": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "reply_to_message": {
                "type_hint": Optional[Message],
                "default": None
            },
            "external_reply": {
                "type_hint": Optional[ExternalReplyInfo],
                "default": None
            },
            "quote": {
                "type_hint": Optional[TextQuote],
                "default": None
            },
            "reply_to_story": {
                "type_hint": Optional[Story],
                "default": None
            },
            "via_bot": {
                "type_hint": Optional[User],
                "default": None
            },
            "edit_date": {
                "type_hint": Optional[int],
                "default": None
            },
            "has_protected_content": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "media_group_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "author_signature": {
                "type_hint": Optional[str],
                "default": None
            },
            "text": {
                "type_hint": str,
                "default": None
            },
            "entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "link_preview_options": {
                "type_hint": Optional[LinkPreviewOptions],
                "default": None
            },
            "animation": {
                "type_hint": Optional[Animation],
                "default": None
            },
            "audio": {
                "type_hint": Optional[Audio],
                "default": None
            },
            "document": {
                "type_hint": Optional[Document],
                "default": None
            },
            "photo": {
                "type_hint": Optional[list[PhotoSize]],
                "default": None
            },
            "sticker": {
                "type_hint": Optional[Sticker],
                "default": None
            },
            "story": {
                "type_hint": Optional[Story],
                "default": None
            },
            "video": {
                "type_hint": Optional[Video],
                "default": None
            },
            "video_note": {
                "type_hint": Optional[VideoNote],
                "default": None
            },
            "voice": {
                "type_hint": Optional[Voice],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "has_media_spoiler": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "contact": {
                "type_hint": Optional[Contact],
                "default": None
            },
            "dice": {
                "type_hint": Optional[Dice],
                "default": None
            },
            "game": {
                "type_hint": Optional[Game],
                "default": None
            },
            "poll": {
                "type_hint": Optional[Poll],
                "default": None
            },
            "venue": {
                "type_hint": Optional[Venue],
                "default": None
            },
            "location": {
                "type_hint": Optional[Location],
                "default": None
            },
            "new_chat_members": {
                "type_hint": Optional[list[User]],
                "default": None
            },
            "left_chat_member": {
                "type_hint": Optional[User],
                "default": None
            },
            "new_chat_title": {
                "type_hint": Optional[str],
                "default": None
            },
            "new_chat_photo": {
                "type_hint": Optional[list[PhotoSize]],
                "default": None
            },
            "delete_chat_photo": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "group_chat_created": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "supergroup_chat_created": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "channel_chat_created": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "message_auto_delete_timer_changed": {
                "type_hint": Optional[MessageAutoDeleteTimerChanged],
                "default": None
            },
            "migrate_to_chat_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "migrate_from_chat_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "pinned_message": {
                "type_hint": Optional[MaybeInaccessibleMessage],
                "default": None
            },
            "invoice": {
                "type_hint": Optional[Invoice],
                "default": None
            },
            "successful_payment": {
                "type_hint": Optional[SuccessfulPayment],
                "default": None
            },
            "users_shared": {
                "type_hint": Optional[UsersShared],
                "default": None
            },
            "chat_shared": {
                "type_hint": Optional[ChatShared],
                "default": None
            },
            "connected_website": {
                "type_hint": Optional[str],
                "default": None
            },
            "write_access_allowed": {
                "type_hint": Optional[WriteAccessAllowed],
                "default": None
            },
            "passport_data": {
                "type_hint": Optional[PassportData],
                "default": None
            },
            "proximity_alert_triggered": {
                "type_hint": Optional[ProximityAlertTriggered],
                "default": None
            },
            "boost_added": {
                "type_hint": Optional[ChatBoostAdded],
                "default": None
            },
            "forum_topic_created": {
                "type_hint": Optional[ForumTopicCreated],
                "default": None
            },
            "forum_topic_edited": {
                "type_hint": Optional[ForumTopicEdited],
                "default": None
            },
            "forum_topic_closed": {
                "type_hint": Optional[ForumTopicClosed],
                "default": None
            },
            "forum_topic_reopened": {
                "type_hint": Optional[ForumTopicReopened],
                "default": None
            },
            "general_forum_topic_hidden": {
                "type_hint": Optional[GeneralForumTopicHidden],
                "default": None
            },
            "general_forum_topic_unhidden": {
                "type_hint": Optional[GeneralForumTopicUnhidden],
                "default": None
            },
            "giveaway_created": {
                "type_hint": Optional[GiveawayCreated],
                "default": None
            },
            "giveaway": {
                "type_hint": Optional[Giveaway],
                "default": None
            },
            "giveaway_winners": {
                "type_hint": Optional[GiveawayWinners],
                "default": None
            },
            "giveaway_completed": {
                "type_hint": Optional[GiveawayCompleted],
                "default": None
            },
            "video_chat_scheduled": {
                "type_hint": Optional[VideoChatScheduled],
                "default": None
            },
            "video_chat_started": {
                "type_hint": Optional[VideoChatStarted],
                "default": None
            },
            "video_chat_ended": {
                "type_hint": Optional[VideoChatEnded],
                "default": None
            },
            "video_chat_participants_invited": {
                "type_hint": Optional[VideoChatParticipantsInvited],
                "default": None
            },
            "web_app_data": {
                "type_hint": Optional[WebAppData],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            }
        },
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
        "init_kwargs": {
            "small_file_id": {
                "type_hint": str
            },
            "small_file_unique_id": {
                "type_hint": str
            },
            "big_file_id": {
                "type_hint": str
            },
            "big_file_unique_id": {
                "type_hint": str
            }
        },
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
        "init_kwargs": {
            "longitude": {
                "type_hint": float
            },
            "latitude": {
                "type_hint": float
            },
            "horizontal_accuracy": {
                "type_hint": Optional[float],
                "default": None
            },
            "live_period": {
                "type_hint": Optional[int],
                "default": None
            },
            "heading": {
                "type_hint": Optional[int],
                "default": None
            },
            "proximity_alert_radius": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ReactionTypeEmoji: {
        "link": "https://core.telegram.org/bots/api#reactiontypeemoji",
        "has_dese": True,
        "dese_kwargs": {
            "emoji": None
        },
        "init_kwargs": {
            "emoji": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    ReactionTypeCustomEmoji: {
        "link": "https://core.telegram.org/bots/api#reactiontypecustomemoji",
        "has_dese": True,
        "dese_kwargs": {
            "custom_emoji_id": None
        },
        "init_kwargs": {
            "custom_emoji_id": {
                "type_hint": str
            }
        },
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
        "init_kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "message_id": {
                "type_hint": int
            },
            "date": {
                "type_hint": int
            },
            "old_reaction": {
                "type_hint": list[ReactionType]
            },
            "new_reaction": {
                "type_hint": list[ReactionType]
            },
            "user": {
                "type_hint": Optional[User],
                "default": None
            },
            "actor_chat": {
                "type_hint": Optional[Chat],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ReactionCount: {
        "link": "https://core.telegram.org/bots/api#reactioncount",
        "has_dese": True,
        "dese_kwargs": {
            "type": ReactionType,
            "total_count": None
        },
        "init_kwargs": {
            "type": {
                "type_hint": ReactionType
            },
            "total_count": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "message_id": {
                "type_hint": int
            },
            "date": {
                "type_hint": int
            },
            "reactions": {
                "type_hint": list[ReactionCount]
            }
        },
        "self_kwargs": {}
    },
    MessageId: {
        "link": "https://core.telegram.org/bots/api#messageid",
        "has_dese": True,
        "dese_kwargs": {
            "message_id": None
        },
        "init_kwargs": {
            "message_id": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "width": {
                "type_hint": int
            },
            "height": {
                "type_hint": int
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            }
        },
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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "thumbnail": {
                "type_hint": Optional[PhotoSize],
                "default": None
            },
            "file_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "mime_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    Story: {
        "link": "https://core.telegram.org/bots/api#story",
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "id": None
        },
        "init_kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "id": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "width": {
                "type_hint": int
            },
            "height": {
                "type_hint": int
            },
            "duration": {
                "type_hint": int
            },
            "thumbnail": {
                "type_hint": Optional[PhotoSize],
                "default": None
            },
            "file_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "mime_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            }
        },
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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "length": {
                "type_hint": int
            },
            "duration": {
                "type_hint": int
            },
            "thumbnail": {
                "type_hint": Optional[PhotoSize],
                "default": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            }
        },
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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "duration": {
                "type_hint": int
            },
            "mime_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            }
        },
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
        "init_kwargs": {
            "phone_number": {
                "type_hint": str
            },
            "first_name": {
                "type_hint": str
            },
            "last_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "user_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "vcard": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    Dice: {
        "link": "https://core.telegram.org/bots/api#dice",
        "has_dese": True,
        "dese_kwargs": {
            "emoji": None,
            "value": None
        },
        "init_kwargs": {
            "emoji": {
                "type_hint": str
            },
            "value": {
                "type_hint": int
            }
        },
        "self_kwargs": {}
    },
    PollOption: {
        "link": "https://core.telegram.org/bots/api#polloption",
        "has_dese": True,
        "dese_kwargs": {
            "text": None,
            "voter_count": None
        },
        "init_kwargs": {
            "text": {
                "type_hint": str
            },
            "voter_count": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "poll_id": {
                "type_hint": str
            },
            "option_ids": {
                "type_hint": list[int]
            },
            "voter_chat": {
                "type_hint": Optional[Chat],
                "default": None
            },
            "user": {
                "type_hint": Optional[User],
                "default": None
            }
        },
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
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "question": {
                "type_hint": str
            },
            "options": {
                "type_hint": list[PollOption]
            },
            "total_voter_count": {
                "type_hint": int
            },
            "is_closed": {
                "type_hint": bool
            },
            "is_anonymous": {
                "type_hint": bool
            },
            "type": {
                "type_hint": str
            },
            "allows_multiple_answers": {
                "type_hint": bool
            },
            "correct_option_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "explanation": {
                "type_hint": Optional[str],
                "default": None
            },
            "explanation_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "open_period": {
                "type_hint": Optional[int],
                "default": None
            },
            "close_date": {
                "type_hint": Optional[int],
                "default": None
            }
        },
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
        "init_kwargs": {
            "location": {
                "type_hint": Location
            },
            "title": {
                "type_hint": str
            },
            "address": {
                "type_hint": str
            },
            "foursquare_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "foursquare_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "google_place_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "google_place_type": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    WebAppData: {
        "link": "https://core.telegram.org/bots/api#webappdata",
        "has_dese": True,
        "dese_kwargs": {
            "data": None,
            "button_text": None
        },
        "init_kwargs": {
            "data": {
                "type_hint": str
            },
            "button_text": {
                "type_hint": str
            }
        },
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
        "init_kwargs": {
            "traveler": {
                "type_hint": User
            },
            "watcher": {
                "type_hint": User
            },
            "distance": {
                "type_hint": int
            }
        },
        "self_kwargs": {}
    },
    MessageAutoDeleteTimerChanged: {
        "link": "https://core.telegram.org/bots/api#messageautodeletetimerchanged",
        "has_dese": True,
        "dese_kwargs": {
            "message_auto_delete_time": None
        },
        "init_kwargs": {
            "message_auto_delete_time": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "name": {
                "type_hint": str
            },
            "icon_color": {
                "type_hint": int
            },
            "icon_custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "name": {
                "type_hint": Optional[str],
                "default": None
            },
            "icon_custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "request_id": {
                "type_hint": int
            },
            "user_ids": {
                "type_hint": list[int]
            }
        },
        "self_kwargs": {}
    },
    ChatShared: {
        "link": "https://core.telegram.org/bots/api#chatshared",
        "has_dese": True,
        "dese_kwargs": {
            "request_id": None,
            "chat_id": None
        },
        "init_kwargs": {
            "request_id": {
                "type_hint": int
            },
            "chat_id": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "from_request": {
                "type_hint": Optional[bool],
                "default": None
            },
            "web_app_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "from_attachment_menu": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    VideoChatScheduled: {
        "link": "https://core.telegram.org/bots/api#videochatscheduled",
        "has_dese": True,
        "dese_kwargs": {
            "start_date": None
        },
        "init_kwargs": {
            "start_date": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "duration": {
                "type_hint": int
            }
        },
        "self_kwargs": {}
    },
    VideoChatParticipantsInvited: {
        "link": "https://core.telegram.org/bots/api#videochatparticipantsinvited",
        "has_dese": True,
        "dese_kwargs": {
            "users": list[User]
        },
        "init_kwargs": {
            "users": {
                "type_hint": list[User]
            }
        },
        "self_kwargs": {}
    },
    UserProfilePhotos: {
        "link": "https://core.telegram.org/bots/api#userprofilephotos",
        "has_dese": True,
        "dese_kwargs": {
            "total_count": None,
            "photos": list[list[PhotoSize]]
        },
        "init_kwargs": {
            "total_count": {
                "type_hint": int
            },
            "photos": {
                "type_hint": list[list[PhotoSize]]
            }
        },
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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            },
            "file_path": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    WebAppInfo: {
        "link": "https://core.telegram.org/bots/api#webappinfo",
        "has_dese": True,
        "dese_kwargs": {
            "url": None
        },
        "init_kwargs": {
            "url": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    KeyboardButtonRequestUsers: {
        "link": "https://core.telegram.org/bots/api#keyboardbuttonrequestusers",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "request_id": {
                "type_hint": int
            },
            "user_is_bot": {
                "type_hint": Optional[bool],
                "default": None
            },
            "user_is_premium": {
                "type_hint": Optional[bool],
                "default": None
            },
            "max_quantity": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    KeyboardButtonRequestChat: {
        "link": "https://core.telegram.org/bots/api#keyboardbuttonrequestchat",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "request_id": {
                "type_hint": int
            },
            "chat_is_channel": {
                "type_hint": bool
            },
            "chat_is_forum": {
                "type_hint": Optional[bool],
                "default": None
            },
            "chat_has_username": {
                "type_hint": Optional[bool],
                "default": None
            },
            "chat_is_created": {
                "type_hint": Optional[bool],
                "default": None
            },
            "user_administrator_rights": {
                "type_hint": Optional[ChatAdministratorRights],
                "default": None
            },
            "bot_administrator_rights": {
                "type_hint": Optional[ChatAdministratorRights],
                "default": None
            },
            "bot_is_member": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    KeyboardButtonPollType: {
        "link": "https://core.telegram.org/bots/api#keyboardbuttonpolltype",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    KeyboardButton: {
        "link": "https://core.telegram.org/bots/api#keyboardbutton",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "text": {
                "type_hint": str
            },
            "request_users": {
                "type_hint": Optional[KeyboardButtonRequestUsers],
                "default": None
            },
            "request_chat": {
                "type_hint": Optional[KeyboardButtonRequestChat],
                "default": None
            },
            "request_contact": {
                "type_hint": Optional[bool],
                "default": None
            },
            "request_location": {
                "type_hint": Optional[bool],
                "default": None
            },
            "request_poll": {
                "type_hint": Optional[KeyboardButtonPollType],
                "default": None
            },
            "web_app": {
                "type_hint": Optional[WebAppInfo],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ReplyKeyboardMarkup: {
        "link": "https://core.telegram.org/bots/api#replykeyboardmarkup",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "keyboard": {
                "type_hint": Optional[list[list[KeyboardButton]]],
                "default": None
            },
            "is_persistent": {
                "type_hint": Optional[bool],
                "default": None
            },
            "resize_keyboard": {
                "type_hint": Optional[bool],
                "default": None
            },
            "one_time_keyboard": {
                "type_hint": Optional[bool],
                "default": None
            },
            "input_field_placeholder": {
                "type_hint": Optional[str],
                "default": None
            },
            "selective": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ReplyKeyboardRemove: {
        "link": "https://core.telegram.org/bots/api#replykeyboardremove",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "selective": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
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
        "init_kwargs": {
            "text": {
                "type_hint": str
            },
            "url": {
                "type_hint": Optional[str],
                "default": None
            },
            "callback_data": {
                "type_hint": Optional[str],
                "default": None
            },
            "web_app": {
                "type_hint": Optional[WebAppInfo],
                "default": None
            },
            "login_url": {
                "type_hint": Optional[LoginUrl],
                "default": None
            },
            "switch_inline_query": {
                "type_hint": Optional[str],
                "default": None
            },
            "switch_inline_query_current_chat": {
                "type_hint": Optional[str],
                "default": None
            },
            "switch_inline_query_chosen_chat": {
                "type_hint": Optional[SwitchInlineQueryChosenChat],
                "default": None
            },
            "callback_game": {
                "type_hint": Optional[CallbackGame],
                "default": None
            },
            "pay": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineKeyboardMarkup: {
        "link": "https://core.telegram.org/bots/api#inlinekeyboardmarkup",
        "has_dese": True,
        "dese_kwargs": {
            "inline_keyboard": list[list[InlineKeyboardButton]]
        },
        "init_kwargs": {
            "inline_keyboard": {
                "type_hint": Optional[list[list[InlineKeyboardButton]]],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ForceReply: {
        "link": "https://core.telegram.org/bots/api#forcereply",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "force_reply": {
                "type_hint": Literal[True],
                "default": True
            },
            "input_field_placeholder": {
                "type_hint": Optional[str],
                "default": None
            },
            "selective": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
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
        "init_kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "from_user": {
                "type_hint": User
            },
            "date": {
                "type_hint": int
            },
            "old_chat_member": {
                "type_hint": ChatMember
            },
            "new_chat_member": {
                "type_hint": ChatMember
            },
            "invite_link": {
                "type_hint": Optional[ChatInviteLink],
                "default": None
            },
            "via_chat_folder_invite_link": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
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
        "init_kwargs": {
            "message_thread_id": {
                "type_hint": int
            },
            "name": {
                "type_hint": str
            },
            "icon_color": {
                "type_hint": int
            },
            "icon_custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "text": {
                "type_hint": str
            },
            "web_app": {
                "type_hint": WebAppInfo
            }
        },
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
        "init_kwargs": {
            "migrate_to_chat_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "retry_after": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputMediaPhoto: {
        "link": "https://core.telegram.org/bots/api#inputmediaphoto",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "has_spoiler": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputMediaVideo: {
        "link": "https://core.telegram.org/bots/api#inputmediavideo",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "thumbnail": {
                "type_hint": Optional[Union[InputFile, str]],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "width": {
                "type_hint": Optional[int],
                "default": None
            },
            "height": {
                "type_hint": Optional[int],
                "default": None
            },
            "duration": {
                "type_hint": Optional[int],
                "default": None
            },
            "supports_streaming": {
                "type_hint": Optional[bool],
                "default": None
            },
            "has_spoiler": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputMediaAnimation: {
        "link": "https://core.telegram.org/bots/api#inputmediaanimation",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "thumbnail": {
                "type_hint": Optional[Union[InputFile, str]],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "width": {
                "type_hint": Optional[int],
                "default": None
            },
            "height": {
                "type_hint": Optional[int],
                "default": None
            },
            "duration": {
                "type_hint": Optional[int],
                "default": None
            },
            "has_spoiler": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputMediaAudio: {
        "link": "https://core.telegram.org/bots/api#inputmediaaudio",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "thumbnail": {
                "type_hint": Optional[Union[InputFile, str]],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "duration": {
                "type_hint": Optional[int],
                "default": None
            },
            "performer": {
                "type_hint": Optional[str],
                "default": None
            },
            "title": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputMediaDocument: {
        "link": "https://core.telegram.org/bots/api#inputmediadocument",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "thumbnail": {
                "type_hint": Optional[Union[InputFile, str]],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "disable_content_type_detection": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
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
        "init_kwargs": {
            "point": {
                "type_hint": str
            },
            "x_shift": {
                "type_hint": float
            },
            "y_shift": {
                "type_hint": float
            },
            "scale": {
                "type_hint": float
            }
        },
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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "type": {
                "type_hint": str
            },
            "width": {
                "type_hint": int
            },
            "height": {
                "type_hint": int
            },
            "is_animated": {
                "type_hint": bool
            },
            "is_video": {
                "type_hint": bool
            },
            "thumbnail": {
                "type_hint": Optional[PhotoSize],
                "default": None
            },
            "emoji": {
                "type_hint": Optional[str],
                "default": None
            },
            "set_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "premium_animation": {
                "type_hint": Optional[File],
                "default": None
            },
            "mask_position": {
                "type_hint": Optional[MaskPosition],
                "default": None
            },
            "custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "needs_repainting": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            }
        },
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
        "init_kwargs": {
            "name": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "sticker_type": {
                "type_hint": str
            },
            "is_animated": {
                "type_hint": bool
            },
            "is_video": {
                "type_hint": bool
            },
            "stickers": {
                "type_hint": list[Sticker]
            },
            "thumbnail": {
                "type_hint": Optional[PhotoSize],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputSticker: {
        "link": "https://core.telegram.org/bots/api#inputsticker",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "sticker": {
                "type_hint": Union[InputFile, str]
            },
            "emoji_list": {
                "type_hint": list[str]
            },
            "mask_position": {
                "type_hint": Optional[MaskPosition],
                "default": None
            },
            "keywords": {
                "type_hint": Optional[list[str]],
                "default": None
            }
        },
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
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "from_user": {
                "type_hint": User
            },
            "query": {
                "type_hint": str
            },
            "offset": {
                "type_hint": str
            },
            "chat_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "location": {
                "type_hint": Optional[Location],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultsButton: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultsbutton",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "text": {
                "type_hint": str
            },
            "web_app": {
                "type_hint": Optional[WebAppInfo],
                "default": None
            },
            "start_parameter": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputTextMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputtextmessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "message_text": {
                "type_hint": str
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "link_preview_options": {
                "type_hint": Optional[LinkPreviewOptions],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputLocationMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputlocationmessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "latitude": {
                "type_hint": float
            },
            "longitude": {
                "type_hint": float
            },
            "horizontal_accuracy": {
                "type_hint": Optional[float],
                "default": None
            },
            "live_period": {
                "type_hint": Optional[int],
                "default": None
            },
            "heading": {
                "type_hint": Optional[int],
                "default": None
            },
            "proximity_alert_radius": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputVenueMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputvenuemessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "latitude": {
                "type_hint": float
            },
            "longitude": {
                "type_hint": float
            },
            "title": {
                "type_hint": str
            },
            "address": {
                "type_hint": str
            },
            "foursquare_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "foursquare_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "google_place_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "google_place_type": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputContactMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputcontactmessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "phone_number": {
                "type_hint": str
            },
            "first_name": {
                "type_hint": str
            },
            "last_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "vcard": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InputInvoiceMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputinvoicemessagecontent",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "title": {
                "type_hint": str
            },
            "description": {
                "type_hint": str
            },
            "payload": {
                "type_hint": str
            },
            "provider_token": {
                "type_hint": str
            },
            "currency": {
                "type_hint": str
            },
            "prices": {
                "type_hint": list[LabeledPrice]
            },
            "max_tip_amount": {
                "type_hint": Optional[int],
                "default": None
            },
            "suggested_tip_amounts": {
                "type_hint": Optional[list[int]],
                "default": None
            },
            "provider_data": {
                "type_hint": Optional[str],
                "default": None
            },
            "photo_url": {
                "type_hint": Optional[str],
                "default": None
            },
            "photo_size": {
                "type_hint": Optional[int],
                "default": None
            },
            "photo_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "photo_height": {
                "type_hint": Optional[int],
                "default": None
            },
            "need_name": {
                "type_hint": Optional[bool],
                "default": None
            },
            "need_phone_number": {
                "type_hint": Optional[bool],
                "default": None
            },
            "need_email": {
                "type_hint": Optional[bool],
                "default": None
            },
            "need_shipping_address": {
                "type_hint": Optional[bool],
                "default": None
            },
            "send_phone_number_to_provider": {
                "type_hint": Optional[bool],
                "default": None
            },
            "send_email_to_provider": {
                "type_hint": Optional[bool],
                "default": None
            },
            "is_flexible": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultArticle: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultarticle",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "input_message_content": {
                "type_hint": InputMessageContent
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "url": {
                "type_hint": Optional[str],
                "default": None
            },
            "hide_url": {
                "type_hint": Optional[bool],
                "default": None
            },
            "description": {
                "type_hint": Optional[str],
                "default": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultPhoto: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultphoto",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "photo_url": {
                "type_hint": str
            },
            "thumbnail_url": {
                "type_hint": str
            },
            "photo_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "photo_height": {
                "type_hint": Optional[int],
                "default": None
            },
            "title": {
                "type_hint": Optional[str],
                "default": None
            },
            "description": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultGif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultgif",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "gif_url": {
                "type_hint": str
            },
            "thumbnail_url": {
                "type_hint": str
            },
            "gif_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "gif_height": {
                "type_hint": Optional[int],
                "default": None
            },
            "gif_duration": {
                "type_hint": Optional[int],
                "default": None
            },
            "thumbnail_mime_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "title": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultMpeg4Gif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "mpeg4_url": {
                "type_hint": str
            },
            "thumbnail_url": {
                "type_hint": str
            },
            "mpeg4_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "mpeg4_height": {
                "type_hint": Optional[int],
                "default": None
            },
            "mpeg4_duration": {
                "type_hint": Optional[int],
                "default": None
            },
            "thumbnail_mime_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "title": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultVideo: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultvideo",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "video_url": {
                "type_hint": str
            },
            "mime_type": {
                "type_hint": str
            },
            "thumbnail_url": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "video_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "video_height": {
                "type_hint": Optional[int],
                "default": None
            },
            "video_duration": {
                "type_hint": Optional[int],
                "default": None
            },
            "description": {
                "type_hint": Optional[str],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultAudio: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultaudio",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "audio_url": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "performer": {
                "type_hint": Optional[str],
                "default": None
            },
            "audio_duration": {
                "type_hint": Optional[int],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultVoice: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultvoice",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "voice_url": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "voice_duration": {
                "type_hint": Optional[int],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultDocument: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultdocument",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "document_url": {
                "type_hint": str
            },
            "mime_type": {
                "type_hint": str
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "description": {
                "type_hint": Optional[str],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultLocation: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultlocation",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "latitude": {
                "type_hint": float
            },
            "longitude": {
                "type_hint": float
            },
            "title": {
                "type_hint": str
            },
            "horizontal_accuracy": {
                "type_hint": Optional[float],
                "default": None
            },
            "live_period": {
                "type_hint": Optional[int],
                "default": None
            },
            "heading": {
                "type_hint": Optional[int],
                "default": None
            },
            "proximity_alert_radius": {
                "type_hint": Optional[int],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultVenue: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultvenue",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "latitude": {
                "type_hint": float
            },
            "longitude": {
                "type_hint": float
            },
            "title": {
                "type_hint": str
            },
            "address": {
                "type_hint": str
            },
            "foursquare_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "foursquare_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "google_place_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "google_place_type": {
                "type_hint": Optional[str],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultContact: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcontact",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "phone_number": {
                "type_hint": str
            },
            "first_name": {
                "type_hint": str
            },
            "last_name": {
                "type_hint": Optional[str],
                "default": None
            },
            "vcard": {
                "type_hint": Optional[str],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultGame: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultgame",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "game_short_name": {
                "type_hint": str
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultCachedPhoto: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedphoto",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "photo_file_id": {
                "type_hint": str
            },
            "title": {
                "type_hint": Optional[str],
                "default": None
            },
            "description": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultCachedGif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedgif",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "gif_file_id": {
                "type_hint": str
            },
            "title": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultCachedMpeg4Gif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "mpeg4_file_id": {
                "type_hint": str
            },
            "title": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultCachedSticker: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedsticker",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "sticker_file_id": {
                "type_hint": str
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultCachedDocument: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcacheddocument",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "document_file_id": {
                "type_hint": str
            },
            "description": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultCachedVideo: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedvideo",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "video_file_id": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "description": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultCachedVoice: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedvoice",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "voice_file_id": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    InlineQueryResultCachedAudio: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedaudio",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "audio_file_id": {
                "type_hint": str
            },
            "caption": {
                "type_hint": Optional[str],
                "default": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
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
        "init_kwargs": {
            "result_id": {
                "type_hint": str
            },
            "from_user": {
                "type_hint": User
            },
            "query": {
                "type_hint": str
            },
            "location": {
                "type_hint": Optional[Location],
                "default": None
            },
            "inline_message_id": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    SentWebAppMessage: {
        "link": "https://core.telegram.org/bots/api#sentwebappmessage",
        "has_dese": True,
        "dese_kwargs": {
            "inline_message_id": None
        },
        "init_kwargs": {
            "inline_message_id": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "title": {
                "type_hint": str
            },
            "description": {
                "type_hint": str
            },
            "start_parameter": {
                "type_hint": str
            },
            "currency": {
                "type_hint": str
            },
            "total_amount": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "country_code": {
                "type_hint": str
            },
            "state": {
                "type_hint": str
            },
            "city": {
                "type_hint": str
            },
            "street_line1": {
                "type_hint": str
            },
            "street_line2": {
                "type_hint": str
            },
            "post_code": {
                "type_hint": str
            }
        },
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
        "init_kwargs": {
            "name": {
                "type_hint": Optional[str],
                "default": None
            },
            "phone_number": {
                "type_hint": Optional[str],
                "default": None
            },
            "email": {
                "type_hint": Optional[str],
                "default": None
            },
            "shipping_address": {
                "type_hint": Optional[ShippingAddress],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    ShippingOption: {
        "link": "https://core.telegram.org/bots/api#shippingoption",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "prices": {
                "type_hint": list[LabeledPrice]
            }
        },
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
        "init_kwargs": {
            "currency": {
                "type_hint": str
            },
            "total_amount": {
                "type_hint": int
            },
            "invoice_payload": {
                "type_hint": str
            },
            "telegram_payment_charge_id": {
                "type_hint": str
            },
            "provider_payment_charge_id": {
                "type_hint": str
            },
            "shipping_option_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "order_info": {
                "type_hint": Optional[OrderInfo],
                "default": None
            }
        },
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
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "from_user": {
                "type_hint": User
            },
            "invoice_payload": {
                "type_hint": str
            },
            "shipping_address": {
                "type_hint": ShippingAddress
            }
        },
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
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "from_user": {
                "type_hint": User
            },
            "currency": {
                "type_hint": str
            },
            "total_amount": {
                "type_hint": int
            },
            "invoice_payload": {
                "type_hint": str
            },
            "shipping_option_id": {
                "type_hint": Optional[str],
                "default": None
            },
            "order_info": {
                "type_hint": Optional[OrderInfo],
                "default": None
            }
        },
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
        "init_kwargs": {
            "file_id": {
                "type_hint": str
            },
            "file_unique_id": {
                "type_hint": str
            },
            "file_size": {
                "type_hint": int
            },
            "file_date": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "type": {
                "type_hint": str
            },
            "hash": {
                "type_hint": str
            },
            "data": {
                "type_hint": Optional[str],
                "default": None
            },
            "phone_number": {
                "type_hint": Optional[str],
                "default": None
            },
            "email": {
                "type_hint": Optional[str],
                "default": None
            },
            "files": {
                "type_hint": Optional[list[PassportFile]],
                "default": None
            },
            "front_side": {
                "type_hint": Optional[PassportFile],
                "default": None
            },
            "reverse_side": {
                "type_hint": Optional[PassportFile],
                "default": None
            },
            "selfie": {
                "type_hint": Optional[PassportFile],
                "default": None
            },
            "translation": {
                "type_hint": Optional[list[PassportFile]],
                "default": None
            }
        },
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
        "init_kwargs": {
            "data": {
                "type_hint": str
            },
            "hash": {
                "type_hint": str
            },
            "secret": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    PassportData: {
        "link": "https://core.telegram.org/bots/api#passportdata",
        "has_dese": True,
        "dese_kwargs": {
            "data": list[EncryptedPassportElement],
            "credentials": EncryptedCredentials
        },
        "init_kwargs": {
            "data": {
                "type_hint": list[EncryptedPassportElement]
            },
            "credentials": {
                "type_hint": EncryptedCredentials
            }
        },
        "self_kwargs": {}
    },
    PassportElementErrorDataField: {
        "link": "https://core.telegram.org/bots/api#passportelementerrordatafield",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": Literal['personal_details', 'passport', 'driver_license', 'identity_card', 'internal_passport', 'address']
            },
            "field_name": {
                "type_hint": str
            },
            "data_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    PassportElementErrorFrontSide: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorfrontside",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": Literal['passport', 'driver_license', 'identity_card', 'internal_passport']
            },
            "file_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    PassportElementErrorReverseSide: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorreverseside",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": Literal['driver_license', 'identity_card']
            },
            "file_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    PassportElementErrorSelfie: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorselfie",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": Literal['passport', 'driver_license', 'identity_card', 'internal_passport']
            },
            "file_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    PassportElementErrorFile: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorfile",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": Literal['utility_bill', 'bank_statement', 'rental_agreement', 'passport_registration', 'temporary_registration']
            },
            "file_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    PassportElementErrorFiles: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorfiles",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": Literal['utility_bill', 'bank_statement', 'rental_agreement', 'passport_registration', 'temporary_registration']
            },
            "file_hashes": {
                "type_hint": list[str]
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    PassportElementErrorTranslationFile: {
        "link": "https://core.telegram.org/bots/api#passportelementerrortranslationfile",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": Literal['passport', 'driver_license', 'identity_card', 'internal_passport', 'utility_bill', 'bank_statement', 'rental_agreement', 'passport_registration', 'temporary_registration']
            },
            "file_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    PassportElementErrorTranslationFiles: {
        "link": "https://core.telegram.org/bots/api#passportelementerrortranslationfiles",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": Literal['passport', 'driver_license', 'identity_card', 'internal_passport', 'utility_bill', 'bank_statement', 'rental_agreement', 'passport_registration', 'temporary_registration']
            },
            "file_hashes": {
                "type_hint": list[str]
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {}
    },
    PassportElementErrorUnspecified: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorunspecified",
        "has_dese": False,
        "dese_kwargs": {},
        "init_kwargs": {
            "type": {
                "type_hint": str
            },
            "element_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
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
        "init_kwargs": {
            "title": {
                "type_hint": str
            },
            "description": {
                "type_hint": str
            },
            "photo": {
                "type_hint": list[PhotoSize]
            },
            "text": {
                "type_hint": Optional[str],
                "default": None
            },
            "text_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default": None
            },
            "animation": {
                "type_hint": Optional[Animation],
                "default": None
            }
        },
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
        "init_kwargs": {
            "position": {
                "type_hint": int
            },
            "user": {
                "type_hint": User
            },
            "score": {
                "type_hint": int
            }
        },
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
        "init_kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "giveaway_message_id": {
                "type_hint": int
            },
            "winners_selection_date": {
                "type_hint": int
            },
            "winner_count": {
                "type_hint": int
            },
            "winners": {
                "type_hint": list[User]
            },
            "additional_chat_count": {
                "type_hint": Optional[int],
                "default": None
            },
            "premium_subscription_month_count": {
                "type_hint": Optional[int],
                "default": None
            },
            "unclaimed_prize_count": {
                "type_hint": Optional[int],
                "default": None
            },
            "only_new_members": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "was_refunded": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "prize_description": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "winner_count": {
                "type_hint": int
            },
            "unclaimed_prize_count": {
                "type_hint": Optional[int],
                "default": None
            },
            "giveaway_message": {
                "type_hint": Optional[Message],
                "default": None
            }
        },
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
        "init_kwargs": {
            "chats": {
                "type_hint": list[Chat]
            },
            "winners_selection_date": {
                "type_hint": int
            },
            "winner_count": {
                "type_hint": int
            },
            "only_new_members": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "has_public_winners": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "prize_description": {
                "type_hint": Optional[str],
                "default": None
            },
            "country_codes": {
                "type_hint": Optional[list[str]],
                "default": None
            },
            "premium_subscription_month_count": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    MessageOriginUser: {
        "link": "https://core.telegram.org/bots/api#messageoriginuser",
        "has_dese": True,
        "dese_kwargs": {
            "date": None,
            "sender_user": User
        },
        "init_kwargs": {
            "date": {
                "type_hint": int
            },
            "sender_user": {
                "type_hint": User
            }
        },
        "self_kwargs": {}
    },
    MessageOriginHiddenUser: {
        "link": "https://core.telegram.org/bots/api#messageoriginhiddenuser",
        "has_dese": True,
        "dese_kwargs": {
            "date": None,
            "sender_user_name": None
        },
        "init_kwargs": {
            "date": {
                "type_hint": int
            },
            "sender_user_name": {
                "type_hint": str
            }
        },
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
        "init_kwargs": {
            "date": {
                "type_hint": int
            },
            "sender_chat": {
                "type_hint": Chat
            },
            "author_signature": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "date": {
                "type_hint": int
            },
            "chat": {
                "type_hint": Chat
            },
            "message_id": {
                "type_hint": int
            },
            "author_signature": {
                "type_hint": Optional[str],
                "default": None
            }
        },
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
        "init_kwargs": {
            "origin": {
                "type_hint": MessageOrigin
            },
            "chat": {
                "type_hint": Optional[Chat],
                "default": None
            },
            "message_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "link_preview_options": {
                "type_hint": Optional[LinkPreviewOptions],
                "default": None
            },
            "animation": {
                "type_hint": Optional[Animation],
                "default": None
            },
            "audio": {
                "type_hint": Optional[Audio],
                "default": None
            },
            "document": {
                "type_hint": Optional[Document],
                "default": None
            },
            "photo": {
                "type_hint": Optional[list[PhotoSize]],
                "default": None
            },
            "sticker": {
                "type_hint": Optional[Sticker],
                "default": None
            },
            "story": {
                "type_hint": Optional[Story],
                "default": None
            },
            "video": {
                "type_hint": Optional[Video],
                "default": None
            },
            "video_note": {
                "type_hint": Optional[VideoNote],
                "default": None
            },
            "voice": {
                "type_hint": Optional[Voice],
                "default": None
            },
            "has_media_spoiler": {
                "type_hint": Optional[Literal[True]],
                "default": None
            },
            "contact": {
                "type_hint": Optional[Contact],
                "default": None
            },
            "dice": {
                "type_hint": Optional[Dice],
                "default": None
            },
            "game": {
                "type_hint": Optional[Game],
                "default": None
            },
            "giveaway": {
                "type_hint": Optional[Giveaway],
                "default": None
            },
            "giveaway_winners": {
                "type_hint": Optional[GiveawayWinners],
                "default": None
            },
            "invoice": {
                "type_hint": Optional[Invoice],
                "default": None
            },
            "location": {
                "type_hint": Optional[Location],
                "default": None
            },
            "poll": {
                "type_hint": Optional[Poll],
                "default": None
            },
            "venue": {
                "type_hint": Optional[Venue],
                "default": None
            }
        },
        "self_kwargs": {}
    },
    UserChatBoosts: {
        "link": "https://core.telegram.org/bots/api#userchatboosts",
        "has_dese": True,
        "dese_kwargs": {
            "boosts": list[ChatBoost]
        },
        "init_kwargs": {
            "boosts": {
                "type_hint": list[ChatBoost]
            }
        },
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
        "init_kwargs": {
            "update_id": {
                "type_hint": int
            },
            "message": {
                "type_hint": Optional[Message],
                "default": None
            },
            "edited_message": {
                "type_hint": Optional[Message],
                "default": None
            },
            "channel_post": {
                "type_hint": Optional[Message],
                "default": None
            },
            "edited_channel_post": {
                "type_hint": Optional[Message],
                "default": None
            },
            "message_reaction": {
                "type_hint": Optional[MessageReactionUpdated],
                "default": None
            },
            "message_reaction_count": {
                "type_hint": Optional[MessageReactionCountUpdated],
                "default": None
            },
            "inline_query": {
                "type_hint": Optional[InlineQuery],
                "default": None
            },
            "chosen_inline_result": {
                "type_hint": Optional[ChosenInlineResult],
                "default": None
            },
            "callback_query": {
                "type_hint": Optional[CallbackQuery],
                "default": None
            },
            "shipping_query": {
                "type_hint": Optional[ShippingQuery],
                "default": None
            },
            "pre_checkout_query": {
                "type_hint": Optional[PreCheckoutQuery],
                "default": None
            },
            "poll": {
                "type_hint": Optional[Poll],
                "default": None
            },
            "poll_answer": {
                "type_hint": Optional[PollAnswer],
                "default": None
            },
            "my_chat_member": {
                "type_hint": Optional[ChatMemberUpdated],
                "default": None
            },
            "chat_member": {
                "type_hint": Optional[ChatMemberUpdated],
                "default": None
            },
            "chat_join_request": {
                "type_hint": Optional[ChatJoinRequest],
                "default": None
            },
            "chat_boost": {
                "type_hint": Optional[ChatBoostUpdated],
                "default": None
            },
            "removed_chat_boost": {
                "type_hint": Optional[ChatBoostRemoved],
                "default": None
            }
        },
        "self_kwargs": {}
    }
}

warnings = []
logger.info('Program finished.')
