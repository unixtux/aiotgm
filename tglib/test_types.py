#!/bin/python3

IGNORE = ()
IGNORE = ('InputFile', )

import sys
sys.path.append('../')

from typing import (
    Union,
    Optional,
    Literal,
    _UnionGenericAlias
)
from tglib.types import *
from tglib.types import (
    TelegramType,
    ChatMember,
    MessageOrigin,
    ReactionType,
    ChatBoostSource,
    InputMessageContent,
    MaybeInaccessibleMessage
)
from tglib.default_literals import *

TYPES = {
    ChatPermissions: {
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
                "default_value": None
            },
            "can_send_audios": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_send_documents": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_send_photos": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_send_videos": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_send_video_notes": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_send_voice_notes": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_send_polls": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_send_other_messages": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_add_web_page_previews": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_change_info": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_invite_users": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_pin_messages": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_manage_topics": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "can_send_messages": {
                "value": "ok."
            },
            "can_send_audios": {
                "value": "ok."
            },
            "can_send_documents": {
                "value": "ok."
            },
            "can_send_photos": {
                "value": "ok."
            },
            "can_send_videos": {
                "value": "ok."
            },
            "can_send_video_notes": {
                "value": "ok."
            },
            "can_send_voice_notes": {
                "value": "ok."
            },
            "can_send_polls": {
                "value": "ok."
            },
            "can_send_other_messages": {
                "value": "ok."
            },
            "can_add_web_page_previews": {
                "value": "ok."
            },
            "can_change_info": {
                "value": "ok."
            },
            "can_invite_users": {
                "value": "ok."
            },
            "can_pin_messages": {
                "value": "ok."
            },
            "can_manage_topics": {
                "value": "ok."
            }
        }
    },
    ChatAdministratorRights: {
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
            "can_post_messages": None,
            "can_edit_messages": None,
            "can_pin_messages": None,
            "can_post_stories": None,
            "can_edit_stories": None,
            "can_delete_stories": None,
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
            "can_post_messages": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_edit_messages": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_pin_messages": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_post_stories": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_edit_stories": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_delete_stories": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_manage_topics": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "is_anonymous": {
                "value": "ok."
            },
            "can_manage_chat": {
                "value": "ok."
            },
            "can_delete_messages": {
                "value": "ok."
            },
            "can_manage_video_chats": {
                "value": "ok."
            },
            "can_restrict_members": {
                "value": "ok."
            },
            "can_promote_members": {
                "value": "ok."
            },
            "can_change_info": {
                "value": "ok."
            },
            "can_invite_users": {
                "value": "ok."
            },
            "can_post_messages": {
                "value": "ok."
            },
            "can_edit_messages": {
                "value": "ok."
            },
            "can_pin_messages": {
                "value": "ok."
            },
            "can_post_stories": {
                "value": "ok."
            },
            "can_edit_stories": {
                "value": "ok."
            },
            "can_delete_stories": {
                "value": "ok."
            },
            "can_manage_topics": {
                "value": "ok."
            }
        }
    },
    SwitchInlineQueryChosenChat: {
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
                "default_value": None
            },
            "allow_user_chats": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "allow_bot_chats": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "allow_group_chats": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "allow_channel_chats": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "query": {
                "value": "ok."
            },
            "allow_user_chats": {
                "value": "ok."
            },
            "allow_bot_chats": {
                "value": "ok."
            },
            "allow_group_chats": {
                "value": "ok."
            },
            "allow_channel_chats": {
                "value": "ok."
            }
        }
    },
    CallbackGame: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    InputFile: {
        "has_dese": False,
        "init_kwargs": {
            "path": {
                "type_hint": str
            },
            "file_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "hide_name": {
                "type_hint": bool,
                "default_value": False
            }
        },
        "self_kwargs": {
            "path": {
                "value": "ok."
            }
        }
    },
    LoginUrl: {
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
                "default_value": None
            },
            "bot_username": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "request_write_access": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "url": {
                "value": "ok."
            },
            "forward_text": {
                "value": "ok."
            },
            "bot_username": {
                "value": "ok."
            },
            "request_write_access": {
                "value": "ok."
            }
        }
    },
    LabeledPrice: {
        "has_dese": False,
        "init_kwargs": {
            "label": {
                "type_hint": str
            },
            "amount": {
                "type_hint": int
            }
        },
        "self_kwargs": {
            "label": {
                "value": "ok."
            },
            "amount": {
                "value": "ok."
            }
        }
    },
    LinkPreviewOptions: {
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
                "default_value": None
            },
            "url": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "prefer_small_media": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "prefer_large_media": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "show_above_text": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "is_disabled": {
                "value": "ok."
            },
            "url": {
                "value": "ok."
            },
            "prefer_small_media": {
                "value": "ok."
            },
            "prefer_large_media": {
                "value": "ok."
            },
            "show_above_text": {
                "value": "ok."
            }
        }
    },
    User: {
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
                "default_value": None
            },
            "username": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "language_code": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "is_premium": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "added_to_attachment_menu": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "can_join_groups": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_read_all_group_messages": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "supports_inline_queries": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "id": {
                "value": "ok."
            },
            "is_bot": {
                "value": "ok."
            },
            "first_name": {
                "value": "ok."
            },
            "last_name": {
                "value": "ok."
            },
            "username": {
                "value": "ok."
            },
            "language_code": {
                "value": "ok."
            },
            "is_premium": {
                "value": "ok."
            },
            "added_to_attachment_menu": {
                "value": "ok."
            },
            "can_join_groups": {
                "value": "ok."
            },
            "can_read_all_group_messages": {
                "value": "ok."
            },
            "supports_inline_queries": {
                "value": "ok."
            }
        }
    },
    MessageEntity: {
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
                "default_value": None
            },
            "user": {
                "type_hint": Optional[User],
                "default_value": None
            },
            "language": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "custom_emoji_id": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "type": {
                "value": "ok."
            },
            "offset": {
                "value": "ok."
            },
            "length": {
                "value": "ok."
            },
            "url": {
                "value": "ok."
            },
            "user": {
                "value": "ok."
            },
            "language": {
                "value": "ok."
            },
            "custom_emoji_id": {
                "value": "ok."
            }
        }
    },
    TextQuote: {
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
                "default_value": None
            },
            "is_manual": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            }
        },
        "self_kwargs": {
            "text": {
                "value": "ok."
            },
            "position": {
                "value": "ok."
            },
            "entities": {
                "value": "ok."
            },
            "is_manual": {
                "value": "ok."
            }
        }
    },
    ReplyParameters: {
        "has_dese": False,
        "init_kwargs": {
            "message_id": {
                "type_hint": int
            },
            "chat_id": {
                "type_hint": Optional[Union[int, str]],
                "default_value": None
            },
            "allow_sending_without_reply": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "quote": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "quote_parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "quote_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "quote_position": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "message_id": {
                "value": "ok."
            },
            "chat_id": {
                "value": "ok."
            },
            "allow_sending_without_reply": {
                "value": "ok."
            },
            "quote": {
                "value": "ok."
            },
            "quote_parse_mode": {
                "value": "ok."
            },
            "quote_entities": {
                "value": "ok."
            },
            "quote_position": {
                "value": "ok."
            }
        }
    },
    InaccessibleMessage: {
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "message_id": None,
            "date": None
        },
        "init_kwargs": {
            "chat": None,
            "message_id": None,
            "date": {
                "default_value": 0
            }
        },
        "self_kwargs": {
            "chat": {
                "value": "ok.",
                "hinting": Chat
            },
            "message_id": {
                "value": "ok.",
                "hinting": int
            },
            "date": {
                "value": "ok.",
                "hinting": int
            }
        }
    },
    Message: {
        "has_dese": True,
        "dese_kwargs": {
            "message_id": None,
            "date": None,
            "chat": Chat,
            "message_thread_id": None,
            "from_user": User,
            "sender_chat": Chat,
            "forward_origin": MessageOrigin,
            "is_topic_message": None,
            "is_automatic_forward": None,
            "reply_to_message": Message,
            "external_reply": ExternalReplyInfo,
            "quote": TextQuote,
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
            "message_id": None,
            "date": None,
            "chat": None,
            "message_thread_id": {
                "default_value": None
            },
            "from_user": {
                "default_value": None
            },
            "sender_chat": {
                "default_value": None
            },
            "forward_origin": {
                "default_value": None
            },
            "is_topic_message": {
                "default_value": None
            },
            "is_automatic_forward": {
                "default_value": None
            },
            "reply_to_message": {
                "default_value": None
            },
            "external_reply": {
                "default_value": None
            },
            "quote": {
                "default_value": None
            },
            "via_bot": {
                "default_value": None
            },
            "edit_date": {
                "default_value": None
            },
            "has_protected_content": {
                "default_value": None
            },
            "media_group_id": {
                "default_value": None
            },
            "author_signature": {
                "default_value": None
            },
            "text": {
                "default_value": None
            },
            "entities": {
                "default_value": None
            },
            "link_preview_options": {
                "default_value": None
            },
            "animation": {
                "default_value": None
            },
            "audio": {
                "default_value": None
            },
            "document": {
                "default_value": None
            },
            "photo": {
                "default_value": None
            },
            "sticker": {
                "default_value": None
            },
            "story": {
                "default_value": None
            },
            "video": {
                "default_value": None
            },
            "video_note": {
                "default_value": None
            },
            "voice": {
                "default_value": None
            },
            "caption": {
                "default_value": None
            },
            "caption_entities": {
                "default_value": None
            },
            "has_media_spoiler": {
                "default_value": None
            },
            "contact": {
                "default_value": None
            },
            "dice": {
                "default_value": None
            },
            "game": {
                "default_value": None
            },
            "poll": {
                "default_value": None
            },
            "venue": {
                "default_value": None
            },
            "location": {
                "default_value": None
            },
            "new_chat_members": {
                "default_value": None
            },
            "left_chat_member": {
                "default_value": None
            },
            "new_chat_title": {
                "default_value": None
            },
            "new_chat_photo": {
                "default_value": None
            },
            "delete_chat_photo": {
                "default_value": None
            },
            "group_chat_created": {
                "default_value": None
            },
            "supergroup_chat_created": {
                "default_value": None
            },
            "channel_chat_created": {
                "default_value": None
            },
            "message_auto_delete_timer_changed": {
                "default_value": None
            },
            "migrate_to_chat_id": {
                "default_value": None
            },
            "migrate_from_chat_id": {
                "default_value": None
            },
            "pinned_message": {
                "default_value": None
            },
            "invoice": {
                "default_value": None
            },
            "successful_payment": {
                "default_value": None
            },
            "users_shared": {
                "default_value": None
            },
            "chat_shared": {
                "default_value": None
            },
            "connected_website": {
                "default_value": None
            },
            "write_access_allowed": {
                "default_value": None
            },
            "passport_data": {
                "default_value": None
            },
            "proximity_alert_triggered": {
                "default_value": None
            },
            "forum_topic_created": {
                "default_value": None
            },
            "forum_topic_edited": {
                "default_value": None
            },
            "forum_topic_closed": {
                "default_value": None
            },
            "forum_topic_reopened": {
                "default_value": None
            },
            "general_forum_topic_hidden": {
                "default_value": None
            },
            "general_forum_topic_unhidden": {
                "default_value": None
            },
            "giveaway_created": {
                "default_value": None
            },
            "giveaway": {
                "default_value": None
            },
            "giveaway_winners": {
                "default_value": None
            },
            "giveaway_completed": {
                "default_value": None
            },
            "video_chat_scheduled": {
                "default_value": None
            },
            "video_chat_started": {
                "default_value": None
            },
            "video_chat_ended": {
                "default_value": None
            },
            "video_chat_participants_invited": {
                "default_value": None
            },
            "web_app_data": {
                "default_value": None
            },
            "reply_markup": {
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "text": {
                    "value": "text or str() # If not text, it's str() instead of None",
                    "type_hint": str
                }
            },
            "message_id": {
                "value": "ok.",
                "hinting": int
            },
            "date": {
                "value": "ok.",
                "hinting": int
            },
            "chat": {
                "value": "ok.",
                "hinting": Chat
            },
            "message_thread_id": {
                "value": "ok.",
                "hinting": Optional[int]
            },
            "from_user": {
                "value": "ok.",
                "hinting": Optional[User]
            },
            "sender_chat": {
                "value": "ok.",
                "hinting": Optional[Chat]
            },
            "forward_origin": {
                "value": "ok.",
                "hinting": Optional[MessageOrigin]
            },
            "is_topic_message": {
                "value": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "is_automatic_forward": {
                "value": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "reply_to_message": {
                "value": "ok.",
                "hinting": Optional[Message]
            },
            "external_reply": {
                "value": "ok.",
                "hinting": Optional[ExternalReplyInfo]
            },
            "quote": {
                "value": "ok.",
                "hinting": Optional[TextQuote]
            },
            "via_bot": {
                "value": "ok.",
                "hinting": Optional[User]
            },
            "edit_date": {
                "value": "ok.",
                "hinting": Optional[int]
            },
            "has_protected_content": {
                "value": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "media_group_id": {
                "value": "ok.",
                "hinting": Optional[str]
            },
            "author_signature": {
                "value": "ok.",
                "hinting": Optional[str]
            },
            "entities": {
                "value": "ok.",
                "hinting": Optional[list[MessageEntity]]
            },
            "link_preview_options": {
                "value": "ok.",
                "hinting": Optional[LinkPreviewOptions]
            },
            "animation": {
                "value": "ok.",
                "hinting": Optional[Animation]
            },
            "audio": {
                "value": "ok.",
                "hinting": Optional[Audio]
            },
            "document": {
                "value": "ok.",
                "hinting": Optional[Document]
            },
            "photo": {
                "value": "ok.",
                "hinting": Optional[list[PhotoSize]]
            },
            "sticker": {
                "value": "ok.",
                "hinting": Optional[Sticker]
            },
            "story": {
                "value": "ok.",
                "hinting": Optional[Story]
            },
            "video": {
                "value": "ok.",
                "hinting": Optional[Video]
            },
            "video_note": {
                "value": "ok.",
                "hinting": Optional[VideoNote]
            },
            "voice": {
                "value": "ok.",
                "hinting": Optional[Voice]
            },
            "caption": {
                "value": "ok.",
                "hinting": Optional[str]
            },
            "caption_entities": {
                "value": "ok.",
                "hinting": Optional[list[MessageEntity]]
            },
            "has_media_spoiler": {
                "value": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "contact": {
                "value": "ok.",
                "hinting": Optional[Contact]
            },
            "dice": {
                "value": "ok.",
                "hinting": Optional[Dice]
            },
            "game": {
                "value": "ok.",
                "hinting": Optional[Game]
            },
            "poll": {
                "value": "ok.",
                "hinting": Optional[Poll]
            },
            "venue": {
                "value": "ok.",
                "hinting": Optional[Venue]
            },
            "location": {
                "value": "ok.",
                "hinting": Optional[Location]
            },
            "new_chat_members": {
                "value": "ok.",
                "hinting": Optional[list[User]]
            },
            "left_chat_member": {
                "value": "ok.",
                "hinting": Optional[User]
            },
            "new_chat_title": {
                "value": "ok.",
                "hinting": Optional[str]
            },
            "new_chat_photo": {
                "value": "ok.",
                "hinting": Optional[list[PhotoSize]]
            },
            "delete_chat_photo": {
                "value": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "group_chat_created": {
                "value": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "supergroup_chat_created": {
                "value": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "channel_chat_created": {
                "value": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "message_auto_delete_timer_changed": {
                "value": "ok.",
                "hinting": Optional[MessageAutoDeleteTimerChanged]
            },
            "migrate_to_chat_id": {
                "value": "ok.",
                "hinting": Optional[int]
            },
            "migrate_from_chat_id": {
                "value": "ok.",
                "hinting": Optional[int]
            },
            "pinned_message": {
                "value": "ok.",
                "hinting": Optional[MaybeInaccessibleMessage]
            },
            "invoice": {
                "value": "ok.",
                "hinting": Optional[Invoice]
            },
            "successful_payment": {
                "value": "ok.",
                "hinting": Optional[SuccessfulPayment]
            },
            "users_shared": {
                "value": "ok.",
                "hinting": Optional[UsersShared]
            },
            "chat_shared": {
                "value": "ok.",
                "hinting": Optional[ChatShared]
            },
            "connected_website": {
                "value": "ok.",
                "hinting": Optional[str]
            },
            "write_access_allowed": {
                "value": "ok.",
                "hinting": Optional[WriteAccessAllowed]
            },
            "passport_data": {
                "value": "ok.",
                "hinting": Optional[PassportData]
            },
            "proximity_alert_triggered": {
                "value": "ok.",
                "hinting": Optional[ProximityAlertTriggered]
            },
            "forum_topic_created": {
                "value": "ok.",
                "hinting": Optional[ForumTopicCreated]
            },
            "forum_topic_edited": {
                "value": "ok.",
                "hinting": Optional[ForumTopicEdited]
            },
            "forum_topic_closed": {
                "value": "ok.",
                "hinting": Optional[ForumTopicClosed]
            },
            "forum_topic_reopened": {
                "value": "ok.",
                "hinting": Optional[ForumTopicReopened]
            },
            "general_forum_topic_hidden": {
                "value": "ok.",
                "hinting": Optional[GeneralForumTopicHidden]
            },
            "general_forum_topic_unhidden": {
                "value": "ok.",
                "hinting": Optional[GeneralForumTopicUnhidden]
            },
            "giveaway_created": {
                "value": "ok.",
                "hinting": Optional[GiveawayCreated]
            },
            "giveaway": {
                "value": "ok.",
                "hinting": Optional[Giveaway]
            },
            "giveaway_winners": {
                "value": "ok.",
                "hinting": Optional[GiveawayWinners]
            },
            "giveaway_completed": {
                "value": "ok.",
                "hinting": Optional[GiveawayCompleted]
            },
            "video_chat_scheduled": {
                "value": "ok.",
                "hinting": Optional[VideoChatScheduled]
            },
            "video_chat_started": {
                "value": "ok.",
                "hinting": Optional[VideoChatStarted]
            },
            "video_chat_ended": {
                "value": "ok.",
                "hinting": Optional[VideoChatEnded]
            },
            "video_chat_participants_invited": {
                "value": "ok.",
                "hinting": Optional[VideoChatParticipantsInvited]
            },
            "web_app_data": {
                "value": "ok.",
                "hinting": Optional[WebAppData]
            },
            "reply_markup": {
                "value": "ok.",
                "hinting": Optional[InlineKeyboardMarkup]
            }
        }
    },
    ChatPhoto: {
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
        "self_kwargs": {
            "small_file_id": {
                "value": "ok."
            },
            "small_file_unique_id": {
                "value": "ok."
            },
            "big_file_id": {
                "value": "ok."
            },
            "big_file_unique_id": {
                "value": "ok."
            }
        }
    },
    Location: {
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
                "default_value": None
            },
            "live_period": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "heading": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "proximity_alert_radius": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "longitude": {
                "value": "ok."
            },
            "latitude": {
                "value": "ok."
            },
            "horizontal_accuracy": {
                "value": "ok."
            },
            "live_period": {
                "value": "ok."
            },
            "heading": {
                "value": "ok."
            },
            "proximity_alert_radius": {
                "value": "ok."
            }
        }
    },
    ChatLocation: {
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
        "self_kwargs": {
            "location": {
                "value": "ok."
            },
            "address": {
                "value": "ok."
            }
        }
    },
    ReactionTypeEmoji: {
        "has_dese": True,
        "dese_kwargs": {
            "emoji": None
        },
        "init_kwargs": {
            "emoji": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_REACTION_TYPE_EMOJI
                }
            },
            "emoji": {
                "value": "ok."
            }
        }
    },
    ReactionTypeCustomEmoji: {
        "has_dese": True,
        "dese_kwargs": {
            "custom_emoji_id": None
        },
        "init_kwargs": {
            "custom_emoji_id": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_REACTION_TYPE_CUSTOM_EMOJI
                }
            },
            "custom_emoji_id": {
                "value": "ok."
            }
        }
    },
    Chat: {
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
            "message_auto_delete_time": None,
            "has_aggressive_anti_spam_enabled": None,
            "has_hidden_members": None,
            "has_protected_content": None,
            "has_visible_history": None,
            "sticker_set_name": None,
            "can_set_sticker_set": None,
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
                "default_value": None
            },
            "username": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "first_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "last_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "is_forum": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "photo": {
                "type_hint": Optional[ChatPhoto],
                "default_value": None
            },
            "active_usernames": {
                "type_hint": Optional[list[str]],
                "default_value": None
            },
            "available_reactions": {
                "type_hint": Optional[list[ReactionType]],
                "default_value": None
            },
            "accent_color_id": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "background_custom_emoji_id": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "profile_accent_color_id": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "profile_background_custom_emoji_id": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "emoji_status_custom_emoji_id": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "emoji_status_expiration_date": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "bio": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "has_private_forwards": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "has_restricted_voice_and_video_messages": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "join_to_send_messages": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "join_by_request": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "description": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "invite_link": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "pinned_message": {
                "type_hint": Optional[Message],
                "default_value": None
            },
            "permissions": {
                "type_hint": Optional[ChatPermissions],
                "default_value": None
            },
            "slow_mode_delay": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "message_auto_delete_time": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "has_aggressive_anti_spam_enabled": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "has_hidden_members": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "has_protected_content": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "has_visible_history": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "sticker_set_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "can_set_sticker_set": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "linked_chat_id": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "location": {
                "type_hint": Optional[ChatLocation],
                "default_value": None
            }
        },
        "self_kwargs": {
            "id": {
                "value": "ok."
            },
            "type": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "username": {
                "value": "ok."
            },
            "first_name": {
                "value": "ok."
            },
            "last_name": {
                "value": "ok."
            },
            "is_forum": {
                "value": "ok."
            },
            "photo": {
                "value": "ok."
            },
            "active_usernames": {
                "value": "ok."
            },
            "available_reactions": {
                "value": "ok."
            },
            "accent_color_id": {
                "value": "ok."
            },
            "background_custom_emoji_id": {
                "value": "ok."
            },
            "profile_accent_color_id": {
                "value": "ok."
            },
            "profile_background_custom_emoji_id": {
                "value": "ok."
            },
            "emoji_status_custom_emoji_id": {
                "value": "ok."
            },
            "emoji_status_expiration_date": {
                "value": "ok."
            },
            "bio": {
                "value": "ok."
            },
            "has_private_forwards": {
                "value": "ok."
            },
            "has_restricted_voice_and_video_messages": {
                "value": "ok."
            },
            "join_to_send_messages": {
                "value": "ok."
            },
            "join_by_request": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "invite_link": {
                "value": "ok."
            },
            "pinned_message": {
                "value": "ok."
            },
            "permissions": {
                "value": "ok."
            },
            "slow_mode_delay": {
                "value": "ok."
            },
            "message_auto_delete_time": {
                "value": "ok."
            },
            "has_aggressive_anti_spam_enabled": {
                "value": "ok."
            },
            "has_hidden_members": {
                "value": "ok."
            },
            "has_protected_content": {
                "value": "ok."
            },
            "has_visible_history": {
                "value": "ok."
            },
            "sticker_set_name": {
                "value": "ok."
            },
            "can_set_sticker_set": {
                "value": "ok."
            },
            "linked_chat_id": {
                "value": "ok."
            },
            "location": {
                "value": "ok."
            }
        }
    },
    MessageReactionUpdated: {
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
                "default_value": None
            },
            "actor_chat": {
                "type_hint": Optional[Chat],
                "default_value": None
            }
        },
        "self_kwargs": {
            "chat": {
                "value": "ok."
            },
            "message_id": {
                "value": "ok."
            },
            "date": {
                "value": "ok."
            },
            "old_reaction": {
                "value": "ok."
            },
            "new_reaction": {
                "value": "ok."
            },
            "user": {
                "value": "ok."
            },
            "actor_chat": {
                "value": "ok."
            }
        }
    },
    ReactionCount: {
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
        "self_kwargs": {
            "type": {
                "value": "ok."
            },
            "total_count": {
                "value": "ok."
            }
        }
    },
    MessageReactionCountUpdated: {
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
        "self_kwargs": {
            "chat": {
                "value": "ok."
            },
            "message_id": {
                "value": "ok."
            },
            "date": {
                "value": "ok."
            },
            "reactions": {
                "value": "ok."
            }
        }
    },
    MessageId: {
        "has_dese": True,
        "dese_kwargs": {
            "message_id": None
        },
        "init_kwargs": {
            "message_id": {
                "type_hint": int
            }
        },
        "self_kwargs": {
            "message_id": {
                "value": "ok."
            }
        }
    },
    PhotoSize: {
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
                "default_value": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "width": {
                "value": "ok."
            },
            "height": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            }
        }
    },
    Animation: {
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
                "default_value": None
            },
            "file_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "mime_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "width": {
                "value": "ok."
            },
            "height": {
                "value": "ok."
            },
            "duration": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            },
            "file_name": {
                "value": "ok."
            },
            "mime_type": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            }
        }
    },
    Audio: {
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
                "default_value": None
            },
            "title": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "file_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "mime_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "thumbnail": {
                "type_hint": Optional[PhotoSize],
                "default_value": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "duration": {
                "value": "ok."
            },
            "performer": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "file_name": {
                "value": "ok."
            },
            "mime_type": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            }
        }
    },
    Document: {
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
                "default_value": None
            },
            "file_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "mime_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            },
            "file_name": {
                "value": "ok."
            },
            "mime_type": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            }
        }
    },
    Story: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    Video: {
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
                "default_value": None
            },
            "file_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "mime_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "width": {
                "value": "ok."
            },
            "height": {
                "value": "ok."
            },
            "duration": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            },
            "file_name": {
                "value": "ok."
            },
            "mime_type": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            }
        }
    },
    VideoNote: {
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
                "default_value": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "length": {
                "value": "ok."
            },
            "duration": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            }
        }
    },
    Voice: {
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
                "default_value": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "duration": {
                "value": "ok."
            },
            "mime_type": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            }
        }
    },
    Contact: {
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
                "default_value": None
            },
            "user_id": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "vcard": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "phone_number": {
                "value": "ok."
            },
            "first_name": {
                "value": "ok."
            },
            "last_name": {
                "value": "ok."
            },
            "user_id": {
                "value": "ok."
            },
            "vcard": {
                "value": "ok."
            }
        }
    },
    Dice: {
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
        "self_kwargs": {
            "emoji": {
                "value": "ok."
            },
            "value": {
                "value": "ok."
            }
        }
    },
    PollOption: {
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
        "self_kwargs": {
            "text": {
                "value": "ok."
            },
            "voter_count": {
                "value": "ok."
            }
        }
    },
    PollAnswer: {
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
                "default_value": None
            },
            "user": {
                "type_hint": Optional[User],
                "default_value": None
            }
        },
        "self_kwargs": {
            "poll_id": {
                "value": "ok."
            },
            "option_ids": {
                "value": "ok."
            },
            "voter_chat": {
                "value": "ok."
            },
            "user": {
                "value": "ok."
            }
        }
    },
    Poll: {
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
                "default_value": None
            },
            "explanation": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "explanation_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "open_period": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "close_date": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "id": {
                "value": "ok."
            },
            "question": {
                "value": "ok."
            },
            "options": {
                "value": "ok."
            },
            "total_voter_count": {
                "value": "ok."
            },
            "is_closed": {
                "value": "ok."
            },
            "is_anonymous": {
                "value": "ok."
            },
            "type": {
                "value": "ok."
            },
            "allows_multiple_answers": {
                "value": "ok."
            },
            "correct_option_id": {
                "value": "ok."
            },
            "explanation": {
                "value": "ok."
            },
            "explanation_entities": {
                "value": "ok."
            },
            "open_period": {
                "value": "ok."
            },
            "close_date": {
                "value": "ok."
            }
        }
    },
    Venue: {
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
                "default_value": None
            },
            "foursquare_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "google_place_id": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "google_place_type": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "location": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "address": {
                "value": "ok."
            },
            "foursquare_id": {
                "value": "ok."
            },
            "foursquare_type": {
                "value": "ok."
            },
            "google_place_id": {
                "value": "ok."
            },
            "google_place_type": {
                "value": "ok."
            }
        }
    },
    WebAppData: {
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
        "self_kwargs": {
            "data": {
                "value": "ok."
            },
            "button_text": {
                "value": "ok."
            }
        }
    },
    ProximityAlertTriggered: {
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
        "self_kwargs": {
            "traveler": {
                "value": "ok."
            },
            "watcher": {
                "value": "ok."
            },
            "distance": {
                "value": "ok."
            }
        }
    },
    MessageAutoDeleteTimerChanged: {
        "has_dese": True,
        "dese_kwargs": {
            "message_auto_delete_time": None
        },
        "init_kwargs": {
            "message_auto_delete_time": {
                "type_hint": int
            }
        },
        "self_kwargs": {
            "message_auto_delete_time": {
                "value": "ok."
            }
        }
    },
    ForumTopicCreated: {
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
                "default_value": None
            }
        },
        "self_kwargs": {
            "name": {
                "value": "ok."
            },
            "icon_color": {
                "value": "ok."
            },
            "icon_custom_emoji_id": {
                "value": "ok."
            }
        }
    },
    ForumTopicClosed: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    ForumTopicEdited: {
        "has_dese": True,
        "dese_kwargs": {
            "name": None,
            "icon_custom_emoji_id": None
        },
        "init_kwargs": {
            "name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "icon_custom_emoji_id": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "name": {
                "value": "ok."
            },
            "icon_custom_emoji_id": {
                "value": "ok."
            }
        }
    },
    ForumTopicReopened: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    GeneralForumTopicHidden: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    GeneralForumTopicUnhidden: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    UsersShared: {
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
        "self_kwargs": {
            "request_id": {
                "value": "ok."
            },
            "user_ids": {
                "value": "ok."
            }
        }
    },
    ChatShared: {
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
        "self_kwargs": {
            "request_id": {
                "value": "ok."
            },
            "chat_id": {
                "value": "ok."
            }
        }
    },
    WriteAccessAllowed: {
        "has_dese": True,
        "dese_kwargs": {
            "from_request": None,
            "web_app_name": None,
            "from_attachment_menu": None
        },
        "init_kwargs": {
            "from_request": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "web_app_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "from_attachment_menu": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "from_request": {
                "value": "ok."
            },
            "web_app_name": {
                "value": "ok."
            },
            "from_attachment_menu": {
                "value": "ok."
            }
        }
    },
    VideoChatScheduled: {
        "has_dese": True,
        "dese_kwargs": {
            "start_date": None
        },
        "init_kwargs": {
            "start_date": {
                "type_hint": int
            }
        },
        "self_kwargs": {
            "start_date": {
                "value": "ok."
            }
        }
    },
    VideoChatStarted: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    VideoChatEnded: {
        "has_dese": True,
        "dese_kwargs": {
            "duration": None
        },
        "init_kwargs": {
            "duration": {
                "type_hint": int
            }
        },
        "self_kwargs": {
            "duration": {
                "value": "ok."
            }
        }
    },
    VideoChatParticipantsInvited: {
        "has_dese": True,
        "dese_kwargs": {
            "users": list[User]
        },
        "init_kwargs": {
            "users": {
                "type_hint": list[User]
            }
        },
        "self_kwargs": {
            "users": {
                "value": "ok."
            }
        }
    },
    UserProfilePhotos: {
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
        "self_kwargs": {
            "total_count": {
                "value": "ok."
            },
            "photos": {
                "value": "ok."
            }
        }
    },
    File: {
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
                "default_value": None
            },
            "file_path": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            },
            "file_path": {
                "value": "ok."
            }
        }
    },
    WebAppInfo: {
        "has_dese": True,
        "dese_kwargs": {
            "url": None
        },
        "init_kwargs": {
            "url": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "url": {
                "value": "ok."
            }
        }
    },
    KeyboardButtonRequestUsers: {
        "has_dese": False,
        "init_kwargs": {
            "request_id": {
                "type_hint": int
            },
            "user_is_bot": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "user_is_premium": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "max_quantity": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "request_id": {
                "value": "ok."
            },
            "user_is_bot": {
                "value": "ok."
            },
            "user_is_premium": {
                "value": "ok."
            },
            "max_quantity": {
                "value": "ok."
            }
        }
    },
    KeyboardButtonRequestChat: {
        "has_dese": False,
        "init_kwargs": {
            "request_id": {
                "type_hint": int
            },
            "chat_is_channel": {
                "type_hint": bool
            },
            "chat_is_forum": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "chat_has_username": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "chat_is_created": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "user_administrator_rights": {
                "type_hint": Optional[ChatAdministratorRights],
                "default_value": None
            },
            "bot_administrator_rights": {
                "type_hint": Optional[ChatAdministratorRights],
                "default_value": None
            },
            "bot_is_member": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "request_id": {
                "value": "ok."
            },
            "chat_is_channel": {
                "value": "ok."
            },
            "chat_is_forum": {
                "value": "ok."
            },
            "chat_has_username": {
                "value": "ok."
            },
            "chat_is_created": {
                "value": "ok."
            },
            "user_administrator_rights": {
                "value": "ok."
            },
            "bot_administrator_rights": {
                "value": "ok."
            },
            "bot_is_member": {
                "value": "ok."
            }
        }
    },
    KeyboardButtonPollType: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "type": {
                "value": "ok."
            }
        }
    },
    KeyboardButton: {
        "has_dese": False,
        "init_kwargs": {
            "text": {
                "type_hint": str
            },
            "request_users": {
                "type_hint": Optional[KeyboardButtonRequestUsers],
                "default_value": None
            },
            "request_chat": {
                "type_hint": Optional[KeyboardButtonRequestChat],
                "default_value": None
            },
            "request_contact": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "request_location": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "request_poll": {
                "type_hint": Optional[KeyboardButtonPollType],
                "default_value": None
            },
            "web_app": {
                "type_hint": Optional[WebAppInfo],
                "default_value": None
            }
        },
        "self_kwargs": {
            "text": {
                "value": "ok."
            },
            "request_users": {
                "value": "ok."
            },
            "request_chat": {
                "value": "ok."
            },
            "request_contact": {
                "value": "ok."
            },
            "request_location": {
                "value": "ok."
            },
            "request_poll": {
                "value": "ok."
            },
            "web_app": {
                "value": "ok."
            }
        }
    },
    ReplyKeyboardMarkup: {
        "has_dese": False,
        "init_kwargs": {
            "keyboard": {
                "type_hint": Optional[list[list[KeyboardButton]]],
                "default_value": None
            },
            "is_persistent": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "resize_keyboard": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "one_time_keyboard": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "input_field_placeholder": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "selective": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "keyboard": {
                    "value": "keyboard or []"
                }
            },
            "is_persistent": {
                "value": "ok."
            },
            "resize_keyboard": {
                "value": "ok."
            },
            "one_time_keyboard": {
                "value": "ok."
            },
            "input_field_placeholder": {
                "value": "ok."
            },
            "selective": {
                "value": "ok."
            }
        }
    },
    ReplyKeyboardRemove: {
        "has_dese": False,
        "init_kwargs": {
            "selective": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "remove_keyboard": {
                    "value": True,
                    "type_hint": Literal[True]
                }
            },
            "selective": {
                "value": "ok."
            }
        }
    },
    InlineKeyboardButton: {
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
                "default_value": None
            },
            "callback_data": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "web_app": {
                "type_hint": Optional[WebAppInfo],
                "default_value": None
            },
            "login_url": {
                "type_hint": Optional[LoginUrl],
                "default_value": None
            },
            "switch_inline_query": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "switch_inline_query_current_chat": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "switch_inline_query_chosen_chat": {
                "type_hint": Optional[SwitchInlineQueryChosenChat],
                "default_value": None
            },
            "callback_game": {
                "type_hint": Optional[CallbackGame],
                "default_value": None
            },
            "pay": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "text": {
                "value": "ok."
            },
            "url": {
                "value": "ok."
            },
            "callback_data": {
                "value": "ok."
            },
            "web_app": {
                "value": "ok."
            },
            "login_url": {
                "value": "ok."
            },
            "switch_inline_query": {
                "value": "ok."
            },
            "switch_inline_query_current_chat": {
                "value": "ok."
            },
            "switch_inline_query_chosen_chat": {
                "value": "ok."
            },
            "callback_game": {
                "value": "ok."
            },
            "pay": {
                "value": "ok."
            }
        }
    },
    InlineKeyboardMarkup: {
        "has_dese": True,
        "dese_kwargs": {
            "inline_keyboard": list[list[InlineKeyboardButton]]
        },
        "init_kwargs": {
            "inline_keyboard": {
                "type_hint": Optional[list[list[InlineKeyboardButton]]],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "inline_keyboard": {
                    "value": "inline_keyboard or []"
                }
            }
        }
    },
    CallbackQuery: {
        "has_dese": True,
        "dese_kwargs": {
            "id": None,
            "from_user": User,
            "message": MaybeInaccessibleMessage,
            "inline_message_id": None,
            "chat_instance": None,
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
                "default_value": None
            },
            "inline_message_id": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "data": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "game_short_name": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "id": {
                "value": "ok."
            },
            "from_user": {
                "value": "ok."
            },
            "chat_instance": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            },
            "inline_message_id": {
                "value": "ok."
            },
            "data": {
                "value": "ok."
            },
            "game_short_name": {
                "value": "ok."
            }
        }
    },
    ForceReply: {
        "has_dese": False,
        "init_kwargs": {
            "force_reply": {
                "type_hint": Literal[True],
                "default_value": True
            },
            "input_field_placeholder": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "selective": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "force_reply": {
                "value": "ok."
            },
            "input_field_placeholder": {
                "value": "ok."
            },
            "selective": {
                "value": "ok."
            }
        }
    },
    ChatInviteLink: {
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
                "default_value": None
            },
            "expire_date": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "member_limit": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "pending_join_request_count": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "invite_link": {
                "value": "ok."
            },
            "creator": {
                "value": "ok."
            },
            "creates_join_request": {
                "value": "ok."
            },
            "is_primary": {
                "value": "ok."
            },
            "is_revoked": {
                "value": "ok."
            },
            "name": {
                "value": "ok."
            },
            "expire_date": {
                "value": "ok."
            },
            "member_limit": {
                "value": "ok."
            },
            "pending_join_request_count": {
                "value": "ok."
            }
        }
    },
    ChatMemberOwner: {
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
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "value": DEFAULT_CHAT_MEMBER_OWNER
                }
            },
            "user": {
                "value": "ok."
            },
            "is_anonymous": {
                "value": "ok."
            },
            "custom_title": {
                "value": "ok."
            }
        }
    },
    ChatMemberAdministrator: {
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
            "can_post_messages": None,
            "can_edit_messages": None,
            "can_pin_messages": None,
            "can_post_stories": None,
            "can_edit_stories": None,
            "can_delete_stories": None,
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
            "can_post_messages": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_edit_messages": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_pin_messages": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_post_stories": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_edit_stories": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_delete_stories": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "can_manage_topics": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "custom_title": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "value": DEFAULT_CHAT_MEMBER_ADMINISTRATOR
                }
            },
            "user": {
                "value": "ok."
            },
            "can_be_edited": {
                "value": "ok."
            },
            "is_anonymous": {
                "value": "ok."
            },
            "can_manage_chat": {
                "value": "ok."
            },
            "can_delete_messages": {
                "value": "ok."
            },
            "can_manage_video_chats": {
                "value": "ok."
            },
            "can_restrict_members": {
                "value": "ok."
            },
            "can_promote_members": {
                "value": "ok."
            },
            "can_change_info": {
                "value": "ok."
            },
            "can_invite_users": {
                "value": "ok."
            },
            "can_post_messages": {
                "value": "ok."
            },
            "can_edit_messages": {
                "value": "ok."
            },
            "can_pin_messages": {
                "value": "ok."
            },
            "can_post_stories": {
                "value": "ok."
            },
            "can_edit_stories": {
                "value": "ok."
            },
            "can_delete_stories": {
                "value": "ok."
            },
            "can_manage_topics": {
                "value": "ok."
            },
            "custom_title": {
                "value": "ok."
            }
        }
    },
    ChatMemberMember: {
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "value": DEFAULT_CHAT_MEMBER_MEMBER
                }
            },
            "user": {
                "value": "ok."
            }
        }
    },
    ChatMemberRestricted: {
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
        "self_kwargs": {
            "warning": {
                "status": {
                    "value": DEFAULT_CHAT_MEMBER_RESTRICTED
                }
            },
            "user": {
                "value": "ok."
            },
            "is_member": {
                "value": "ok."
            },
            "can_send_messages": {
                "value": "ok."
            },
            "can_send_audios": {
                "value": "ok."
            },
            "can_send_documents": {
                "value": "ok."
            },
            "can_send_photos": {
                "value": "ok."
            },
            "can_send_videos": {
                "value": "ok."
            },
            "can_send_video_notes": {
                "value": "ok."
            },
            "can_send_voice_notes": {
                "value": "ok."
            },
            "can_send_polls": {
                "value": "ok."
            },
            "can_send_other_messages": {
                "value": "ok."
            },
            "can_add_web_page_previews": {
                "value": "ok."
            },
            "can_change_info": {
                "value": "ok."
            },
            "can_invite_users": {
                "value": "ok."
            },
            "can_pin_messages": {
                "value": "ok."
            },
            "can_manage_topics": {
                "value": "ok."
            },
            "until_date": {
                "value": "ok."
            }
        }
    },
    ChatMemberLeft: {
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "value": DEFAULT_CHAT_MEMBER_LEFT
                }
            },
            "user": {
                "value": "ok."
            }
        }
    },
    ChatMemberBanned: {
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
        "self_kwargs": {
            "warning": {
                "status": {
                    "value": DEFAULT_CHAT_MEMBER_BANNED
                }
            },
            "user": {
                "value": "ok."
            },
            "until_date": {
                "value": "ok."
            }
        }
    },
    ChatMemberUpdated: {
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
                "default_value": None
            },
            "via_chat_folder_invite_link": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "chat": {
                "value": "ok."
            },
            "from_user": {
                "value": "ok."
            },
            "date": {
                "value": "ok."
            },
            "old_chat_member": {
                "value": "ok."
            },
            "new_chat_member": {
                "value": "ok."
            },
            "invite_link": {
                "value": "ok."
            },
            "via_chat_folder_invite_link": {
                "value": "ok."
            }
        }
    },
    ChatJoinRequest: {
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
                "default_value": None
            },
            "invite_link": {
                "type_hint": Optional[ChatInviteLink],
                "default_value": None
            }
        },
        "self_kwargs": {
            "chat": {
                "value": "ok."
            },
            "from_user": {
                "value": "ok."
            },
            "user_chat_id": {
                "value": "ok."
            },
            "date": {
                "value": "ok."
            },
            "bio": {
                "value": "ok."
            },
            "invite_link": {
                "value": "ok."
            }
        }
    },
    ForumTopic: {
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
                "default_value": None
            }
        },
        "self_kwargs": {
            "message_thread_id": {
                "value": "ok."
            },
            "name": {
                "value": "ok."
            },
            "icon_color": {
                "value": "ok."
            },
            "icon_custom_emoji_id": {
                "value": "ok."
            }
        }
    },
    BotCommand: {
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
        "self_kwargs": {
            "command": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            }
        }
    },
    BotCommandScopeDefault: {
        "has_dese": False,
        "init_kwargs": {},
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_BOT_COMMAND_SCOPE_DEFAULT
                }
            }
        }
    },
    BotCommandScopeAllPrivateChats: {
        "has_dese": False,
        "init_kwargs": {},
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_BOT_COMMAND_SCOPE_ALL_PRIVATE_CHATS
                }
            }
        }
    },
    BotCommandScopeAllGroupChats: {
        "has_dese": False,
        "init_kwargs": {},
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_BOT_COMMAND_SCOPE_ALL_GROUP_CHATS
                }
            }
        }
    },
    BotCommandScopeAllChatAdministrators: {
        "has_dese": False,
        "init_kwargs": {},
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_BOT_COMMAND_SCOPE_ALL_CHAT_ADMINISTRATORS
                }
            }
        }
    },
    BotCommandScopeChat: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": {
                "type_hint": Union[int, str]
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_BOT_COMMAND_SCOPE_CHAT
                }
            },
            "chat_id": {
                "value": "ok."
            }
        }
    },
    BotCommandScopeChatAdministrators: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": {
                "type_hint": Union[int, str]
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_BOT_COMMAND_SCOPE_CHAT_ADMINISTRATORS
                }
            },
            "chat_id": {
                "value": "ok."
            }
        }
    },
    BotCommandScopeChatMember: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": {
                "type_hint": Union[int, str]
            },
            "user_id": {
                "type_hint": int
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_BOT_COMMAND_SCOPE_CHAT_MEMBER
                }
            },
            "chat_id": {
                "value": "ok."
            },
            "user_id": {
                "value": "ok."
            }
        }
    },
    BotName: {
        "has_dese": True,
        "dese_kwargs": {
            "name": None
        },
        "init_kwargs": {
            "name": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "name": {
                "value": "ok."
            }
        }
    },
    BotDescription: {
        "has_dese": True,
        "dese_kwargs": {
            "description": None
        },
        "init_kwargs": {
            "description": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "description": {
                "value": "ok."
            }
        }
    },
    BotShortDescription: {
        "has_dese": True,
        "dese_kwargs": {
            "short_description": None
        },
        "init_kwargs": {
            "short_description": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "short_description": {
                "value": "ok."
            }
        }
    },
    MenuButtonCommands: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_MENU_BUTTON_COMMANDS
                }
            }
        }
    },
    MenuButtonWebApp: {
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_MENU_BUTTON_WEB_APP
                }
            },
            "text": {
                "value": "ok."
            },
            "web_app": {
                "value": "ok."
            }
        }
    },
    MenuButtonDefault: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_MENU_BUTTON_DEFAULT
                }
            }
        }
    },
    ResponseParameters: {
        "has_dese": True,
        "dese_kwargs": {
            "migrate_to_chat_id": None,
            "retry_after": None
        },
        "init_kwargs": {
            "migrate_to_chat_id": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "retry_after": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "migrate_to_chat_id": {
                "value": "ok."
            },
            "retry_after": {
                "value": "ok."
            }
        }
    },
    InputMediaPhoto: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "has_spoiler": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INPUT_MEDIA_PHOTO
                }
            },
            "media": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "has_spoiler": {
                "value": "ok."
            }
        }
    },
    InputMediaVideo: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "thumbnail": {
                "type_hint": Optional[Union[InputFile, str]],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "width": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "height": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "duration": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "supports_streaming": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "has_spoiler": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INPUT_MEDIA_VIDEO
                }
            },
            "media": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "width": {
                "value": "ok."
            },
            "height": {
                "value": "ok."
            },
            "duration": {
                "value": "ok."
            },
            "supports_streaming": {
                "value": "ok."
            },
            "has_spoiler": {
                "value": "ok."
            }
        }
    },
    InputMediaAnimation: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "thumbnail": {
                "type_hint": Optional[Union[InputFile, str]],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "width": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "height": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "duration": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "has_spoiler": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INPUT_MEDIA_ANIMATION
                }
            },
            "media": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "width": {
                "value": "ok."
            },
            "height": {
                "value": "ok."
            },
            "duration": {
                "value": "ok."
            },
            "has_spoiler": {
                "value": "ok."
            }
        }
    },
    InputMediaAudio: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "thumbnail": {
                "type_hint": Optional[Union[InputFile, str]],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "duration": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "performer": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "title": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INPUT_MEDIA_AUDIO
                }
            },
            "media": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "duration": {
                "value": "ok."
            },
            "performer": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            }
        }
    },
    InputMediaDocument: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "type_hint": str
            },
            "thumbnail": {
                "type_hint": Optional[Union[InputFile, str]],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "disable_content_type_detection": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INPUT_MEDIA_DOCUMENT
                }
            },
            "media": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "disable_content_type_detection": {
                "value": "ok."
            }
        }
    },
    MaskPosition: {
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
        "self_kwargs": {
            "point": {
                "value": "ok."
            },
            "x_shift": {
                "value": "ok."
            },
            "y_shift": {
                "value": "ok."
            },
            "scale": {
                "value": "ok."
            }
        }
    },
    Sticker: {
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
                "default_value": None
            },
            "emoji": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "set_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "premium_animation": {
                "type_hint": Optional[File],
                "default_value": None
            },
            "mask_position": {
                "type_hint": Optional[MaskPosition],
                "default_value": None
            },
            "custom_emoji_id": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "needs_repainting": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "type": {
                "value": "ok."
            },
            "width": {
                "value": "ok."
            },
            "height": {
                "value": "ok."
            },
            "is_animated": {
                "value": "ok."
            },
            "is_video": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            },
            "emoji": {
                "value": "ok."
            },
            "set_name": {
                "value": "ok."
            },
            "premium_animation": {
                "value": "ok."
            },
            "mask_position": {
                "value": "ok."
            },
            "custom_emoji_id": {
                "value": "ok."
            },
            "needs_repainting": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            }
        }
    },
    StickerSet: {
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
                "default_value": None
            }
        },
        "self_kwargs": {
            "name": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "sticker_type": {
                "value": "ok."
            },
            "is_animated": {
                "value": "ok."
            },
            "is_video": {
                "value": "ok."
            },
            "stickers": {
                "value": "ok."
            },
            "thumbnail": {
                "value": "ok."
            }
        }
    },
    InputSticker: {
        "has_dese": False,
        "init_kwargs": {
            "sticker": {
                "type_hint": Union[InputFile, str]
            },
            "emoji_list": {
                "type_hint": list[str]
            },
            "mask_position": {
                "type_hint": Optional[MaskPosition],
                "default_value": None
            },
            "keywords": {
                "type_hint": Optional[list[str]],
                "default_value": None
            }
        },
        "self_kwargs": {
            "sticker": {
                "value": "ok."
            },
            "emoji_list": {
                "value": "ok."
            },
            "mask_position": {
                "value": "ok."
            },
            "keywords": {
                "value": "ok."
            }
        }
    },
    InlineQuery: {
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
                "default_value": None
            },
            "location": {
                "type_hint": Optional[Location],
                "default_value": None
            }
        },
        "self_kwargs": {
            "id": {
                "value": "ok."
            },
            "from_user": {
                "value": "ok."
            },
            "query": {
                "value": "ok."
            },
            "offset": {
                "value": "ok."
            },
            "chat_type": {
                "value": "ok."
            },
            "location": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultsButton: {
        "has_dese": False,
        "init_kwargs": {
            "text": {
                "type_hint": str
            },
            "web_app": {
                "type_hint": Optional[WebAppInfo],
                "default_value": None
            },
            "start_parameter": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "text": {
                "value": "ok."
            },
            "web_app": {
                "value": "ok."
            },
            "start_parameter": {
                "value": "ok."
            }
        }
    },
    InputTextMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "message_text": {
                "type_hint": str
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "link_preview_options": {
                "type_hint": Optional[LinkPreviewOptions],
                "default_value": None
            }
        },
        "self_kwargs": {
            "message_text": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "entities": {
                "value": "ok."
            },
            "link_preview_options": {
                "value": "ok."
            }
        }
    },
    InputLocationMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "latitude": {
                "type_hint": float
            },
            "longitude": {
                "type_hint": float
            },
            "horizontal_accuracy": {
                "type_hint": Optional[float],
                "default_value": None
            },
            "live_period": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "heading": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "proximity_alert_radius": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "latitude": {
                "value": "ok."
            },
            "longitude": {
                "value": "ok."
            },
            "horizontal_accuracy": {
                "value": "ok."
            },
            "live_period": {
                "value": "ok."
            },
            "heading": {
                "value": "ok."
            },
            "proximity_alert_radius": {
                "value": "ok."
            }
        }
    },
    InputVenueMessageContent: {
        "has_dese": False,
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
                "default_value": None
            },
            "foursquare_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "google_place_id": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "google_place_type": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "latitude": {
                "value": "ok."
            },
            "longitude": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "address": {
                "value": "ok."
            },
            "foursquare_id": {
                "value": "ok."
            },
            "foursquare_type": {
                "value": "ok."
            },
            "google_place_id": {
                "value": "ok."
            },
            "google_place_type": {
                "value": "ok."
            }
        }
    },
    InputContactMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "phone_number": {
                "type_hint": str
            },
            "first_name": {
                "type_hint": str
            },
            "last_name": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "vcard": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "phone_number": {
                "value": "ok."
            },
            "first_name": {
                "value": "ok."
            },
            "last_name": {
                "value": "ok."
            },
            "vcard": {
                "value": "ok."
            }
        }
    },
    InputInvoiceMessageContent: {
        "has_dese": False,
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
                "default_value": None
            },
            "suggested_tip_amounts": {
                "type_hint": Optional[list[int]],
                "default_value": None
            },
            "provider_data": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "photo_url": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "photo_size": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "photo_width": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "photo_height": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "need_name": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "need_phone_number": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "need_email": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "need_shipping_address": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "send_phone_number_to_provider": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "send_email_to_provider": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "is_flexible": {
                "type_hint": Optional[bool],
                "default_value": None
            }
        },
        "self_kwargs": {
            "title": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "payload": {
                "value": "ok."
            },
            "provider_token": {
                "value": "ok."
            },
            "currency": {
                "value": "ok."
            },
            "prices": {
                "value": "ok."
            },
            "max_tip_amount": {
                "value": "ok."
            },
            "suggested_tip_amounts": {
                "value": "ok."
            },
            "provider_data": {
                "value": "ok."
            },
            "photo_url": {
                "value": "ok."
            },
            "photo_size": {
                "value": "ok."
            },
            "photo_width": {
                "value": "ok."
            },
            "photo_height": {
                "value": "ok."
            },
            "need_name": {
                "value": "ok."
            },
            "need_phone_number": {
                "value": "ok."
            },
            "need_email": {
                "value": "ok."
            },
            "need_shipping_address": {
                "value": "ok."
            },
            "send_phone_number_to_provider": {
                "value": "ok."
            },
            "send_email_to_provider": {
                "value": "ok."
            },
            "is_flexible": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultArticle: {
        "has_dese": False,
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
                "default_value": None
            },
            "url": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "hide_url": {
                "type_hint": Optional[bool],
                "default_value": None
            },
            "description": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_ARTICLE
                }
            },
            "id": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "url": {
                "value": "ok."
            },
            "hide_url": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "thumbnail_url": {
                "value": "ok."
            },
            "thumbnail_width": {
                "value": "ok."
            },
            "thumbnail_height": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultPhoto: {
        "has_dese": False,
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
                "default_value": None
            },
            "photo_height": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "title": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "description": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_PHOTO
                }
            },
            "id": {
                "value": "ok."
            },
            "photo_url": {
                "value": "ok."
            },
            "thumbnail_url": {
                "value": "ok."
            },
            "photo_width": {
                "value": "ok."
            },
            "photo_height": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultGif: {
        "has_dese": False,
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
                "default_value": None
            },
            "gif_height": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "gif_duration": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "thumbnail_mime_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "title": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_GIF
                }
            },
            "id": {
                "value": "ok."
            },
            "gif_url": {
                "value": "ok."
            },
            "thumbnail_url": {
                "value": "ok."
            },
            "gif_width": {
                "value": "ok."
            },
            "gif_height": {
                "value": "ok."
            },
            "gif_duration": {
                "value": "ok."
            },
            "thumbnail_mime_type": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultMpeg4Gif: {
        "has_dese": False,
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
                "default_value": None
            },
            "mpeg4_height": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "mpeg4_duration": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "thumbnail_mime_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "title": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_MPEG4_GIF
                }
            },
            "id": {
                "value": "ok."
            },
            "mpeg4_url": {
                "value": "ok."
            },
            "thumbnail_url": {
                "value": "ok."
            },
            "mpeg4_width": {
                "value": "ok."
            },
            "mpeg4_height": {
                "value": "ok."
            },
            "mpeg4_duration": {
                "value": "ok."
            },
            "thumbnail_mime_type": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultVideo: {
        "has_dese": False,
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
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "video_width": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "video_height": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "video_duration": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "description": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_VIDEO
                }
            },
            "id": {
                "value": "ok."
            },
            "video_url": {
                "value": "ok."
            },
            "mime_type": {
                "value": "ok."
            },
            "thumbnail_url": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "video_width": {
                "value": "ok."
            },
            "video_height": {
                "value": "ok."
            },
            "video_duration": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultAudio: {
        "has_dese": False,
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
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "performer": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "audio_duration": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_AUDIO
                }
            },
            "id": {
                "value": "ok."
            },
            "audio_url": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "performer": {
                "value": "ok."
            },
            "audio_duration": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultVoice: {
        "has_dese": False,
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
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "voice_duration": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_VOICE
                }
            },
            "id": {
                "value": "ok."
            },
            "voice_url": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "voice_duration": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultDocument: {
        "has_dese": False,
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
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "description": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_DOCUMENT
                }
            },
            "id": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "document_url": {
                "value": "ok."
            },
            "mime_type": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            },
            "thumbnail_url": {
                "value": "ok."
            },
            "thumbnail_width": {
                "value": "ok."
            },
            "thumbnail_height": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultLocation: {
        "has_dese": False,
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
                "default_value": None
            },
            "live_period": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "heading": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "proximity_alert_radius": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_LOCATION
                }
            },
            "id": {
                "value": "ok."
            },
            "latitude": {
                "value": "ok."
            },
            "longitude": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "horizontal_accuracy": {
                "value": "ok."
            },
            "live_period": {
                "value": "ok."
            },
            "heading": {
                "value": "ok."
            },
            "proximity_alert_radius": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            },
            "thumbnail_url": {
                "value": "ok."
            },
            "thumbnail_width": {
                "value": "ok."
            },
            "thumbnail_height": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultVenue: {
        "has_dese": False,
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
                "default_value": None
            },
            "foursquare_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "google_place_id": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "google_place_type": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_VENUE
                }
            },
            "id": {
                "value": "ok."
            },
            "latitude": {
                "value": "ok."
            },
            "longitude": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "address": {
                "value": "ok."
            },
            "foursquare_id": {
                "value": "ok."
            },
            "foursquare_type": {
                "value": "ok."
            },
            "google_place_id": {
                "value": "ok."
            },
            "google_place_type": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            },
            "thumbnail_url": {
                "value": "ok."
            },
            "thumbnail_width": {
                "value": "ok."
            },
            "thumbnail_height": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultContact: {
        "has_dese": False,
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
                "default_value": None
            },
            "vcard": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            },
            "thumbnail_url": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_CONTACT
                }
            },
            "id": {
                "value": "ok."
            },
            "phone_number": {
                "value": "ok."
            },
            "first_name": {
                "value": "ok."
            },
            "last_name": {
                "value": "ok."
            },
            "vcard": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            },
            "thumbnail_url": {
                "value": "ok."
            },
            "thumbnail_width": {
                "value": "ok."
            },
            "thumbnail_height": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultGame: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "game_short_name": {
                "type_hint": str
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_GAME
                }
            },
            "id": {
                "value": "ok."
            },
            "game_short_name": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultCachedPhoto: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "photo_file_id": {
                "type_hint": str
            },
            "title": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "description": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_CACHED_PHOTO
                }
            },
            "id": {
                "value": "ok."
            },
            "photo_file_id": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultCachedGif: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "gif_file_id": {
                "type_hint": str
            },
            "title": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_CACHED_GIF
                }
            },
            "id": {
                "value": "ok."
            },
            "gif_file_id": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultCachedMpeg4Gif: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "mpeg4_file_id": {
                "type_hint": str
            },
            "title": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_CACHED_MPEG4_GIF
                }
            },
            "id": {
                "value": "ok."
            },
            "mpeg4_file_id": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultCachedSticker: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "sticker_file_id": {
                "type_hint": str
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_CACHED_STICKER
                }
            },
            "id": {
                "value": "ok."
            },
            "sticker_file_id": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultCachedDocument: {
        "has_dese": False,
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
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_CACHED_DOCUMENT
                }
            },
            "id": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "document_file_id": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultCachedVideo: {
        "has_dese": False,
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
                "default_value": None
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_CACHED_VIDEO
                }
            },
            "id": {
                "value": "ok."
            },
            "video_file_id": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultCachedVoice: {
        "has_dese": False,
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
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_CACHED_VOICE
                }
            },
            "id": {
                "value": "ok."
            },
            "voice_file_id": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    InlineQueryResultCachedAudio: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "type_hint": str
            },
            "audio_file_id": {
                "type_hint": str
            },
            "caption": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "type_hint": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_INLINE_QUERY_RESULT_CACHED_AUDIO
                }
            },
            "id": {
                "value": "ok."
            },
            "audio_file_id": {
                "value": "ok."
            },
            "caption": {
                "value": "ok."
            },
            "parse_mode": {
                "value": "ok."
            },
            "caption_entities": {
                "value": "ok."
            },
            "reply_markup": {
                "value": "ok."
            },
            "input_message_content": {
                "value": "ok."
            }
        }
    },
    ChosenInlineResult: {
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
                "default_value": None
            },
            "inline_message_id": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "result_id": {
                "value": "ok."
            },
            "from_user": {
                "value": "ok."
            },
            "query": {
                "value": "ok."
            },
            "location": {
                "value": "ok."
            },
            "inline_message_id": {
                "value": "ok."
            }
        }
    },
    SentWebAppMessage: {
        "has_dese": True,
        "dese_kwargs": {
            "inline_message_id": None
        },
        "init_kwargs": {
            "inline_message_id": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "inline_message_id": {
                "value": "ok."
            }
        }
    },
    Invoice: {
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
        "self_kwargs": {
            "title": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "start_parameter": {
                "value": "ok."
            },
            "currency": {
                "value": "ok."
            },
            "total_amount": {
                "value": "ok."
            }
        }
    },
    ShippingAddress: {
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
        "self_kwargs": {
            "country_code": {
                "value": "ok."
            },
            "state": {
                "value": "ok."
            },
            "city": {
                "value": "ok."
            },
            "street_line1": {
                "value": "ok."
            },
            "street_line2": {
                "value": "ok."
            },
            "post_code": {
                "value": "ok."
            }
        }
    },
    OrderInfo: {
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
                "default_value": None
            },
            "phone_number": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "email": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "shipping_address": {
                "type_hint": Optional[ShippingAddress],
                "default_value": None
            }
        },
        "self_kwargs": {
            "name": {
                "value": "ok."
            },
            "phone_number": {
                "value": "ok."
            },
            "email": {
                "value": "ok."
            },
            "shipping_address": {
                "value": "ok."
            }
        }
    },
    ShippingOption: {
        "has_dese": False,
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
        "self_kwargs": {
            "id": {
                "value": "ok."
            },
            "title": {
                "value": "ok."
            },
            "prices": {
                "value": "ok."
            }
        }
    },
    SuccessfulPayment: {
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
                "default_value": None
            },
            "order_info": {
                "type_hint": Optional[OrderInfo],
                "default_value": None
            }
        },
        "self_kwargs": {
            "currency": {
                "value": "ok."
            },
            "total_amount": {
                "value": "ok."
            },
            "invoice_payload": {
                "value": "ok."
            },
            "telegram_payment_charge_id": {
                "value": "ok."
            },
            "provider_payment_charge_id": {
                "value": "ok."
            },
            "shipping_option_id": {
                "value": "ok."
            },
            "order_info": {
                "value": "ok."
            }
        }
    },
    ShippingQuery: {
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
        "self_kwargs": {
            "id": {
                "value": "ok."
            },
            "from_user": {
                "value": "ok."
            },
            "invoice_payload": {
                "value": "ok."
            },
            "shipping_address": {
                "value": "ok."
            }
        }
    },
    PreCheckoutQuery: {
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
                "default_value": None
            },
            "order_info": {
                "type_hint": Optional[OrderInfo],
                "default_value": None
            }
        },
        "self_kwargs": {
            "id": {
                "value": "ok."
            },
            "from_user": {
                "value": "ok."
            },
            "currency": {
                "value": "ok."
            },
            "total_amount": {
                "value": "ok."
            },
            "invoice_payload": {
                "value": "ok."
            },
            "shipping_option_id": {
                "value": "ok."
            },
            "order_info": {
                "value": "ok."
            }
        }
    },
    PassportFile: {
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
        "self_kwargs": {
            "file_id": {
                "value": "ok."
            },
            "file_unique_id": {
                "value": "ok."
            },
            "file_size": {
                "value": "ok."
            },
            "file_date": {
                "value": "ok."
            }
        }
    },
    EncryptedPassportElement: {
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
                "default_value": None
            },
            "phone_number": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "email": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "files": {
                "type_hint": Optional[list[PassportFile]],
                "default_value": None
            },
            "front_side": {
                "type_hint": Optional[PassportFile],
                "default_value": None
            },
            "reverse_side": {
                "type_hint": Optional[PassportFile],
                "default_value": None
            },
            "selfie": {
                "type_hint": Optional[PassportFile],
                "default_value": None
            },
            "translation": {
                "type_hint": Optional[list[PassportFile]],
                "default_value": None
            }
        },
        "self_kwargs": {
            "type": {
                "value": "ok."
            },
            "hash": {
                "value": "ok."
            },
            "data": {
                "value": "ok."
            },
            "phone_number": {
                "value": "ok."
            },
            "email": {
                "value": "ok."
            },
            "files": {
                "value": "ok."
            },
            "front_side": {
                "value": "ok."
            },
            "reverse_side": {
                "value": "ok."
            },
            "selfie": {
                "value": "ok."
            },
            "translation": {
                "value": "ok."
            }
        }
    },
    EncryptedCredentials: {
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
        "self_kwargs": {
            "data": {
                "value": "ok."
            },
            "hash": {
                "value": "ok."
            },
            "secret": {
                "value": "ok."
            }
        }
    },
    PassportData: {
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
        "self_kwargs": {
            "data": {
                "value": "ok."
            },
            "credentials": {
                "value": "ok."
            }
        }
    },
    PassportElementErrorDataField: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal['personal_details', 'passport', 'driver_license', 'identity_card', 'internal_passport', 'address']
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_PASSPORT_ELEMENT_ERROR_DATA_FIELD
                }
            },
            "type": {
                "value": "ok."
            },
            "field_name": {
                "value": "ok."
            },
            "data_hash": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            }
        }
    },
    PassportElementErrorFrontSide: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal['passport', 'driver_license', 'identity_card', 'internal_passport']
            },
            "file_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_PASSPORT_ELEMENT_ERROR_FRONT_SIDE
                }
            },
            "type": {
                "value": "ok."
            },
            "file_hash": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            }
        }
    },
    PassportElementErrorReverseSide: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_PASSPORT_ELEMENT_ERROR_REVERSE_SIDE
                }
            },
            "type": {
                "value": "ok."
            },
            "file_hash": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            }
        }
    },
    PassportElementErrorSelfie: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal['passport', 'driver_license', 'identity_card', 'internal_passport']
            },
            "file_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_PASSPORT_ELEMENT_ERROR_SELFIE
                }
            },
            "type": {
                "value": "ok."
            },
            "file_hash": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            }
        }
    },
    PassportElementErrorFile: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal['utility_bill', 'bank_statement', 'rental_agreement', 'passport_registration', 'temporary_registration']
            },
            "file_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_PASSPORT_ELEMENT_ERROR_FILE
                }
            },
            "type": {
                "value": "ok."
            },
            "file_hash": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            }
        }
    },
    PassportElementErrorFiles: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal['utility_bill', 'bank_statement', 'rental_agreement', 'passport_registration', 'temporary_registration']
            },
            "file_hashes": {
                "type_hint": list[str]
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_PASSPORT_ELEMENT_ERROR_FILES
                }
            },
            "type": {
                "value": "ok."
            },
            "file_hashes": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            }
        }
    },
    PassportElementErrorTranslationFile: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal['passport', 'driver_license', 'identity_card', 'internal_passport', 'utility_bill', 'bank_statement', 'rental_agreement', 'passport_registration', 'temporary_registration']
            },
            "file_hash": {
                "type_hint": str
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILE
                }
            },
            "type": {
                "value": "ok."
            },
            "file_hash": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            }
        }
    },
    PassportElementErrorTranslationFiles: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal['passport', 'driver_license', 'identity_card', 'internal_passport', 'utility_bill', 'bank_statement', 'rental_agreement', 'passport_registration', 'temporary_registration']
            },
            "file_hashes": {
                "type_hint": list[str]
            },
            "message": {
                "type_hint": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILES
                }
            },
            "type": {
                "value": "ok."
            },
            "file_hashes": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            }
        }
    },
    PassportElementErrorUnspecified: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_PASSPORT_ELEMENT_ERROR_UNSPECIFIED
                }
            },
            "type": {
                "value": "ok."
            },
            "element_hash": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            }
        }
    },
    Game: {
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
                "default_value": None
            },
            "text_entities": {
                "type_hint": Optional[list[MessageEntity]],
                "default_value": None
            },
            "animation": {
                "type_hint": Optional[Animation],
                "default_value": None
            }
        },
        "self_kwargs": {
            "title": {
                "value": "ok."
            },
            "description": {
                "value": "ok."
            },
            "photo": {
                "value": "ok."
            },
            "text": {
                "value": "ok."
            },
            "text_entities": {
                "value": "ok."
            },
            "animation": {
                "value": "ok."
            }
        }
    },
    GameHighScore: {
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
        "self_kwargs": {
            "position": {
                "value": "ok."
            },
            "user": {
                "value": "ok."
            },
            "score": {
                "value": "ok."
            }
        }
    },
    GiveawayCreated: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {},
        "self_kwargs": {}
    },
    GiveawayWinners: {
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
                "default_value": None
            },
            "premium_subscription_month_count": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "unclaimed_prize_count": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "only_new_members": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "was_refunded": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "prize_description": {
                "type_hint": Optional[str],
                "default_value": None
            }
        },
        "self_kwargs": {
            "chat": {
                "value": "ok."
            },
            "giveaway_message_id": {
                "value": "ok."
            },
            "winners_selection_date": {
                "value": "ok."
            },
            "winner_count": {
                "value": "ok."
            },
            "winners": {
                "value": "ok."
            },
            "additional_chat_count": {
                "value": "ok."
            },
            "premium_subscription_month_count": {
                "value": "ok."
            },
            "unclaimed_prize_count": {
                "value": "ok."
            },
            "only_new_members": {
                "value": "ok."
            },
            "was_refunded": {
                "value": "ok."
            },
            "prize_description": {
                "value": "ok."
            }
        }
    },
    GiveawayCompleted: {
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
                "default_value": None
            },
            "giveaway_message": {
                "type_hint": Optional[Message],
                "default_value": None
            }
        },
        "self_kwargs": {
            "winner_count": {
                "value": "ok."
            },
            "unclaimed_prize_count": {
                "value": "ok."
            },
            "giveaway_message": {
                "value": "ok."
            }
        }
    },
    Giveaway: {
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
                "default_value": None
            },
            "has_public_winners": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "prize_description": {
                "type_hint": Optional[str],
                "default_value": None
            },
            "country_codes": {
                "type_hint": Optional[list[str]],
                "default_value": None
            },
            "premium_subscription_month_count": {
                "type_hint": Optional[int],
                "default_value": None
            }
        },
        "self_kwargs": {
            "chats": {
                "value": "ok."
            },
            "winners_selection_date": {
                "value": "ok."
            },
            "winner_count": {
                "value": "ok."
            },
            "only_new_members": {
                "value": "ok."
            },
            "has_public_winners": {
                "value": "ok."
            },
            "prize_description": {
                "value": "ok."
            },
            "country_codes": {
                "value": "ok."
            },
            "premium_subscription_month_count": {
                "value": "ok."
            }
        }
    },
    MessageOriginUser: {
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_MESSAGE_ORIGIN_USER
                }
            },
            "date": {
                "value": "ok."
            },
            "sender_user": {
                "value": "ok."
            }
        }
    },
    MessageOriginHiddenUser: {
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_MESSAGE_ORIGIN_HIDDEN_USER
                }
            },
            "date": {
                "value": "ok."
            },
            "sender_user_name": {
                "value": "ok."
            }
        }
    },
    MessageOriginChat: {
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
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_MESSAGE_ORIGIN_CHAT
                }
            },
            "date": {
                "value": "ok."
            },
            "sender_chat": {
                "value": "ok."
            },
            "author_signature": {
                "value": "ok."
            }
        }
    },
    MessageOriginChannel: {
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
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "value": DEFAULT_MESSAGE_ORIGIN_CHANNEL
                }
            },
            "date": {
                "value": "ok."
            },
            "chat": {
                "value": "ok."
            },
            "message_id": {
                "value": "ok."
            },
            "author_signature": {
                "value": "ok."
            }
        }
    },
    ExternalReplyInfo: {
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
                "default_value": None
            },
            "message_id": {
                "type_hint": Optional[int],
                "default_value": None
            },
            "link_preview_options": {
                "type_hint": Optional[LinkPreviewOptions],
                "default_value": None
            },
            "animation": {
                "type_hint": Optional[Animation],
                "default_value": None
            },
            "audio": {
                "type_hint": Optional[Audio],
                "default_value": None
            },
            "document": {
                "type_hint": Optional[Document],
                "default_value": None
            },
            "photo": {
                "type_hint": Optional[list[PhotoSize]],
                "default_value": None
            },
            "sticker": {
                "type_hint": Optional[Sticker],
                "default_value": None
            },
            "story": {
                "type_hint": Optional[Story],
                "default_value": None
            },
            "video": {
                "type_hint": Optional[Video],
                "default_value": None
            },
            "video_note": {
                "type_hint": Optional[VideoNote],
                "default_value": None
            },
            "voice": {
                "type_hint": Optional[Voice],
                "default_value": None
            },
            "has_media_spoiler": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            },
            "contact": {
                "type_hint": Optional[Contact],
                "default_value": None
            },
            "dice": {
                "type_hint": Optional[Dice],
                "default_value": None
            },
            "game": {
                "type_hint": Optional[Game],
                "default_value": None
            },
            "giveaway": {
                "type_hint": Optional[Giveaway],
                "default_value": None
            },
            "giveaway_winners": {
                "type_hint": Optional[GiveawayWinners],
                "default_value": None
            },
            "invoice": {
                "type_hint": Optional[Invoice],
                "default_value": None
            },
            "location": {
                "type_hint": Optional[Location],
                "default_value": None
            },
            "poll": {
                "type_hint": Optional[Poll],
                "default_value": None
            },
            "venue": {
                "type_hint": Optional[Venue],
                "default_value": None
            }
        },
        "self_kwargs": {
            "origin": {
                "value": "ok."
            },
            "chat": {
                "value": "ok."
            },
            "message_id": {
                "value": "ok."
            },
            "link_preview_options": {
                "value": "ok."
            },
            "animation": {
                "value": "ok."
            },
            "audio": {
                "value": "ok."
            },
            "document": {
                "value": "ok."
            },
            "photo": {
                "value": "ok."
            },
            "sticker": {
                "value": "ok."
            },
            "story": {
                "value": "ok."
            },
            "video": {
                "value": "ok."
            },
            "video_note": {
                "value": "ok."
            },
            "voice": {
                "value": "ok."
            },
            "has_media_spoiler": {
                "value": "ok."
            },
            "contact": {
                "value": "ok."
            },
            "dice": {
                "value": "ok."
            },
            "game": {
                "value": "ok."
            },
            "giveaway": {
                "value": "ok."
            },
            "giveaway_winners": {
                "value": "ok."
            },
            "invoice": {
                "value": "ok."
            },
            "location": {
                "value": "ok."
            },
            "poll": {
                "value": "ok."
            },
            "venue": {
                "value": "ok."
            }
        }
    },
    ChatBoostSourcePremium: {
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_CHAT_BOOST_SOURCE_PREMIUM
                }
            },
            "user": {
                "value": "ok."
            }
        }
    },
    ChatBoostSourceGiftCode: {
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_CHAT_BOOST_SOURCE_GIFT_CODE
                }
            },
            "user": {
                "value": "ok."
            }
        }
    },
    ChatBoostSourceGiveaway: {
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
                "default_value": None
            },
            "is_unclaimed": {
                "type_hint": Optional[Literal[True]],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "value": DEFAULT_CHAT_BOOST_SOURCE_GIVEAWAY
                }
            },
            "giveaway_message_id": {
                "value": "ok."
            },
            "user": {
                "value": "ok."
            },
            "is_unclaimed": {
                "value": "ok."
            }
        }
    },
    ChatBoost: {
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
        "self_kwargs": {
            "boost_id": {
                "value": "ok."
            },
            "add_date": {
                "value": "ok."
            },
            "expiration_date": {
                "value": "ok."
            },
            "source": {
                "value": "ok."
            }
        }
    },
    UserChatBoosts: {
        "has_dese": True,
        "dese_kwargs": {
            "boosts": list[ChatBoost]
        },
        "init_kwargs": {
            "boosts": {
                "type_hint": list[ChatBoost]
            }
        },
        "self_kwargs": {
            "boosts": {
                "value": "ok."
            }
        }
    },
    ChatBoostUpdated: {
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
        "self_kwargs": {
            "chat": {
                "value": "ok."
            },
            "boost": {
                "value": "ok."
            }
        }
    },
    ChatBoostRemoved: {
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
        "self_kwargs": {
            "chat": {
                "value": "ok."
            },
            "boost_id": {
                "value": "ok."
            },
            "remove_date": {
                "value": "ok."
            },
            "source": {
                "value": "ok."
            }
        }
    },
    Update: {
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
                "default_value": None
            },
            "edited_message": {
                "type_hint": Optional[Message],
                "default_value": None
            },
            "channel_post": {
                "type_hint": Optional[Message],
                "default_value": None
            },
            "edited_channel_post": {
                "type_hint": Optional[Message],
                "default_value": None
            },
            "message_reaction": {
                "type_hint": Optional[MessageReactionUpdated],
                "default_value": None
            },
            "message_reaction_count": {
                "type_hint": Optional[MessageReactionCountUpdated],
                "default_value": None
            },
            "inline_query": {
                "type_hint": Optional[InlineQuery],
                "default_value": None
            },
            "chosen_inline_result": {
                "type_hint": Optional[ChosenInlineResult],
                "default_value": None
            },
            "callback_query": {
                "type_hint": Optional[CallbackQuery],
                "default_value": None
            },
            "shipping_query": {
                "type_hint": Optional[ShippingQuery],
                "default_value": None
            },
            "pre_checkout_query": {
                "type_hint": Optional[PreCheckoutQuery],
                "default_value": None
            },
            "poll": {
                "type_hint": Optional[Poll],
                "default_value": None
            },
            "poll_answer": {
                "type_hint": Optional[PollAnswer],
                "default_value": None
            },
            "my_chat_member": {
                "type_hint": Optional[ChatMemberUpdated],
                "default_value": None
            },
            "chat_member": {
                "type_hint": Optional[ChatMemberUpdated],
                "default_value": None
            },
            "chat_join_request": {
                "type_hint": Optional[ChatJoinRequest],
                "default_value": None
            },
            "chat_boost": {
                "type_hint": Optional[ChatBoostUpdated],
                "default_value": None
            },
            "removed_chat_boost": {
                "type_hint": Optional[ChatBoostRemoved],
                "default_value": None
            }
        },
        "self_kwargs": {
            "warning": {},
            "update_id": {
                "value": "ok."
            },
            "message": {
                "value": "ok."
            },
            "edited_message": {
                "value": "ok."
            },
            "channel_post": {
                "value": "ok."
            },
            "edited_channel_post": {
                "value": "ok."
            },
            "message_reaction": {
                "value": "ok."
            },
            "message_reaction_count": {
                "value": "ok."
            },
            "inline_query": {
                "value": "ok."
            },
            "chosen_inline_result": {
                "value": "ok."
            },
            "callback_query": {
                "value": "ok."
            },
            "shipping_query": {
                "value": "ok."
            },
            "pre_checkout_query": {
                "value": "ok."
            },
            "poll": {
                "value": "ok."
            },
            "poll_answer": {
                "value": "ok."
            },
            "my_chat_member": {
                "value": "ok."
            },
            "chat_member": {
                "value": "ok."
            },
            "chat_join_request": {
                "value": "ok."
            },
            "chat_boost": {
                "value": "ok."
            },
            "removed_chat_boost": {
                "value": "ok."
            }
        }
    }
}

from inspect import isclass

from tglib.logger import get_logger
logger = get_logger('TypesChecker')

logger.setLevel(10)

for k in TYPES:

    if not isclass(k):
        raise TypeError(
            f'Invalid key {k!r}: expected a type, got {k.__class__.__name__}.'
        )
    if not issubclass(k, TelegramType):
        raise TypeError(
            f'{k.__name__} is not a subclass of TelegramType.'
        )
    if k.__name__ in IGNORE:
        continue

    if TYPES[k]['has_dese']:
        has_dese = True
        for arg in TYPES[k]['dese_kwargs']:
            if TYPES[k]['dese_kwargs'][arg] is None:
                continue
            if arg not in TYPES[k]['init_kwargs']:
                logger.warning('%s, %s: %s', k.__name__, arg, 'not in init_kwargs')
            else:
                init_arg = TYPES[k]['init_kwargs'][arg]
                if init_arg is not None and 'type_hint' in init_arg:
                    init_type_hint = init_arg['type_hint']
                    dese_type_hint = TYPES[k]['dese_kwargs'][arg]

                    if type(dese_type_hint) is _UnionGenericAlias and type(init_type_hint) is _UnionGenericAlias:
                        if type(None) in dese_type_hint.__dict__['__args__']:
                            if not type(None) in init_type_hint.__dict__['__args__']:
                                raise ValueError(f'Argument {arg!r} should be Optional in {k.__name__}.__init__(), got {dese_type_hint}')
                            else:
                                logger.debug('{} was optional in {}.dese()'.format(dese_type_hint, k.__name__))

                        if type(None) not in dese_type_hint.__dict__['__args__'] and type(None) in init_type_hint.__dict__['__args__']:
                            dese_type_hint = Optional[dese_type_hint]

                    elif not type(dese_type_hint) is _UnionGenericAlias and type(init_type_hint) is _UnionGenericAlias:
                        if type(None) in init_type_hint.__dict__['__args__']:
                            dese_type_hint = Optional[dese_type_hint]

                    if dese_type_hint != init_type_hint:
                        raise ValueError(init_type_hint, dese_type_hint, k.__name__)

            if arg not in TYPES[k]['self_kwargs']:
                if (
                    'warning' in TYPES[k]['self_kwargs']
                    and arg in TYPES[k]['self_kwargs']['warning']
                ):
                    continue
                logger.warning('%s, %s: %s', k.__name__, arg, 'not in self_kwargs')
    else:
        has_dese = False

    for arg in TYPES[k]['init_kwargs']:
        if has_dese and arg not in TYPES[k]['dese_kwargs']:
            logger.warning('%s, %s: %s', k.__name__, arg, 'not in dese_kwargs')
        if arg not in TYPES[k]['self_kwargs']:
            if (
                'warning' in TYPES[k]['self_kwargs']
                and arg in TYPES[k]['self_kwargs']['warning']
            ):
                continue
            logger.warning('%s, %s: %s', k.__name__, arg, 'not in self_kwargs')

    for arg in TYPES[k]['self_kwargs']:
        if arg == 'warning':
            continue
        if has_dese and arg not in TYPES[k]['dese_kwargs']:
            logger.warning('%s, %s: %s', k.__name__, arg, 'not in dese_kwargs')
        if arg not in TYPES[k]['init_kwargs']:
            logger.warning('%s, %s: %s', k.__name__, arg, 'not in init_kwargs')
