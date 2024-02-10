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
        "self_kwargs": {
            "can_send_messages": {
                "default": "ok."
            },
            "can_send_audios": {
                "default": "ok."
            },
            "can_send_documents": {
                "default": "ok."
            },
            "can_send_photos": {
                "default": "ok."
            },
            "can_send_videos": {
                "default": "ok."
            },
            "can_send_video_notes": {
                "default": "ok."
            },
            "can_send_voice_notes": {
                "default": "ok."
            },
            "can_send_polls": {
                "default": "ok."
            },
            "can_send_other_messages": {
                "default": "ok."
            },
            "can_add_web_page_previews": {
                "default": "ok."
            },
            "can_change_info": {
                "default": "ok."
            },
            "can_invite_users": {
                "default": "ok."
            },
            "can_pin_messages": {
                "default": "ok."
            },
            "can_manage_topics": {
                "default": "ok."
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
            "can_post_stories": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_edit_stories": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_delete_stories": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_manage_topics": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {
            "is_anonymous": {
                "default": "ok."
            },
            "can_manage_chat": {
                "default": "ok."
            },
            "can_delete_messages": {
                "default": "ok."
            },
            "can_manage_video_chats": {
                "default": "ok."
            },
            "can_restrict_members": {
                "default": "ok."
            },
            "can_promote_members": {
                "default": "ok."
            },
            "can_change_info": {
                "default": "ok."
            },
            "can_invite_users": {
                "default": "ok."
            },
            "can_post_messages": {
                "default": "ok."
            },
            "can_edit_messages": {
                "default": "ok."
            },
            "can_pin_messages": {
                "default": "ok."
            },
            "can_post_stories": {
                "default": "ok."
            },
            "can_edit_stories": {
                "default": "ok."
            },
            "can_delete_stories": {
                "default": "ok."
            },
            "can_manage_topics": {
                "default": "ok."
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
        "self_kwargs": {
            "query": {
                "default": "ok."
            },
            "allow_user_chats": {
                "default": "ok."
            },
            "allow_bot_chats": {
                "default": "ok."
            },
            "allow_group_chats": {
                "default": "ok."
            },
            "allow_channel_chats": {
                "default": "ok."
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
                "default": None
            },
            "hide_name": {
                "type_hint": bool,
                "default": False
            }
        },
        "self_kwargs": {
            "path": {
                "default": "ok."
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
        "self_kwargs": {
            "url": {
                "default": "ok."
            },
            "forward_text": {
                "default": "ok."
            },
            "bot_username": {
                "default": "ok."
            },
            "request_write_access": {
                "default": "ok."
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
                "default": "ok."
            },
            "amount": {
                "default": "ok."
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
        "self_kwargs": {
            "is_disabled": {
                "default": "ok."
            },
            "url": {
                "default": "ok."
            },
            "prefer_small_media": {
                "default": "ok."
            },
            "prefer_large_media": {
                "default": "ok."
            },
            "show_above_text": {
                "default": "ok."
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
        "self_kwargs": {
            "id": {
                "default": "ok."
            },
            "is_bot": {
                "default": "ok."
            },
            "first_name": {
                "default": "ok."
            },
            "last_name": {
                "default": "ok."
            },
            "username": {
                "default": "ok."
            },
            "language_code": {
                "default": "ok."
            },
            "is_premium": {
                "default": "ok."
            },
            "added_to_attachment_menu": {
                "default": "ok."
            },
            "can_join_groups": {
                "default": "ok."
            },
            "can_read_all_group_messages": {
                "default": "ok."
            },
            "supports_inline_queries": {
                "default": "ok."
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
        "self_kwargs": {
            "type": {
                "default": "ok."
            },
            "offset": {
                "default": "ok."
            },
            "length": {
                "default": "ok."
            },
            "url": {
                "default": "ok."
            },
            "user": {
                "default": "ok."
            },
            "language": {
                "default": "ok."
            },
            "custom_emoji_id": {
                "default": "ok."
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
                "default": None
            },
            "is_manual": {
                "type_hint": Optional[Literal[True]],
                "default": None
            }
        },
        "self_kwargs": {
            "text": {
                "default": "ok."
            },
            "position": {
                "default": "ok."
            },
            "entities": {
                "default": "ok."
            },
            "is_manual": {
                "default": "ok."
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
        "self_kwargs": {
            "message_id": {
                "default": "ok."
            },
            "chat_id": {
                "default": "ok."
            },
            "allow_sending_without_reply": {
                "default": "ok."
            },
            "quote": {
                "default": "ok."
            },
            "quote_parse_mode": {
                "default": "ok."
            },
            "quote_entities": {
                "default": "ok."
            },
            "quote_position": {
                "default": "ok."
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
                "default": 0
            }
        },
        "self_kwargs": {
            "chat": {
                "value": "ok.",
                "type_hint": Chat
            },
            "message_id": {
                "value": "ok.",
                "type_hint": int
            },
            "date": {
                "value": "ok.",
                "type_hint": int
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
                "default": None
            },
            "from_user": {
                "default": None
            },
            "sender_chat": {
                "default": None
            },
            "forward_origin": {
                "default": None
            },
            "is_topic_message": {
                "default": None
            },
            "is_automatic_forward": {
                "default": None
            },
            "reply_to_message": {
                "default": None
            },
            "external_reply": {
                "default": None
            },
            "quote": {
                "default": None
            },
            "via_bot": {
                "default": None
            },
            "edit_date": {
                "default": None
            },
            "has_protected_content": {
                "default": None
            },
            "media_group_id": {
                "default": None
            },
            "author_signature": {
                "default": None
            },
            "text": {
                "default": None
            },
            "entities": {
                "default": None
            },
            "link_preview_options": {
                "default": None
            },
            "animation": {
                "default": None
            },
            "audio": {
                "default": None
            },
            "document": {
                "default": None
            },
            "photo": {
                "default": None
            },
            "sticker": {
                "default": None
            },
            "story": {
                "default": None
            },
            "video": {
                "default": None
            },
            "video_note": {
                "default": None
            },
            "voice": {
                "default": None
            },
            "caption": {
                "default": None
            },
            "caption_entities": {
                "default": None
            },
            "has_media_spoiler": {
                "default": None
            },
            "contact": {
                "default": None
            },
            "dice": {
                "default": None
            },
            "game": {
                "default": None
            },
            "poll": {
                "default": None
            },
            "venue": {
                "default": None
            },
            "location": {
                "default": None
            },
            "new_chat_members": {
                "default": None
            },
            "left_chat_member": {
                "default": None
            },
            "new_chat_title": {
                "default": None
            },
            "new_chat_photo": {
                "default": None
            },
            "delete_chat_photo": {
                "default": None
            },
            "group_chat_created": {
                "default": None
            },
            "supergroup_chat_created": {
                "default": None
            },
            "channel_chat_created": {
                "default": None
            },
            "message_auto_delete_timer_changed": {
                "default": None
            },
            "migrate_to_chat_id": {
                "default": None
            },
            "migrate_from_chat_id": {
                "default": None
            },
            "pinned_message": {
                "default": None
            },
            "invoice": {
                "default": None
            },
            "successful_payment": {
                "default": None
            },
            "users_shared": {
                "default": None
            },
            "chat_shared": {
                "default": None
            },
            "connected_website": {
                "default": None
            },
            "write_access_allowed": {
                "default": None
            },
            "passport_data": {
                "default": None
            },
            "proximity_alert_triggered": {
                "default": None
            },
            "forum_topic_created": {
                "default": None
            },
            "forum_topic_edited": {
                "default": None
            },
            "forum_topic_closed": {
                "default": None
            },
            "forum_topic_reopened": {
                "default": None
            },
            "general_forum_topic_hidden": {
                "default": None
            },
            "general_forum_topic_unhidden": {
                "default": None
            },
            "giveaway_created": {
                "default": None
            },
            "giveaway": {
                "default": None
            },
            "giveaway_winners": {
                "default": None
            },
            "giveaway_completed": {
                "default": None
            },
            "video_chat_scheduled": {
                "default": None
            },
            "video_chat_started": {
                "default": None
            },
            "video_chat_ended": {
                "default": None
            },
            "video_chat_participants_invited": {
                "default": None
            },
            "web_app_data": {
                "default": None
            },
            "reply_markup": {
                "default": None
            }
        },
        "self_kwargs": {
            "warning": {
                "text": {
                    "default": "text or str() # If not text, it's str() instead of None",
                    "type_hint": str
                }
            },
            "message_id": {
                "value": "ok.",
                "type_hint": int
            },
            "date": {
                "value": "ok.",
                "type_hint": int
            },
            "chat": {
                "value": "ok.",
                "type_hint": Chat
            },
            "message_thread_id": {
                "value": "ok.",
                "type_hint": Optional[int]
            },
            "from_user": {
                "value": "ok.",
                "type_hint": Optional[User]
            },
            "sender_chat": {
                "value": "ok.",
                "type_hint": Optional[Chat]
            },
            "forward_origin": {
                "value": "ok.",
                "type_hint": Optional[MessageOrigin]
            },
            "is_topic_message": {
                "value": "ok.",
                "type_hint": Optional[Literal[True]]
            },
            "is_automatic_forward": {
                "value": "ok.",
                "type_hint": Optional[Literal[True]]
            },
            "reply_to_message": {
                "value": "ok.",
                "type_hint": Optional[Message]
            },
            "external_reply": {
                "value": "ok.",
                "type_hint": Optional[ExternalReplyInfo]
            },
            "quote": {
                "value": "ok.",
                "type_hint": Optional[TextQuote]
            },
            "via_bot": {
                "value": "ok.",
                "type_hint": Optional[User]
            },
            "edit_date": {
                "value": "ok.",
                "type_hint": Optional[int]
            },
            "has_protected_content": {
                "value": "ok.",
                "type_hint": Optional[Literal[True]]
            },
            "media_group_id": {
                "value": "ok.",
                "type_hint": Optional[str]
            },
            "author_signature": {
                "value": "ok.",
                "type_hint": Optional[str]
            },
            "entities": {
                "value": "ok.",
                "type_hint": Optional[list[MessageEntity]]
            },
            "link_preview_options": {
                "value": "ok.",
                "type_hint": Optional[LinkPreviewOptions]
            },
            "animation": {
                "value": "ok.",
                "type_hint": Optional[Animation]
            },
            "audio": {
                "value": "ok.",
                "type_hint": Optional[Audio]
            },
            "document": {
                "value": "ok.",
                "type_hint": Optional[Document]
            },
            "photo": {
                "value": "ok.",
                "type_hint": Optional[list[PhotoSize]]
            },
            "sticker": {
                "value": "ok.",
                "type_hint": Optional[Sticker]
            },
            "story": {
                "value": "ok.",
                "type_hint": Optional[Story]
            },
            "video": {
                "value": "ok.",
                "type_hint": Optional[Video]
            },
            "video_note": {
                "value": "ok.",
                "type_hint": Optional[VideoNote]
            },
            "voice": {
                "value": "ok.",
                "type_hint": Optional[Voice]
            },
            "caption": {
                "value": "ok.",
                "type_hint": Optional[str]
            },
            "caption_entities": {
                "value": "ok.",
                "type_hint": Optional[list[MessageEntity]]
            },
            "has_media_spoiler": {
                "value": "ok.",
                "type_hint": Optional[Literal[True]]
            },
            "contact": {
                "value": "ok.",
                "type_hint": Optional[Contact]
            },
            "dice": {
                "value": "ok.",
                "type_hint": Optional[Dice]
            },
            "game": {
                "value": "ok.",
                "type_hint": Optional[Game]
            },
            "poll": {
                "value": "ok.",
                "type_hint": Optional[Poll]
            },
            "venue": {
                "value": "ok.",
                "type_hint": Optional[Venue]
            },
            "location": {
                "value": "ok.",
                "type_hint": Optional[Location]
            },
            "new_chat_members": {
                "value": "ok.",
                "type_hint": Optional[list[User]]
            },
            "left_chat_member": {
                "value": "ok.",
                "type_hint": Optional[User]
            },
            "new_chat_title": {
                "value": "ok.",
                "type_hint": Optional[str]
            },
            "new_chat_photo": {
                "value": "ok.",
                "type_hint": Optional[list[PhotoSize]]
            },
            "delete_chat_photo": {
                "value": "ok.",
                "type_hint": Optional[Literal[True]]
            },
            "group_chat_created": {
                "value": "ok.",
                "type_hint": Optional[Literal[True]]
            },
            "supergroup_chat_created": {
                "value": "ok.",
                "type_hint": Optional[Literal[True]]
            },
            "channel_chat_created": {
                "value": "ok.",
                "type_hint": Optional[Literal[True]]
            },
            "message_auto_delete_timer_changed": {
                "value": "ok.",
                "type_hint": Optional[MessageAutoDeleteTimerChanged]
            },
            "migrate_to_chat_id": {
                "value": "ok.",
                "type_hint": Optional[int]
            },
            "migrate_from_chat_id": {
                "value": "ok.",
                "type_hint": Optional[int]
            },
            "pinned_message": {
                "value": "ok.",
                "type_hint": Optional[MaybeInaccessibleMessage]
            },
            "invoice": {
                "value": "ok.",
                "type_hint": Optional[Invoice]
            },
            "successful_payment": {
                "value": "ok.",
                "type_hint": Optional[SuccessfulPayment]
            },
            "users_shared": {
                "value": "ok.",
                "type_hint": Optional[UsersShared]
            },
            "chat_shared": {
                "value": "ok.",
                "type_hint": Optional[ChatShared]
            },
            "connected_website": {
                "value": "ok.",
                "type_hint": Optional[str]
            },
            "write_access_allowed": {
                "value": "ok.",
                "type_hint": Optional[WriteAccessAllowed]
            },
            "passport_data": {
                "value": "ok.",
                "type_hint": Optional[PassportData]
            },
            "proximity_alert_triggered": {
                "value": "ok.",
                "type_hint": Optional[ProximityAlertTriggered]
            },
            "forum_topic_created": {
                "value": "ok.",
                "type_hint": Optional[ForumTopicCreated]
            },
            "forum_topic_edited": {
                "value": "ok.",
                "type_hint": Optional[ForumTopicEdited]
            },
            "forum_topic_closed": {
                "value": "ok.",
                "type_hint": Optional[ForumTopicClosed]
            },
            "forum_topic_reopened": {
                "value": "ok.",
                "type_hint": Optional[ForumTopicReopened]
            },
            "general_forum_topic_hidden": {
                "value": "ok.",
                "type_hint": Optional[GeneralForumTopicHidden]
            },
            "general_forum_topic_unhidden": {
                "value": "ok.",
                "type_hint": Optional[GeneralForumTopicUnhidden]
            },
            "giveaway_created": {
                "value": "ok.",
                "type_hint": Optional[GiveawayCreated]
            },
            "giveaway": {
                "value": "ok.",
                "type_hint": Optional[Giveaway]
            },
            "giveaway_winners": {
                "value": "ok.",
                "type_hint": Optional[GiveawayWinners]
            },
            "giveaway_completed": {
                "value": "ok.",
                "type_hint": Optional[GiveawayCompleted]
            },
            "video_chat_scheduled": {
                "value": "ok.",
                "type_hint": Optional[VideoChatScheduled]
            },
            "video_chat_started": {
                "value": "ok.",
                "type_hint": Optional[VideoChatStarted]
            },
            "video_chat_ended": {
                "value": "ok.",
                "type_hint": Optional[VideoChatEnded]
            },
            "video_chat_participants_invited": {
                "value": "ok.",
                "type_hint": Optional[VideoChatParticipantsInvited]
            },
            "web_app_data": {
                "value": "ok.",
                "type_hint": Optional[WebAppData]
            },
            "reply_markup": {
                "value": "ok.",
                "type_hint": Optional[InlineKeyboardMarkup]
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
                "default": "ok."
            },
            "small_file_unique_id": {
                "default": "ok."
            },
            "big_file_id": {
                "default": "ok."
            },
            "big_file_unique_id": {
                "default": "ok."
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
        "self_kwargs": {
            "longitude": {
                "default": "ok."
            },
            "latitude": {
                "default": "ok."
            },
            "horizontal_accuracy": {
                "default": "ok."
            },
            "live_period": {
                "default": "ok."
            },
            "heading": {
                "default": "ok."
            },
            "proximity_alert_radius": {
                "default": "ok."
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
                "default": "ok."
            },
            "address": {
                "default": "ok."
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
                    "default": DEFAULT_REACTION_TYPE_EMOJI
                }
            },
            "emoji": {
                "default": "ok."
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
                    "default": DEFAULT_REACTION_TYPE_CUSTOM_EMOJI
                }
            },
            "custom_emoji_id": {
                "default": "ok."
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
            "linked_chat_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "location": {
                "type_hint": Optional[ChatLocation],
                "default": None
            }
        },
        "self_kwargs": {
            "id": {
                "default": "ok."
            },
            "type": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "username": {
                "default": "ok."
            },
            "first_name": {
                "default": "ok."
            },
            "last_name": {
                "default": "ok."
            },
            "is_forum": {
                "default": "ok."
            },
            "photo": {
                "default": "ok."
            },
            "active_usernames": {
                "default": "ok."
            },
            "available_reactions": {
                "default": "ok."
            },
            "accent_color_id": {
                "default": "ok."
            },
            "background_custom_emoji_id": {
                "default": "ok."
            },
            "profile_accent_color_id": {
                "default": "ok."
            },
            "profile_background_custom_emoji_id": {
                "default": "ok."
            },
            "emoji_status_custom_emoji_id": {
                "default": "ok."
            },
            "emoji_status_expiration_date": {
                "default": "ok."
            },
            "bio": {
                "default": "ok."
            },
            "has_private_forwards": {
                "default": "ok."
            },
            "has_restricted_voice_and_video_messages": {
                "default": "ok."
            },
            "join_to_send_messages": {
                "default": "ok."
            },
            "join_by_request": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "invite_link": {
                "default": "ok."
            },
            "pinned_message": {
                "default": "ok."
            },
            "permissions": {
                "default": "ok."
            },
            "slow_mode_delay": {
                "default": "ok."
            },
            "message_auto_delete_time": {
                "default": "ok."
            },
            "has_aggressive_anti_spam_enabled": {
                "default": "ok."
            },
            "has_hidden_members": {
                "default": "ok."
            },
            "has_protected_content": {
                "default": "ok."
            },
            "has_visible_history": {
                "default": "ok."
            },
            "sticker_set_name": {
                "default": "ok."
            },
            "can_set_sticker_set": {
                "default": "ok."
            },
            "linked_chat_id": {
                "default": "ok."
            },
            "location": {
                "default": "ok."
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
                "default": None
            },
            "actor_chat": {
                "type_hint": Optional[Chat],
                "default": None
            }
        },
        "self_kwargs": {
            "chat": {
                "default": "ok."
            },
            "message_id": {
                "default": "ok."
            },
            "date": {
                "default": "ok."
            },
            "old_reaction": {
                "default": "ok."
            },
            "new_reaction": {
                "default": "ok."
            },
            "user": {
                "default": "ok."
            },
            "actor_chat": {
                "default": "ok."
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
                "default": "ok."
            },
            "total_count": {
                "default": "ok."
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
                "default": "ok."
            },
            "message_id": {
                "default": "ok."
            },
            "date": {
                "default": "ok."
            },
            "reactions": {
                "default": "ok."
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
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "width": {
                "default": "ok."
            },
            "height": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
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
        "self_kwargs": {
            "file_id": {
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "width": {
                "default": "ok."
            },
            "height": {
                "default": "ok."
            },
            "duration": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
            },
            "file_name": {
                "default": "ok."
            },
            "mime_type": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
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
        "self_kwargs": {
            "file_id": {
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "duration": {
                "default": "ok."
            },
            "performer": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "file_name": {
                "default": "ok."
            },
            "mime_type": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
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
        "self_kwargs": {
            "file_id": {
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
            },
            "file_name": {
                "default": "ok."
            },
            "mime_type": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
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
        "self_kwargs": {
            "file_id": {
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "width": {
                "default": "ok."
            },
            "height": {
                "default": "ok."
            },
            "duration": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
            },
            "file_name": {
                "default": "ok."
            },
            "mime_type": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
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
                "default": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "length": {
                "default": "ok."
            },
            "duration": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
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
                "default": None
            },
            "file_size": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "duration": {
                "default": "ok."
            },
            "mime_type": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
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
        "self_kwargs": {
            "phone_number": {
                "default": "ok."
            },
            "first_name": {
                "default": "ok."
            },
            "last_name": {
                "default": "ok."
            },
            "user_id": {
                "default": "ok."
            },
            "vcard": {
                "default": "ok."
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
                "default": "ok."
            },
            "value": {
                "default": "ok."
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
                "default": "ok."
            },
            "voter_count": {
                "default": "ok."
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
                "default": None
            },
            "user": {
                "type_hint": Optional[User],
                "default": None
            }
        },
        "self_kwargs": {
            "poll_id": {
                "default": "ok."
            },
            "option_ids": {
                "default": "ok."
            },
            "voter_chat": {
                "default": "ok."
            },
            "user": {
                "default": "ok."
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
        "self_kwargs": {
            "id": {
                "default": "ok."
            },
            "question": {
                "default": "ok."
            },
            "options": {
                "default": "ok."
            },
            "total_voter_count": {
                "default": "ok."
            },
            "is_closed": {
                "default": "ok."
            },
            "is_anonymous": {
                "default": "ok."
            },
            "type": {
                "default": "ok."
            },
            "allows_multiple_answers": {
                "default": "ok."
            },
            "correct_option_id": {
                "default": "ok."
            },
            "explanation": {
                "default": "ok."
            },
            "explanation_entities": {
                "default": "ok."
            },
            "open_period": {
                "default": "ok."
            },
            "close_date": {
                "default": "ok."
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
        "self_kwargs": {
            "location": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "address": {
                "default": "ok."
            },
            "foursquare_id": {
                "default": "ok."
            },
            "foursquare_type": {
                "default": "ok."
            },
            "google_place_id": {
                "default": "ok."
            },
            "google_place_type": {
                "default": "ok."
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
                "default": "ok."
            },
            "button_text": {
                "default": "ok."
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
                "default": "ok."
            },
            "watcher": {
                "default": "ok."
            },
            "distance": {
                "default": "ok."
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
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "name": {
                "default": "ok."
            },
            "icon_color": {
                "default": "ok."
            },
            "icon_custom_emoji_id": {
                "default": "ok."
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
                "default": None
            },
            "icon_custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {
            "name": {
                "default": "ok."
            },
            "icon_custom_emoji_id": {
                "default": "ok."
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
                "default": "ok."
            },
            "user_ids": {
                "default": "ok."
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
                "default": "ok."
            },
            "chat_id": {
                "default": "ok."
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
        "self_kwargs": {
            "from_request": {
                "default": "ok."
            },
            "web_app_name": {
                "default": "ok."
            },
            "from_attachment_menu": {
                "default": "ok."
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
                "default": "ok."
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
                "default": "ok."
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
                "default": "ok."
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
                "default": "ok."
            },
            "photos": {
                "default": "ok."
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
                "default": None
            },
            "file_path": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
            },
            "file_path": {
                "default": "ok."
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
                "default": "ok."
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
        "self_kwargs": {
            "request_id": {
                "default": "ok."
            },
            "user_is_bot": {
                "default": "ok."
            },
            "user_is_premium": {
                "default": "ok."
            },
            "max_quantity": {
                "default": "ok."
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
        "self_kwargs": {
            "request_id": {
                "default": "ok."
            },
            "chat_is_channel": {
                "default": "ok."
            },
            "chat_is_forum": {
                "default": "ok."
            },
            "chat_has_username": {
                "default": "ok."
            },
            "chat_is_created": {
                "default": "ok."
            },
            "user_administrator_rights": {
                "default": "ok."
            },
            "bot_administrator_rights": {
                "default": "ok."
            },
            "bot_is_member": {
                "default": "ok."
            }
        }
    },
    KeyboardButtonPollType: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {
            "type": {
                "default": "ok."
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
        "self_kwargs": {
            "text": {
                "default": "ok."
            },
            "request_users": {
                "default": "ok."
            },
            "request_chat": {
                "default": "ok."
            },
            "request_contact": {
                "default": "ok."
            },
            "request_location": {
                "default": "ok."
            },
            "request_poll": {
                "default": "ok."
            },
            "web_app": {
                "default": "ok."
            }
        }
    },
    ReplyKeyboardMarkup: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "keyboard": {
                    "default": "keyboard or []"
                }
            },
            "is_persistent": {
                "default": "ok."
            },
            "resize_keyboard": {
                "default": "ok."
            },
            "one_time_keyboard": {
                "default": "ok."
            },
            "input_field_placeholder": {
                "default": "ok."
            },
            "selective": {
                "default": "ok."
            }
        }
    },
    ReplyKeyboardRemove: {
        "has_dese": False,
        "init_kwargs": {
            "selective": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {
            "warning": {
                "remove_keyboard": {
                    "default": True,
                    "type_hint": Literal[True]
                }
            },
            "selective": {
                "default": "ok."
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
        "self_kwargs": {
            "text": {
                "default": "ok."
            },
            "url": {
                "default": "ok."
            },
            "callback_data": {
                "default": "ok."
            },
            "web_app": {
                "default": "ok."
            },
            "login_url": {
                "default": "ok."
            },
            "switch_inline_query": {
                "default": "ok."
            },
            "switch_inline_query_current_chat": {
                "default": "ok."
            },
            "switch_inline_query_chosen_chat": {
                "default": "ok."
            },
            "callback_game": {
                "default": "ok."
            },
            "pay": {
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "warning": {
                "inline_keyboard": {
                    "default": "inline_keyboard or []"
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
        "self_kwargs": {
            "id": {
                "default": "ok."
            },
            "from_user": {
                "default": "ok."
            },
            "chat_instance": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
            },
            "inline_message_id": {
                "default": "ok."
            },
            "data": {
                "default": "ok."
            },
            "game_short_name": {
                "default": "ok."
            }
        }
    },
    ForceReply: {
        "has_dese": False,
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
        "self_kwargs": {
            "force_reply": {
                "default": "ok."
            },
            "input_field_placeholder": {
                "default": "ok."
            },
            "selective": {
                "default": "ok."
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
        "self_kwargs": {
            "invite_link": {
                "default": "ok."
            },
            "creator": {
                "default": "ok."
            },
            "creates_join_request": {
                "default": "ok."
            },
            "is_primary": {
                "default": "ok."
            },
            "is_revoked": {
                "default": "ok."
            },
            "name": {
                "default": "ok."
            },
            "expire_date": {
                "default": "ok."
            },
            "member_limit": {
                "default": "ok."
            },
            "pending_join_request_count": {
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "default": DEFAULT_CHAT_MEMBER_OWNER
                }
            },
            "user": {
                "default": "ok."
            },
            "is_anonymous": {
                "default": "ok."
            },
            "custom_title": {
                "default": "ok."
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
            "can_post_stories": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_edit_stories": {
                "type_hint": Optional[bool],
                "default": None
            },
            "can_delete_stories": {
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
        "self_kwargs": {
            "warning": {
                "status": {
                    "default": DEFAULT_CHAT_MEMBER_ADMINISTRATOR
                }
            },
            "user": {
                "default": "ok."
            },
            "can_be_edited": {
                "default": "ok."
            },
            "is_anonymous": {
                "default": "ok."
            },
            "can_manage_chat": {
                "default": "ok."
            },
            "can_delete_messages": {
                "default": "ok."
            },
            "can_manage_video_chats": {
                "default": "ok."
            },
            "can_restrict_members": {
                "default": "ok."
            },
            "can_promote_members": {
                "default": "ok."
            },
            "can_change_info": {
                "default": "ok."
            },
            "can_invite_users": {
                "default": "ok."
            },
            "can_post_messages": {
                "default": "ok."
            },
            "can_edit_messages": {
                "default": "ok."
            },
            "can_pin_messages": {
                "default": "ok."
            },
            "can_post_stories": {
                "default": "ok."
            },
            "can_edit_stories": {
                "default": "ok."
            },
            "can_delete_stories": {
                "default": "ok."
            },
            "can_manage_topics": {
                "default": "ok."
            },
            "custom_title": {
                "default": "ok."
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
                    "default": DEFAULT_CHAT_MEMBER_MEMBER
                }
            },
            "user": {
                "default": "ok."
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
                    "default": DEFAULT_CHAT_MEMBER_RESTRICTED
                }
            },
            "user": {
                "default": "ok."
            },
            "is_member": {
                "default": "ok."
            },
            "can_send_messages": {
                "default": "ok."
            },
            "can_send_audios": {
                "default": "ok."
            },
            "can_send_documents": {
                "default": "ok."
            },
            "can_send_photos": {
                "default": "ok."
            },
            "can_send_videos": {
                "default": "ok."
            },
            "can_send_video_notes": {
                "default": "ok."
            },
            "can_send_voice_notes": {
                "default": "ok."
            },
            "can_send_polls": {
                "default": "ok."
            },
            "can_send_other_messages": {
                "default": "ok."
            },
            "can_add_web_page_previews": {
                "default": "ok."
            },
            "can_change_info": {
                "default": "ok."
            },
            "can_invite_users": {
                "default": "ok."
            },
            "can_pin_messages": {
                "default": "ok."
            },
            "can_manage_topics": {
                "default": "ok."
            },
            "until_date": {
                "default": "ok."
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
                    "default": DEFAULT_CHAT_MEMBER_LEFT
                }
            },
            "user": {
                "default": "ok."
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
                    "default": DEFAULT_CHAT_MEMBER_BANNED
                }
            },
            "user": {
                "default": "ok."
            },
            "until_date": {
                "default": "ok."
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
                "default": None
            },
            "via_chat_folder_invite_link": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "self_kwargs": {
            "chat": {
                "default": "ok."
            },
            "from_user": {
                "default": "ok."
            },
            "date": {
                "default": "ok."
            },
            "old_chat_member": {
                "default": "ok."
            },
            "new_chat_member": {
                "default": "ok."
            },
            "invite_link": {
                "default": "ok."
            },
            "via_chat_folder_invite_link": {
                "default": "ok."
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
                "default": None
            },
            "invite_link": {
                "type_hint": Optional[ChatInviteLink],
                "default": None
            }
        },
        "self_kwargs": {
            "chat": {
                "default": "ok."
            },
            "from_user": {
                "default": "ok."
            },
            "user_chat_id": {
                "default": "ok."
            },
            "date": {
                "default": "ok."
            },
            "bio": {
                "default": "ok."
            },
            "invite_link": {
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "message_thread_id": {
                "default": "ok."
            },
            "name": {
                "default": "ok."
            },
            "icon_color": {
                "default": "ok."
            },
            "icon_custom_emoji_id": {
                "default": "ok."
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
                "default": "ok."
            },
            "description": {
                "default": "ok."
            }
        }
    },
    BotCommandScopeDefault: {
        "has_dese": False,
        "init_kwargs": {},
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_BOT_COMMAND_SCOPE_DEFAULT
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
                    "default": DEFAULT_BOT_COMMAND_SCOPE_ALL_PRIVATE_CHATS
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
                    "default": DEFAULT_BOT_COMMAND_SCOPE_ALL_GROUP_CHATS
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
                    "default": DEFAULT_BOT_COMMAND_SCOPE_ALL_CHAT_ADMINISTRATORS
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
                    "default": DEFAULT_BOT_COMMAND_SCOPE_CHAT
                }
            },
            "chat_id": {
                "default": "ok."
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
                    "default": DEFAULT_BOT_COMMAND_SCOPE_CHAT_ADMINISTRATORS
                }
            },
            "chat_id": {
                "default": "ok."
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
                    "default": DEFAULT_BOT_COMMAND_SCOPE_CHAT_MEMBER
                }
            },
            "chat_id": {
                "default": "ok."
            },
            "user_id": {
                "default": "ok."
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
                "default": "ok."
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
                "default": "ok."
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
                "default": "ok."
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
                    "default": DEFAULT_MENU_BUTTON_COMMANDS
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
                    "default": DEFAULT_MENU_BUTTON_WEB_APP
                }
            },
            "text": {
                "default": "ok."
            },
            "web_app": {
                "default": "ok."
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
                    "default": DEFAULT_MENU_BUTTON_DEFAULT
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
                "default": None
            },
            "retry_after": {
                "type_hint": Optional[int],
                "default": None
            }
        },
        "self_kwargs": {
            "migrate_to_chat_id": {
                "default": "ok."
            },
            "retry_after": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INPUT_MEDIA_PHOTO
                }
            },
            "media": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "has_spoiler": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INPUT_MEDIA_VIDEO
                }
            },
            "media": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "width": {
                "default": "ok."
            },
            "height": {
                "default": "ok."
            },
            "duration": {
                "default": "ok."
            },
            "supports_streaming": {
                "default": "ok."
            },
            "has_spoiler": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INPUT_MEDIA_ANIMATION
                }
            },
            "media": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "width": {
                "default": "ok."
            },
            "height": {
                "default": "ok."
            },
            "duration": {
                "default": "ok."
            },
            "has_spoiler": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INPUT_MEDIA_AUDIO
                }
            },
            "media": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "duration": {
                "default": "ok."
            },
            "performer": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INPUT_MEDIA_DOCUMENT
                }
            },
            "media": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "disable_content_type_detection": {
                "default": "ok."
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
                "default": "ok."
            },
            "x_shift": {
                "default": "ok."
            },
            "y_shift": {
                "default": "ok."
            },
            "scale": {
                "default": "ok."
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
        "self_kwargs": {
            "file_id": {
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "type": {
                "default": "ok."
            },
            "width": {
                "default": "ok."
            },
            "height": {
                "default": "ok."
            },
            "is_animated": {
                "default": "ok."
            },
            "is_video": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
            },
            "emoji": {
                "default": "ok."
            },
            "set_name": {
                "default": "ok."
            },
            "premium_animation": {
                "default": "ok."
            },
            "mask_position": {
                "default": "ok."
            },
            "custom_emoji_id": {
                "default": "ok."
            },
            "needs_repainting": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "name": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "sticker_type": {
                "default": "ok."
            },
            "is_animated": {
                "default": "ok."
            },
            "is_video": {
                "default": "ok."
            },
            "stickers": {
                "default": "ok."
            },
            "thumbnail": {
                "default": "ok."
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
                "default": None
            },
            "keywords": {
                "type_hint": Optional[list[str]],
                "default": None
            }
        },
        "self_kwargs": {
            "sticker": {
                "default": "ok."
            },
            "emoji_list": {
                "default": "ok."
            },
            "mask_position": {
                "default": "ok."
            },
            "keywords": {
                "default": "ok."
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
                "default": None
            },
            "location": {
                "type_hint": Optional[Location],
                "default": None
            }
        },
        "self_kwargs": {
            "id": {
                "default": "ok."
            },
            "from_user": {
                "default": "ok."
            },
            "query": {
                "default": "ok."
            },
            "offset": {
                "default": "ok."
            },
            "chat_type": {
                "default": "ok."
            },
            "location": {
                "default": "ok."
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
                "default": None
            },
            "start_parameter": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {
            "text": {
                "default": "ok."
            },
            "web_app": {
                "default": "ok."
            },
            "start_parameter": {
                "default": "ok."
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
        "self_kwargs": {
            "message_text": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "entities": {
                "default": "ok."
            },
            "link_preview_options": {
                "default": "ok."
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
        "self_kwargs": {
            "latitude": {
                "default": "ok."
            },
            "longitude": {
                "default": "ok."
            },
            "horizontal_accuracy": {
                "default": "ok."
            },
            "live_period": {
                "default": "ok."
            },
            "heading": {
                "default": "ok."
            },
            "proximity_alert_radius": {
                "default": "ok."
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
        "self_kwargs": {
            "latitude": {
                "default": "ok."
            },
            "longitude": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "address": {
                "default": "ok."
            },
            "foursquare_id": {
                "default": "ok."
            },
            "foursquare_type": {
                "default": "ok."
            },
            "google_place_id": {
                "default": "ok."
            },
            "google_place_type": {
                "default": "ok."
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
                "default": None
            },
            "vcard": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {
            "phone_number": {
                "default": "ok."
            },
            "first_name": {
                "default": "ok."
            },
            "last_name": {
                "default": "ok."
            },
            "vcard": {
                "default": "ok."
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
        "self_kwargs": {
            "title": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "payload": {
                "default": "ok."
            },
            "provider_token": {
                "default": "ok."
            },
            "currency": {
                "default": "ok."
            },
            "prices": {
                "default": "ok."
            },
            "max_tip_amount": {
                "default": "ok."
            },
            "suggested_tip_amounts": {
                "default": "ok."
            },
            "provider_data": {
                "default": "ok."
            },
            "photo_url": {
                "default": "ok."
            },
            "photo_size": {
                "default": "ok."
            },
            "photo_width": {
                "default": "ok."
            },
            "photo_height": {
                "default": "ok."
            },
            "need_name": {
                "default": "ok."
            },
            "need_phone_number": {
                "default": "ok."
            },
            "need_email": {
                "default": "ok."
            },
            "need_shipping_address": {
                "default": "ok."
            },
            "send_phone_number_to_provider": {
                "default": "ok."
            },
            "send_email_to_provider": {
                "default": "ok."
            },
            "is_flexible": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_ARTICLE
                }
            },
            "id": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "url": {
                "default": "ok."
            },
            "hide_url": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "thumbnail_url": {
                "default": "ok."
            },
            "thumbnail_width": {
                "default": "ok."
            },
            "thumbnail_height": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_PHOTO
                }
            },
            "id": {
                "default": "ok."
            },
            "photo_url": {
                "default": "ok."
            },
            "thumbnail_url": {
                "default": "ok."
            },
            "photo_width": {
                "default": "ok."
            },
            "photo_height": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_GIF
                }
            },
            "id": {
                "default": "ok."
            },
            "gif_url": {
                "default": "ok."
            },
            "thumbnail_url": {
                "default": "ok."
            },
            "gif_width": {
                "default": "ok."
            },
            "gif_height": {
                "default": "ok."
            },
            "gif_duration": {
                "default": "ok."
            },
            "thumbnail_mime_type": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_MPEG4_GIF
                }
            },
            "id": {
                "default": "ok."
            },
            "mpeg4_url": {
                "default": "ok."
            },
            "thumbnail_url": {
                "default": "ok."
            },
            "mpeg4_width": {
                "default": "ok."
            },
            "mpeg4_height": {
                "default": "ok."
            },
            "mpeg4_duration": {
                "default": "ok."
            },
            "thumbnail_mime_type": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_VIDEO
                }
            },
            "id": {
                "default": "ok."
            },
            "video_url": {
                "default": "ok."
            },
            "mime_type": {
                "default": "ok."
            },
            "thumbnail_url": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "video_width": {
                "default": "ok."
            },
            "video_height": {
                "default": "ok."
            },
            "video_duration": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_AUDIO
                }
            },
            "id": {
                "default": "ok."
            },
            "audio_url": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "performer": {
                "default": "ok."
            },
            "audio_duration": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_VOICE
                }
            },
            "id": {
                "default": "ok."
            },
            "voice_url": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "voice_duration": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_DOCUMENT
                }
            },
            "id": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "document_url": {
                "default": "ok."
            },
            "mime_type": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
            },
            "thumbnail_url": {
                "default": "ok."
            },
            "thumbnail_width": {
                "default": "ok."
            },
            "thumbnail_height": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_LOCATION
                }
            },
            "id": {
                "default": "ok."
            },
            "latitude": {
                "default": "ok."
            },
            "longitude": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "horizontal_accuracy": {
                "default": "ok."
            },
            "live_period": {
                "default": "ok."
            },
            "heading": {
                "default": "ok."
            },
            "proximity_alert_radius": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
            },
            "thumbnail_url": {
                "default": "ok."
            },
            "thumbnail_width": {
                "default": "ok."
            },
            "thumbnail_height": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_VENUE
                }
            },
            "id": {
                "default": "ok."
            },
            "latitude": {
                "default": "ok."
            },
            "longitude": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "address": {
                "default": "ok."
            },
            "foursquare_id": {
                "default": "ok."
            },
            "foursquare_type": {
                "default": "ok."
            },
            "google_place_id": {
                "default": "ok."
            },
            "google_place_type": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
            },
            "thumbnail_url": {
                "default": "ok."
            },
            "thumbnail_width": {
                "default": "ok."
            },
            "thumbnail_height": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_CONTACT
                }
            },
            "id": {
                "default": "ok."
            },
            "phone_number": {
                "default": "ok."
            },
            "first_name": {
                "default": "ok."
            },
            "last_name": {
                "default": "ok."
            },
            "vcard": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
            },
            "thumbnail_url": {
                "default": "ok."
            },
            "thumbnail_width": {
                "default": "ok."
            },
            "thumbnail_height": {
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_GAME
                }
            },
            "id": {
                "default": "ok."
            },
            "game_short_name": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_CACHED_PHOTO
                }
            },
            "id": {
                "default": "ok."
            },
            "photo_file_id": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_CACHED_GIF
                }
            },
            "id": {
                "default": "ok."
            },
            "gif_file_id": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_CACHED_MPEG4_GIF
                }
            },
            "id": {
                "default": "ok."
            },
            "mpeg4_file_id": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
                "default": None
            },
            "input_message_content": {
                "type_hint": Optional[InputMessageContent],
                "default": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_CACHED_STICKER
                }
            },
            "id": {
                "default": "ok."
            },
            "sticker_file_id": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_CACHED_DOCUMENT
                }
            },
            "id": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "document_file_id": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_CACHED_VIDEO
                }
            },
            "id": {
                "default": "ok."
            },
            "video_file_id": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_CACHED_VOICE
                }
            },
            "id": {
                "default": "ok."
            },
            "voice_file_id": {
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_INLINE_QUERY_RESULT_CACHED_AUDIO
                }
            },
            "id": {
                "default": "ok."
            },
            "audio_file_id": {
                "default": "ok."
            },
            "caption": {
                "default": "ok."
            },
            "parse_mode": {
                "default": "ok."
            },
            "caption_entities": {
                "default": "ok."
            },
            "reply_markup": {
                "default": "ok."
            },
            "input_message_content": {
                "default": "ok."
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
                "default": None
            },
            "inline_message_id": {
                "type_hint": Optional[str],
                "default": None
            }
        },
        "self_kwargs": {
            "result_id": {
                "default": "ok."
            },
            "from_user": {
                "default": "ok."
            },
            "query": {
                "default": "ok."
            },
            "location": {
                "default": "ok."
            },
            "inline_message_id": {
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "inline_message_id": {
                "default": "ok."
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
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "start_parameter": {
                "default": "ok."
            },
            "currency": {
                "default": "ok."
            },
            "total_amount": {
                "default": "ok."
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
                "default": "ok."
            },
            "state": {
                "default": "ok."
            },
            "city": {
                "default": "ok."
            },
            "street_line1": {
                "default": "ok."
            },
            "street_line2": {
                "default": "ok."
            },
            "post_code": {
                "default": "ok."
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
        "self_kwargs": {
            "name": {
                "default": "ok."
            },
            "phone_number": {
                "default": "ok."
            },
            "email": {
                "default": "ok."
            },
            "shipping_address": {
                "default": "ok."
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
                "default": "ok."
            },
            "title": {
                "default": "ok."
            },
            "prices": {
                "default": "ok."
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
                "default": None
            },
            "order_info": {
                "type_hint": Optional[OrderInfo],
                "default": None
            }
        },
        "self_kwargs": {
            "currency": {
                "default": "ok."
            },
            "total_amount": {
                "default": "ok."
            },
            "invoice_payload": {
                "default": "ok."
            },
            "telegram_payment_charge_id": {
                "default": "ok."
            },
            "provider_payment_charge_id": {
                "default": "ok."
            },
            "shipping_option_id": {
                "default": "ok."
            },
            "order_info": {
                "default": "ok."
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
                "default": "ok."
            },
            "from_user": {
                "default": "ok."
            },
            "invoice_payload": {
                "default": "ok."
            },
            "shipping_address": {
                "default": "ok."
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
                "default": None
            },
            "order_info": {
                "type_hint": Optional[OrderInfo],
                "default": None
            }
        },
        "self_kwargs": {
            "id": {
                "default": "ok."
            },
            "from_user": {
                "default": "ok."
            },
            "currency": {
                "default": "ok."
            },
            "total_amount": {
                "default": "ok."
            },
            "invoice_payload": {
                "default": "ok."
            },
            "shipping_option_id": {
                "default": "ok."
            },
            "order_info": {
                "default": "ok."
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
                "default": "ok."
            },
            "file_unique_id": {
                "default": "ok."
            },
            "file_size": {
                "default": "ok."
            },
            "file_date": {
                "default": "ok."
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
        "self_kwargs": {
            "type": {
                "default": "ok."
            },
            "hash": {
                "default": "ok."
            },
            "data": {
                "default": "ok."
            },
            "phone_number": {
                "default": "ok."
            },
            "email": {
                "default": "ok."
            },
            "files": {
                "default": "ok."
            },
            "front_side": {
                "default": "ok."
            },
            "reverse_side": {
                "default": "ok."
            },
            "selfie": {
                "default": "ok."
            },
            "translation": {
                "default": "ok."
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
                "default": "ok."
            },
            "hash": {
                "default": "ok."
            },
            "secret": {
                "default": "ok."
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
                "default": "ok."
            },
            "credentials": {
                "default": "ok."
            }
        }
    },
    PassportElementErrorDataField: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "default": DEFAULT_PASSPORT_ELEMENT_ERROR_DATA_FIELD
                }
            },
            "type": {
                "default": "ok."
            },
            "field_name": {
                "default": "ok."
            },
            "data_hash": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
            }
        }
    },
    PassportElementErrorFrontSide: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "default": DEFAULT_PASSPORT_ELEMENT_ERROR_FRONT_SIDE
                }
            },
            "type": {
                "default": "ok."
            },
            "file_hash": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
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
                    "default": DEFAULT_PASSPORT_ELEMENT_ERROR_REVERSE_SIDE
                }
            },
            "type": {
                "default": "ok."
            },
            "file_hash": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
            }
        }
    },
    PassportElementErrorSelfie: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "default": DEFAULT_PASSPORT_ELEMENT_ERROR_SELFIE
                }
            },
            "type": {
                "default": "ok."
            },
            "file_hash": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
            }
        }
    },
    PassportElementErrorFile: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "default": DEFAULT_PASSPORT_ELEMENT_ERROR_FILE
                }
            },
            "type": {
                "default": "ok."
            },
            "file_hash": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
            }
        }
    },
    PassportElementErrorFiles: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "default": DEFAULT_PASSPORT_ELEMENT_ERROR_FILES
                }
            },
            "type": {
                "default": "ok."
            },
            "file_hashes": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
            }
        }
    },
    PassportElementErrorTranslationFile: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "default": DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILE
                }
            },
            "type": {
                "default": "ok."
            },
            "file_hash": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
            }
        }
    },
    PassportElementErrorTranslationFiles: {
        "has_dese": False,
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
        "self_kwargs": {
            "warning": {
                "source": {
                    "default": DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILES
                }
            },
            "type": {
                "default": "ok."
            },
            "file_hashes": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
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
                    "default": DEFAULT_PASSPORT_ELEMENT_ERROR_UNSPECIFIED
                }
            },
            "type": {
                "default": "ok."
            },
            "element_hash": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
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
        "self_kwargs": {
            "title": {
                "default": "ok."
            },
            "description": {
                "default": "ok."
            },
            "photo": {
                "default": "ok."
            },
            "text": {
                "default": "ok."
            },
            "text_entities": {
                "default": "ok."
            },
            "animation": {
                "default": "ok."
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
                "default": "ok."
            },
            "user": {
                "default": "ok."
            },
            "score": {
                "default": "ok."
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
        "self_kwargs": {
            "chat": {
                "default": "ok."
            },
            "giveaway_message_id": {
                "default": "ok."
            },
            "winners_selection_date": {
                "default": "ok."
            },
            "winner_count": {
                "default": "ok."
            },
            "winners": {
                "default": "ok."
            },
            "additional_chat_count": {
                "default": "ok."
            },
            "premium_subscription_month_count": {
                "default": "ok."
            },
            "unclaimed_prize_count": {
                "default": "ok."
            },
            "only_new_members": {
                "default": "ok."
            },
            "was_refunded": {
                "default": "ok."
            },
            "prize_description": {
                "default": "ok."
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
                "default": None
            },
            "giveaway_message": {
                "type_hint": Optional[Message],
                "default": None
            }
        },
        "self_kwargs": {
            "winner_count": {
                "default": "ok."
            },
            "unclaimed_prize_count": {
                "default": "ok."
            },
            "giveaway_message": {
                "default": "ok."
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
        "self_kwargs": {
            "chats": {
                "default": "ok."
            },
            "winners_selection_date": {
                "default": "ok."
            },
            "winner_count": {
                "default": "ok."
            },
            "only_new_members": {
                "default": "ok."
            },
            "has_public_winners": {
                "default": "ok."
            },
            "prize_description": {
                "default": "ok."
            },
            "country_codes": {
                "default": "ok."
            },
            "premium_subscription_month_count": {
                "default": "ok."
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
                    "default": DEFAULT_MESSAGE_ORIGIN_USER
                }
            },
            "date": {
                "default": "ok."
            },
            "sender_user": {
                "default": "ok."
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
                    "default": DEFAULT_MESSAGE_ORIGIN_HIDDEN_USER
                }
            },
            "date": {
                "default": "ok."
            },
            "sender_user_name": {
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_MESSAGE_ORIGIN_CHAT
                }
            },
            "date": {
                "default": "ok."
            },
            "sender_chat": {
                "default": "ok."
            },
            "author_signature": {
                "default": "ok."
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
                "default": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "default": DEFAULT_MESSAGE_ORIGIN_CHANNEL
                }
            },
            "date": {
                "default": "ok."
            },
            "chat": {
                "default": "ok."
            },
            "message_id": {
                "default": "ok."
            },
            "author_signature": {
                "default": "ok."
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
        "self_kwargs": {
            "origin": {
                "default": "ok."
            },
            "chat": {
                "default": "ok."
            },
            "message_id": {
                "default": "ok."
            },
            "link_preview_options": {
                "default": "ok."
            },
            "animation": {
                "default": "ok."
            },
            "audio": {
                "default": "ok."
            },
            "document": {
                "default": "ok."
            },
            "photo": {
                "default": "ok."
            },
            "sticker": {
                "default": "ok."
            },
            "story": {
                "default": "ok."
            },
            "video": {
                "default": "ok."
            },
            "video_note": {
                "default": "ok."
            },
            "voice": {
                "default": "ok."
            },
            "has_media_spoiler": {
                "default": "ok."
            },
            "contact": {
                "default": "ok."
            },
            "dice": {
                "default": "ok."
            },
            "game": {
                "default": "ok."
            },
            "giveaway": {
                "default": "ok."
            },
            "giveaway_winners": {
                "default": "ok."
            },
            "invoice": {
                "default": "ok."
            },
            "location": {
                "default": "ok."
            },
            "poll": {
                "default": "ok."
            },
            "venue": {
                "default": "ok."
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
                    "default": DEFAULT_CHAT_BOOST_SOURCE_PREMIUM
                }
            },
            "user": {
                "default": "ok."
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
                    "default": DEFAULT_CHAT_BOOST_SOURCE_GIFT_CODE
                }
            },
            "user": {
                "default": "ok."
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
                "default": None
            },
            "is_unclaimed": {
                "type_hint": Optional[Literal[True]],
                "default": None
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "default": DEFAULT_CHAT_BOOST_SOURCE_GIVEAWAY
                }
            },
            "giveaway_message_id": {
                "default": "ok."
            },
            "user": {
                "default": "ok."
            },
            "is_unclaimed": {
                "default": "ok."
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
                "default": "ok."
            },
            "add_date": {
                "default": "ok."
            },
            "expiration_date": {
                "default": "ok."
            },
            "source": {
                "default": "ok."
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
                "default": "ok."
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
                "default": "ok."
            },
            "boost": {
                "default": "ok."
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
                "default": "ok."
            },
            "boost_id": {
                "default": "ok."
            },
            "remove_date": {
                "default": "ok."
            },
            "source": {
                "default": "ok."
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
        "self_kwargs": {
            "warning": {},
            "update_id": {
                "default": "ok."
            },
            "message": {
                "default": "ok."
            },
            "edited_message": {
                "default": "ok."
            },
            "channel_post": {
                "default": "ok."
            },
            "edited_channel_post": {
                "default": "ok."
            },
            "message_reaction": {
                "default": "ok."
            },
            "message_reaction_count": {
                "default": "ok."
            },
            "inline_query": {
                "default": "ok."
            },
            "chosen_inline_result": {
                "default": "ok."
            },
            "callback_query": {
                "default": "ok."
            },
            "shipping_query": {
                "default": "ok."
            },
            "pre_checkout_query": {
                "default": "ok."
            },
            "poll": {
                "default": "ok."
            },
            "poll_answer": {
                "default": "ok."
            },
            "my_chat_member": {
                "default": "ok."
            },
            "chat_member": {
                "default": "ok."
            },
            "chat_join_request": {
                "default": "ok."
            },
            "chat_boost": {
                "default": "ok."
            },
            "removed_chat_boost": {
                "default": "ok."
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
