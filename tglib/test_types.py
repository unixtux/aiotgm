#!/bin/python3

IGNORE = ()
IGNORE = ('InputFile', )

import sys
sys.path.append('../')

from typing import (
    Union,
    Optional,
    Literal
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
                "hinting": Optional[bool],
                "val": None
            },
            "can_send_audios": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_send_documents": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_send_photos": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_send_videos": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_send_video_notes": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_send_voice_notes": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_send_polls": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_send_other_messages": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_add_web_page_previews": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_change_info": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_invite_users": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_pin_messages": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_manage_topics": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "can_send_messages": {
                "val": "ok."
            },
            "can_send_audios": {
                "val": "ok."
            },
            "can_send_documents": {
                "val": "ok."
            },
            "can_send_photos": {
                "val": "ok."
            },
            "can_send_videos": {
                "val": "ok."
            },
            "can_send_video_notes": {
                "val": "ok."
            },
            "can_send_voice_notes": {
                "val": "ok."
            },
            "can_send_polls": {
                "val": "ok."
            },
            "can_send_other_messages": {
                "val": "ok."
            },
            "can_add_web_page_previews": {
                "val": "ok."
            },
            "can_change_info": {
                "val": "ok."
            },
            "can_invite_users": {
                "val": "ok."
            },
            "can_pin_messages": {
                "val": "ok."
            },
            "can_manage_topics": {
                "val": "ok."
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
                "hinting": bool
            },
            "can_manage_chat": {
                "hinting": bool
            },
            "can_delete_messages": {
                "hinting": bool
            },
            "can_manage_video_chats": {
                "hinting": bool
            },
            "can_restrict_members": {
                "hinting": bool
            },
            "can_promote_members": {
                "hinting": bool
            },
            "can_change_info": {
                "hinting": bool
            },
            "can_invite_users": {
                "hinting": bool
            },
            "can_post_messages": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_edit_messages": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_pin_messages": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_post_stories": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_edit_stories": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_delete_stories": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_manage_topics": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "is_anonymous": {
                "val": "ok."
            },
            "can_manage_chat": {
                "val": "ok."
            },
            "can_delete_messages": {
                "val": "ok."
            },
            "can_manage_video_chats": {
                "val": "ok."
            },
            "can_restrict_members": {
                "val": "ok."
            },
            "can_promote_members": {
                "val": "ok."
            },
            "can_change_info": {
                "val": "ok."
            },
            "can_invite_users": {
                "val": "ok."
            },
            "can_post_messages": {
                "val": "ok."
            },
            "can_edit_messages": {
                "val": "ok."
            },
            "can_pin_messages": {
                "val": "ok."
            },
            "can_post_stories": {
                "val": "ok."
            },
            "can_edit_stories": {
                "val": "ok."
            },
            "can_delete_stories": {
                "val": "ok."
            },
            "can_manage_topics": {
                "val": "ok."
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
                "hinting": Optional[str],
                "val": None
            },
            "allow_user_chats": {
                "hinting": Optional[bool],
                "val": None
            },
            "allow_bot_chats": {
                "hinting": Optional[bool],
                "val": None
            },
            "allow_group_chats": {
                "hinting": Optional[bool],
                "val": None
            },
            "allow_channel_chats": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "query": {
                "val": "ok."
            },
            "allow_user_chats": {
                "val": "ok."
            },
            "allow_bot_chats": {
                "val": "ok."
            },
            "allow_group_chats": {
                "val": "ok."
            },
            "allow_channel_chats": {
                "val": "ok."
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
                "hinting": str
            },
            "file_name": {
                "hinting": Optional[str],
                "val": None
            },
            "hide_name": {
                "hinting": bool,
                "val": False
            }
        },
        "self_kwargs": {
            "path": {
                "val": "ok."
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
                "hinting": str
            },
            "forward_text": {
                "hinting": Optional[str],
                "val": None
            },
            "bot_username": {
                "hinting": Optional[str],
                "val": None
            },
            "request_write_access": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "url": {
                "val": "ok."
            },
            "forward_text": {
                "val": "ok."
            },
            "bot_username": {
                "val": "ok."
            },
            "request_write_access": {
                "val": "ok."
            }
        }
    },
    LabeledPrice: {
        "has_dese": False,
        "init_kwargs": {
            "label": {
                "hinting": str
            },
            "amount": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "label": {
                "val": "ok."
            },
            "amount": {
                "val": "ok."
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
                "hinting": Optional[bool],
                "val": None
            },
            "url": {
                "hinting": Optional[str],
                "val": None
            },
            "prefer_small_media": {
                "hinting": Optional[bool],
                "val": None
            },
            "prefer_large_media": {
                "hinting": Optional[bool],
                "val": None
            },
            "show_above_text": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "is_disabled": {
                "val": "ok."
            },
            "url": {
                "val": "ok."
            },
            "prefer_small_media": {
                "val": "ok."
            },
            "prefer_large_media": {
                "val": "ok."
            },
            "show_above_text": {
                "val": "ok."
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
                "hinting": int
            },
            "is_bot": {
                "hinting": bool
            },
            "first_name": {
                "hinting": str
            },
            "last_name": {
                "hinting": Optional[str],
                "val": None
            },
            "username": {
                "hinting": Optional[str],
                "val": None
            },
            "language_code": {
                "hinting": Optional[str],
                "val": None
            },
            "is_premium": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "added_to_attachment_menu": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "can_join_groups": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_read_all_group_messages": {
                "hinting": Optional[bool],
                "val": None
            },
            "supports_inline_queries": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "id": {
                "val": "ok."
            },
            "is_bot": {
                "val": "ok."
            },
            "first_name": {
                "val": "ok."
            },
            "last_name": {
                "val": "ok."
            },
            "username": {
                "val": "ok."
            },
            "language_code": {
                "val": "ok."
            },
            "is_premium": {
                "val": "ok."
            },
            "added_to_attachment_menu": {
                "val": "ok."
            },
            "can_join_groups": {
                "val": "ok."
            },
            "can_read_all_group_messages": {
                "val": "ok."
            },
            "supports_inline_queries": {
                "val": "ok."
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
                "hinting": str
            },
            "offset": {
                "hinting": int
            },
            "length": {
                "hinting": int
            },
            "url": {
                "hinting": Optional[str],
                "val": None
            },
            "user": {
                "hinting": Optional[User],
                "val": None
            },
            "language": {
                "hinting": Optional[str],
                "val": None
            },
            "custom_emoji_id": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "type": {
                "val": "ok."
            },
            "offset": {
                "val": "ok."
            },
            "length": {
                "val": "ok."
            },
            "url": {
                "val": "ok."
            },
            "user": {
                "val": "ok."
            },
            "language": {
                "val": "ok."
            },
            "custom_emoji_id": {
                "val": "ok."
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
                "hinting": str
            },
            "position": {
                "hinting": int
            },
            "entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "is_manual": {
                "hinting": Optional[Literal[True]],
                "val": None
            }
        },
        "self_kwargs": {
            "text": {
                "val": "ok."
            },
            "position": {
                "val": "ok."
            },
            "entities": {
                "val": "ok."
            },
            "is_manual": {
                "val": "ok."
            }
        }
    },
    ReplyParameters: {
        "has_dese": False,
        "init_kwargs": {
            "message_id": {
                "hinting": int
            },
            "chat_id": {
                "hinting": Optional[Union[int, str]],
                "val": None
            },
            "allow_sending_without_reply": {
                "hinting": Optional[bool],
                "val": None
            },
            "quote": {
                "hinting": Optional[str],
                "val": None
            },
            "quote_parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "quote_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "quote_position": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "message_id": {
                "val": "ok."
            },
            "chat_id": {
                "val": "ok."
            },
            "allow_sending_without_reply": {
                "val": "ok."
            },
            "quote": {
                "val": "ok."
            },
            "quote_parse_mode": {
                "val": "ok."
            },
            "quote_entities": {
                "val": "ok."
            },
            "quote_position": {
                "val": "ok."
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
                "val": 0
            }
        },
        "self_kwargs": {
            "chat": {
                "val": "ok.",
                "hinting": Chat
            },
            "message_id": {
                "val": "ok.",
                "hinting": int
            },
            "date": {
                "val": "ok.",
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
                "val": None
            },
            "from_user": {
                "val": None
            },
            "sender_chat": {
                "val": None
            },
            "forward_origin": {
                "val": None
            },
            "is_topic_message": {
                "val": None
            },
            "is_automatic_forward": {
                "val": None
            },
            "reply_to_message": {
                "val": None
            },
            "external_reply": {
                "val": None
            },
            "quote": {
                "val": None
            },
            "via_bot": {
                "val": None
            },
            "edit_date": {
                "val": None
            },
            "has_protected_content": {
                "val": None
            },
            "media_group_id": {
                "val": None
            },
            "author_signature": {
                "val": None
            },
            "text": {
                "val": None
            },
            "entities": {
                "val": None
            },
            "link_preview_options": {
                "val": None
            },
            "animation": {
                "val": None
            },
            "audio": {
                "val": None
            },
            "document": {
                "val": None
            },
            "photo": {
                "val": None
            },
            "sticker": {
                "val": None
            },
            "story": {
                "val": None
            },
            "video": {
                "val": None
            },
            "video_note": {
                "val": None
            },
            "voice": {
                "val": None
            },
            "caption": {
                "val": None
            },
            "caption_entities": {
                "val": None
            },
            "has_media_spoiler": {
                "val": None
            },
            "contact": {
                "val": None
            },
            "dice": {
                "val": None
            },
            "game": {
                "val": None
            },
            "poll": {
                "val": None
            },
            "venue": {
                "val": None
            },
            "location": {
                "val": None
            },
            "new_chat_members": {
                "val": None
            },
            "left_chat_member": {
                "val": None
            },
            "new_chat_title": {
                "val": None
            },
            "new_chat_photo": {
                "val": None
            },
            "delete_chat_photo": {
                "val": None
            },
            "group_chat_created": {
                "val": None
            },
            "supergroup_chat_created": {
                "val": None
            },
            "channel_chat_created": {
                "val": None
            },
            "message_auto_delete_timer_changed": {
                "val": None
            },
            "migrate_to_chat_id": {
                "val": None
            },
            "migrate_from_chat_id": {
                "val": None
            },
            "pinned_message": {
                "val": None
            },
            "invoice": {
                "val": None
            },
            "successful_payment": {
                "val": None
            },
            "users_shared": {
                "val": None
            },
            "chat_shared": {
                "val": None
            },
            "connected_website": {
                "val": None
            },
            "write_access_allowed": {
                "val": None
            },
            "passport_data": {
                "val": None
            },
            "proximity_alert_triggered": {
                "val": None
            },
            "forum_topic_created": {
                "val": None
            },
            "forum_topic_edited": {
                "val": None
            },
            "forum_topic_closed": {
                "val": None
            },
            "forum_topic_reopened": {
                "val": None
            },
            "general_forum_topic_hidden": {
                "val": None
            },
            "general_forum_topic_unhidden": {
                "val": None
            },
            "giveaway_created": {
                "val": None
            },
            "giveaway": {
                "val": None
            },
            "giveaway_winners": {
                "val": None
            },
            "giveaway_completed": {
                "val": None
            },
            "video_chat_scheduled": {
                "val": None
            },
            "video_chat_started": {
                "val": None
            },
            "video_chat_ended": {
                "val": None
            },
            "video_chat_participants_invited": {
                "val": None
            },
            "web_app_data": {
                "val": None
            },
            "reply_markup": {
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "text": {
                    "val": "text or str() # If not text, it's str() instead of None",
                    "hinting": str
                }
            },
            "message_id": {
                "val": "ok.",
                "hinting": int
            },
            "date": {
                "val": "ok.",
                "hinting": int
            },
            "chat": {
                "val": "ok.",
                "hinting": Chat
            },
            "message_thread_id": {
                "val": "ok.",
                "hinting": Optional[int]
            },
            "from_user": {
                "val": "ok.",
                "hinting": Optional[User]
            },
            "sender_chat": {
                "val": "ok.",
                "hinting": Optional[Chat]
            },
            "forward_origin": {
                "val": "ok.",
                "hinting": Optional[MessageOrigin]
            },
            "is_topic_message": {
                "val": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "is_automatic_forward": {
                "val": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "reply_to_message": {
                "val": "ok.",
                "hinting": Optional[Message]
            },
            "external_reply": {
                "val": "ok.",
                "hinting": Optional[ExternalReplyInfo]
            },
            "quote": {
                "val": "ok.",
                "hinting": Optional[TextQuote]
            },
            "via_bot": {
                "val": "ok.",
                "hinting": Optional[User]
            },
            "edit_date": {
                "val": "ok.",
                "hinting": Optional[int]
            },
            "has_protected_content": {
                "val": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "media_group_id": {
                "val": "ok.",
                "hinting": Optional[str]
            },
            "author_signature": {
                "val": "ok.",
                "hinting": Optional[str]
            },
            "entities": {
                "val": "ok.",
                "hinting": Optional[list[MessageEntity]]
            },
            "link_preview_options": {
                "val": "ok.",
                "hinting": Optional[LinkPreviewOptions]
            },
            "animation": {
                "val": "ok.",
                "hinting": Optional[Animation]
            },
            "audio": {
                "val": "ok.",
                "hinting": Optional[Audio]
            },
            "document": {
                "val": "ok.",
                "hinting": Optional[Document]
            },
            "photo": {
                "val": "ok.",
                "hinting": Optional[list[PhotoSize]]
            },
            "sticker": {
                "val": "ok.",
                "hinting": Optional[Sticker]
            },
            "story": {
                "val": "ok.",
                "hinting": Optional[Story]
            },
            "video": {
                "val": "ok.",
                "hinting": Optional[Video]
            },
            "video_note": {
                "val": "ok.",
                "hinting": Optional[VideoNote]
            },
            "voice": {
                "val": "ok.",
                "hinting": Optional[Voice]
            },
            "caption": {
                "val": "ok.",
                "hinting": Optional[str]
            },
            "caption_entities": {
                "val": "ok.",
                "hinting": Optional[list[MessageEntity]]
            },
            "has_media_spoiler": {
                "val": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "contact": {
                "val": "ok.",
                "hinting": Optional[Contact]
            },
            "dice": {
                "val": "ok.",
                "hinting": Optional[Dice]
            },
            "game": {
                "val": "ok.",
                "hinting": Optional[Game]
            },
            "poll": {
                "val": "ok.",
                "hinting": Optional[Poll]
            },
            "venue": {
                "val": "ok.",
                "hinting": Optional[Venue]
            },
            "location": {
                "val": "ok.",
                "hinting": Optional[Location]
            },
            "new_chat_members": {
                "val": "ok.",
                "hinting": Optional[list[User]]
            },
            "left_chat_member": {
                "val": "ok.",
                "hinting": Optional[User]
            },
            "new_chat_title": {
                "val": "ok.",
                "hinting": Optional[str]
            },
            "new_chat_photo": {
                "val": "ok.",
                "hinting": Optional[list[PhotoSize]]
            },
            "delete_chat_photo": {
                "val": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "group_chat_created": {
                "val": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "supergroup_chat_created": {
                "val": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "channel_chat_created": {
                "val": "ok.",
                "hinting": Optional[Literal[True]]
            },
            "message_auto_delete_timer_changed": {
                "val": "ok.",
                "hinting": Optional[MessageAutoDeleteTimerChanged]
            },
            "migrate_to_chat_id": {
                "val": "ok.",
                "hinting": Optional[int]
            },
            "migrate_from_chat_id": {
                "val": "ok.",
                "hinting": Optional[int]
            },
            "pinned_message": {
                "val": "ok.",
                "hinting": Optional[MaybeInaccessibleMessage]
            },
            "invoice": {
                "val": "ok.",
                "hinting": Optional[Invoice]
            },
            "successful_payment": {
                "val": "ok.",
                "hinting": Optional[SuccessfulPayment]
            },
            "users_shared": {
                "val": "ok.",
                "hinting": Optional[UsersShared]
            },
            "chat_shared": {
                "val": "ok.",
                "hinting": Optional[ChatShared]
            },
            "connected_website": {
                "val": "ok.",
                "hinting": Optional[str]
            },
            "write_access_allowed": {
                "val": "ok.",
                "hinting": Optional[WriteAccessAllowed]
            },
            "passport_data": {
                "val": "ok.",
                "hinting": Optional[PassportData]
            },
            "proximity_alert_triggered": {
                "val": "ok.",
                "hinting": Optional[ProximityAlertTriggered]
            },
            "forum_topic_created": {
                "val": "ok.",
                "hinting": Optional[ForumTopicCreated]
            },
            "forum_topic_edited": {
                "val": "ok.",
                "hinting": Optional[ForumTopicEdited]
            },
            "forum_topic_closed": {
                "val": "ok.",
                "hinting": Optional[ForumTopicClosed]
            },
            "forum_topic_reopened": {
                "val": "ok.",
                "hinting": Optional[ForumTopicReopened]
            },
            "general_forum_topic_hidden": {
                "val": "ok.",
                "hinting": Optional[GeneralForumTopicHidden]
            },
            "general_forum_topic_unhidden": {
                "val": "ok.",
                "hinting": Optional[GeneralForumTopicUnhidden]
            },
            "giveaway_created": {
                "val": "ok.",
                "hinting": Optional[GiveawayCreated]
            },
            "giveaway": {
                "val": "ok.",
                "hinting": Optional[Giveaway]
            },
            "giveaway_winners": {
                "val": "ok.",
                "hinting": Optional[GiveawayWinners]
            },
            "giveaway_completed": {
                "val": "ok.",
                "hinting": Optional[GiveawayCompleted]
            },
            "video_chat_scheduled": {
                "val": "ok.",
                "hinting": Optional[VideoChatScheduled]
            },
            "video_chat_started": {
                "val": "ok.",
                "hinting": Optional[VideoChatStarted]
            },
            "video_chat_ended": {
                "val": "ok.",
                "hinting": Optional[VideoChatEnded]
            },
            "video_chat_participants_invited": {
                "val": "ok.",
                "hinting": Optional[VideoChatParticipantsInvited]
            },
            "web_app_data": {
                "val": "ok.",
                "hinting": Optional[WebAppData]
            },
            "reply_markup": {
                "val": "ok.",
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
                "hinting": str
            },
            "small_file_unique_id": {
                "hinting": str
            },
            "big_file_id": {
                "hinting": str
            },
            "big_file_unique_id": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "small_file_id": {
                "val": "ok."
            },
            "small_file_unique_id": {
                "val": "ok."
            },
            "big_file_id": {
                "val": "ok."
            },
            "big_file_unique_id": {
                "val": "ok."
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
                "hinting": float
            },
            "latitude": {
                "hinting": float
            },
            "horizontal_accuracy": {
                "hinting": Optional[float],
                "val": None
            },
            "live_period": {
                "hinting": Optional[int],
                "val": None
            },
            "heading": {
                "hinting": Optional[int],
                "val": None
            },
            "proximity_alert_radius": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "longitude": {
                "val": "ok."
            },
            "latitude": {
                "val": "ok."
            },
            "horizontal_accuracy": {
                "val": "ok."
            },
            "live_period": {
                "val": "ok."
            },
            "heading": {
                "val": "ok."
            },
            "proximity_alert_radius": {
                "val": "ok."
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
                "hinting": Location
            },
            "address": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "location": {
                "val": "ok."
            },
            "address": {
                "val": "ok."
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
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_REACTION_TYPE_EMOJI
                }
            },
            "emoji": {
                "val": "ok."
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
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_REACTION_TYPE_CUSTOM_EMOJI
                }
            },
            "custom_emoji_id": {
                "val": "ok."
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
                "hinting": int
            },
            "type": {
                "hinting": str
            },
            "title": {
                "hinting": Optional[str],
                "val": None
            },
            "username": {
                "hinting": Optional[str],
                "val": None
            },
            "first_name": {
                "hinting": Optional[str],
                "val": None
            },
            "last_name": {
                "hinting": Optional[str],
                "val": None
            },
            "is_forum": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "photo": {
                "hinting": Optional[ChatPhoto],
                "val": None
            },
            "active_usernames": {
                "hinting": Optional[list[str]],
                "val": None
            },
            "available_reactions": {
                "hinting": Optional[list[ReactionType]],
                "val": None
            },
            "accent_color_id": {
                "hinting": Optional[int],
                "val": None
            },
            "background_custom_emoji_id": {
                "hinting": Optional[str],
                "val": None
            },
            "profile_accent_color_id": {
                "hinting": Optional[int],
                "val": None
            },
            "profile_background_custom_emoji_id": {
                "hinting": Optional[str],
                "val": None
            },
            "emoji_status_custom_emoji_id": {
                "hinting": Optional[str],
                "val": None
            },
            "emoji_status_expiration_date": {
                "hinting": Optional[int],
                "val": None
            },
            "bio": {
                "hinting": Optional[str],
                "val": None
            },
            "has_private_forwards": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "has_restricted_voice_and_video_messages": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "join_to_send_messages": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "join_by_request": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "description": {
                "hinting": Optional[str],
                "val": None
            },
            "invite_link": {
                "hinting": Optional[str],
                "val": None
            },
            "pinned_message": {
                "hinting": Optional[Message],
                "val": None
            },
            "permissions": {
                "hinting": Optional[ChatPermissions],
                "val": None
            },
            "slow_mode_delay": {
                "hinting": Optional[int],
                "val": None
            },
            "message_auto_delete_time": {
                "hinting": Optional[int],
                "val": None
            },
            "has_aggressive_anti_spam_enabled": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "has_hidden_members": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "has_protected_content": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "has_visible_history": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "sticker_set_name": {
                "hinting": Optional[str],
                "val": None
            },
            "can_set_sticker_set": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "linked_chat_id": {
                "hinting": Optional[int],
                "val": None
            },
            "location": {
                "hinting": Optional[ChatLocation],
                "val": None
            }
        },
        "self_kwargs": {
            "id": {
                "val": "ok."
            },
            "type": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "username": {
                "val": "ok."
            },
            "first_name": {
                "val": "ok."
            },
            "last_name": {
                "val": "ok."
            },
            "is_forum": {
                "val": "ok."
            },
            "photo": {
                "val": "ok."
            },
            "active_usernames": {
                "val": "ok."
            },
            "available_reactions": {
                "val": "ok."
            },
            "accent_color_id": {
                "val": "ok."
            },
            "background_custom_emoji_id": {
                "val": "ok."
            },
            "profile_accent_color_id": {
                "val": "ok."
            },
            "profile_background_custom_emoji_id": {
                "val": "ok."
            },
            "emoji_status_custom_emoji_id": {
                "val": "ok."
            },
            "emoji_status_expiration_date": {
                "val": "ok."
            },
            "bio": {
                "val": "ok."
            },
            "has_private_forwards": {
                "val": "ok."
            },
            "has_restricted_voice_and_video_messages": {
                "val": "ok."
            },
            "join_to_send_messages": {
                "val": "ok."
            },
            "join_by_request": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "invite_link": {
                "val": "ok."
            },
            "pinned_message": {
                "val": "ok."
            },
            "permissions": {
                "val": "ok."
            },
            "slow_mode_delay": {
                "val": "ok."
            },
            "message_auto_delete_time": {
                "val": "ok."
            },
            "has_aggressive_anti_spam_enabled": {
                "val": "ok."
            },
            "has_hidden_members": {
                "val": "ok."
            },
            "has_protected_content": {
                "val": "ok."
            },
            "has_visible_history": {
                "val": "ok."
            },
            "sticker_set_name": {
                "val": "ok."
            },
            "can_set_sticker_set": {
                "val": "ok."
            },
            "linked_chat_id": {
                "val": "ok."
            },
            "location": {
                "val": "ok."
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
                "hinting": Chat
            },
            "message_id": {
                "hinting": int
            },
            "date": {
                "hinting": int
            },
            "old_reaction": {
                "hinting": list[ReactionType]
            },
            "new_reaction": {
                "hinting": list[ReactionType]
            },
            "user": {
                "hinting": Optional[User],
                "val": None
            },
            "actor_chat": {
                "hinting": Optional[Chat],
                "val": None
            }
        },
        "self_kwargs": {
            "chat": {
                "val": "ok."
            },
            "message_id": {
                "val": "ok."
            },
            "date": {
                "val": "ok."
            },
            "old_reaction": {
                "val": "ok."
            },
            "new_reaction": {
                "val": "ok."
            },
            "user": {
                "val": "ok."
            },
            "actor_chat": {
                "val": "ok."
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
                "hinting": ReactionType
            },
            "total_count": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "type": {
                "val": "ok."
            },
            "total_count": {
                "val": "ok."
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
                "hinting": Chat
            },
            "message_id": {
                "hinting": int
            },
            "date": {
                "hinting": int
            },
            "reactions": {
                "hinting": list[ReactionCount]
            }
        },
        "self_kwargs": {
            "chat": {
                "val": "ok."
            },
            "message_id": {
                "val": "ok."
            },
            "date": {
                "val": "ok."
            },
            "reactions": {
                "val": "ok."
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
                "hinting": int
            }
        },
        "self_kwargs": {
            "message_id": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "width": {
                "hinting": int
            },
            "height": {
                "hinting": int
            },
            "file_size": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "width": {
                "val": "ok."
            },
            "height": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "width": {
                "hinting": int
            },
            "height": {
                "hinting": int
            },
            "duration": {
                "hinting": int
            },
            "thumbnail": {
                "hinting": Optional[PhotoSize],
                "val": None
            },
            "file_name": {
                "hinting": Optional[str],
                "val": None
            },
            "mime_type": {
                "hinting": Optional[str],
                "val": None
            },
            "file_size": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "width": {
                "val": "ok."
            },
            "height": {
                "val": "ok."
            },
            "duration": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            },
            "file_name": {
                "val": "ok."
            },
            "mime_type": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "duration": {
                "hinting": int
            },
            "performer": {
                "hinting": Optional[str],
                "val": None
            },
            "title": {
                "hinting": Optional[str],
                "val": None
            },
            "file_name": {
                "hinting": Optional[str],
                "val": None
            },
            "mime_type": {
                "hinting": Optional[str],
                "val": None
            },
            "file_size": {
                "hinting": Optional[int],
                "val": None
            },
            "thumbnail": {
                "hinting": Optional[PhotoSize],
                "val": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "duration": {
                "val": "ok."
            },
            "performer": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "file_name": {
                "val": "ok."
            },
            "mime_type": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "thumbnail": {
                "hinting": Optional[PhotoSize],
                "val": None
            },
            "file_name": {
                "hinting": Optional[str],
                "val": None
            },
            "mime_type": {
                "hinting": Optional[str],
                "val": None
            },
            "file_size": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            },
            "file_name": {
                "val": "ok."
            },
            "mime_type": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "width": {
                "hinting": int
            },
            "height": {
                "hinting": int
            },
            "duration": {
                "hinting": int
            },
            "thumbnail": {
                "hinting": Optional[PhotoSize],
                "val": None
            },
            "file_name": {
                "hinting": Optional[str],
                "val": None
            },
            "mime_type": {
                "hinting": Optional[str],
                "val": None
            },
            "file_size": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "width": {
                "val": "ok."
            },
            "height": {
                "val": "ok."
            },
            "duration": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            },
            "file_name": {
                "val": "ok."
            },
            "mime_type": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "length": {
                "hinting": int
            },
            "duration": {
                "hinting": int
            },
            "thumbnail": {
                "hinting": Optional[PhotoSize],
                "val": None
            },
            "file_size": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "length": {
                "val": "ok."
            },
            "duration": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "duration": {
                "hinting": int
            },
            "mime_type": {
                "hinting": Optional[str],
                "val": None
            },
            "file_size": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "duration": {
                "val": "ok."
            },
            "mime_type": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
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
                "hinting": str
            },
            "first_name": {
                "hinting": str
            },
            "last_name": {
                "hinting": Optional[str],
                "val": None
            },
            "user_id": {
                "hinting": Optional[int],
                "val": None
            },
            "vcard": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "phone_number": {
                "val": "ok."
            },
            "first_name": {
                "val": "ok."
            },
            "last_name": {
                "val": "ok."
            },
            "user_id": {
                "val": "ok."
            },
            "vcard": {
                "val": "ok."
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
                "hinting": str
            },
            "value": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "emoji": {
                "val": "ok."
            },
            "value": {
                "val": "ok."
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
                "hinting": str
            },
            "voter_count": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "text": {
                "val": "ok."
            },
            "voter_count": {
                "val": "ok."
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
                "hinting": str
            },
            "option_ids": {
                "hinting": list[int]
            },
            "voter_chat": {
                "hinting": Optional[Chat],
                "val": None
            },
            "user": {
                "hinting": Optional[User],
                "val": None
            }
        },
        "self_kwargs": {
            "poll_id": {
                "val": "ok."
            },
            "option_ids": {
                "val": "ok."
            },
            "voter_chat": {
                "val": "ok."
            },
            "user": {
                "val": "ok."
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
                "hinting": str
            },
            "question": {
                "hinting": str
            },
            "options": {
                "hinting": list[PollOption]
            },
            "total_voter_count": {
                "hinting": int
            },
            "is_closed": {
                "hinting": bool
            },
            "is_anonymous": {
                "hinting": bool
            },
            "type": {
                "hinting": str
            },
            "allows_multiple_answers": {
                "hinting": bool
            },
            "correct_option_id": {
                "hinting": Optional[int],
                "val": None
            },
            "explanation": {
                "hinting": Optional[str],
                "val": None
            },
            "explanation_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "open_period": {
                "hinting": Optional[int],
                "val": None
            },
            "close_date": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "id": {
                "val": "ok."
            },
            "question": {
                "val": "ok."
            },
            "options": {
                "val": "ok."
            },
            "total_voter_count": {
                "val": "ok."
            },
            "is_closed": {
                "val": "ok."
            },
            "is_anonymous": {
                "val": "ok."
            },
            "type": {
                "val": "ok."
            },
            "allows_multiple_answers": {
                "val": "ok."
            },
            "correct_option_id": {
                "val": "ok."
            },
            "explanation": {
                "val": "ok."
            },
            "explanation_entities": {
                "val": "ok."
            },
            "open_period": {
                "val": "ok."
            },
            "close_date": {
                "val": "ok."
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
                "hinting": Location
            },
            "title": {
                "hinting": str
            },
            "address": {
                "hinting": str
            },
            "foursquare_id": {
                "hinting": Optional[str],
                "val": None
            },
            "foursquare_type": {
                "hinting": Optional[str],
                "val": None
            },
            "google_place_id": {
                "hinting": Optional[str],
                "val": None
            },
            "google_place_type": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "location": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "address": {
                "val": "ok."
            },
            "foursquare_id": {
                "val": "ok."
            },
            "foursquare_type": {
                "val": "ok."
            },
            "google_place_id": {
                "val": "ok."
            },
            "google_place_type": {
                "val": "ok."
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
                "hinting": str
            },
            "button_text": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "data": {
                "val": "ok."
            },
            "button_text": {
                "val": "ok."
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
                "hinting": User
            },
            "watcher": {
                "hinting": User
            },
            "distance": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "traveler": {
                "val": "ok."
            },
            "watcher": {
                "val": "ok."
            },
            "distance": {
                "val": "ok."
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
                "hinting": int
            }
        },
        "self_kwargs": {
            "message_auto_delete_time": {
                "val": "ok."
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
                "hinting": str
            },
            "icon_color": {
                "hinting": int
            },
            "icon_custom_emoji_id": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "name": {
                "val": "ok."
            },
            "icon_color": {
                "val": "ok."
            },
            "icon_custom_emoji_id": {
                "val": "ok."
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
                "hinting": Optional[str],
                "val": None
            },
            "icon_custom_emoji_id": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "name": {
                "val": "ok."
            },
            "icon_custom_emoji_id": {
                "val": "ok."
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
                "hinting": int
            },
            "user_ids": {
                "hinting": list[int]
            }
        },
        "self_kwargs": {
            "request_id": {
                "val": "ok."
            },
            "user_ids": {
                "val": "ok."
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
                "hinting": int
            },
            "chat_id": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "request_id": {
                "val": "ok."
            },
            "chat_id": {
                "val": "ok."
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
                "hinting": Optional[bool],
                "val": None
            },
            "web_app_name": {
                "hinting": Optional[str],
                "val": None
            },
            "from_attachment_menu": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "from_request": {
                "val": "ok."
            },
            "web_app_name": {
                "val": "ok."
            },
            "from_attachment_menu": {
                "val": "ok."
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
                "hinting": int
            }
        },
        "self_kwargs": {
            "start_date": {
                "val": "ok."
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
                "hinting": int
            }
        },
        "self_kwargs": {
            "duration": {
                "val": "ok."
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
                "hinting": list[User]
            }
        },
        "self_kwargs": {
            "users": {
                "val": "ok."
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
                "hinting": int
            },
            "photos": {
                "hinting": list[list[PhotoSize]]
            }
        },
        "self_kwargs": {
            "total_count": {
                "val": "ok."
            },
            "photos": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "file_size": {
                "hinting": Optional[int],
                "val": None
            },
            "file_path": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
            },
            "file_path": {
                "val": "ok."
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
                "hinting": str
            }
        },
        "self_kwargs": {
            "url": {
                "val": "ok."
            }
        }
    },
    KeyboardButtonRequestUsers: {
        "has_dese": False,
        "init_kwargs": {
            "request_id": {
                "hinting": int
            },
            "user_is_bot": {
                "hinting": Optional[bool],
                "val": None
            },
            "user_is_premium": {
                "hinting": Optional[bool],
                "val": None
            },
            "max_quantity": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "request_id": {
                "val": "ok."
            },
            "user_is_bot": {
                "val": "ok."
            },
            "user_is_premium": {
                "val": "ok."
            },
            "max_quantity": {
                "val": "ok."
            }
        }
    },
    KeyboardButtonRequestChat: {
        "has_dese": False,
        "init_kwargs": {
            "request_id": {
                "hinting": int
            },
            "chat_is_channel": {
                "hinting": bool
            },
            "chat_is_forum": {
                "hinting": Optional[bool],
                "val": None
            },
            "chat_has_username": {
                "hinting": Optional[bool],
                "val": None
            },
            "chat_is_created": {
                "hinting": Optional[bool],
                "val": None
            },
            "user_administrator_rights": {
                "hinting": Optional[ChatAdministratorRights],
                "val": None
            },
            "bot_administrator_rights": {
                "hinting": Optional[ChatAdministratorRights],
                "val": None
            },
            "bot_is_member": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "request_id": {
                "val": "ok."
            },
            "chat_is_channel": {
                "val": "ok."
            },
            "chat_is_forum": {
                "val": "ok."
            },
            "chat_has_username": {
                "val": "ok."
            },
            "chat_is_created": {
                "val": "ok."
            },
            "user_administrator_rights": {
                "val": "ok."
            },
            "bot_administrator_rights": {
                "val": "ok."
            },
            "bot_is_member": {
                "val": "ok."
            }
        }
    },
    KeyboardButtonPollType: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "type": {
                "val": "ok."
            }
        }
    },
    KeyboardButton: {
        "has_dese": False,
        "init_kwargs": {
            "text": {
                "hinting": str
            },
            "request_users": {
                "hinting": Optional[KeyboardButtonRequestUsers],
                "val": None
            },
            "request_chat": {
                "hinting": Optional[KeyboardButtonRequestChat],
                "val": None
            },
            "request_contact": {
                "hinting": Optional[bool],
                "val": None
            },
            "request_location": {
                "hinting": Optional[bool],
                "val": None
            },
            "request_poll": {
                "hinting": Optional[KeyboardButtonPollType],
                "val": None
            },
            "web_app": {
                "hinting": Optional[WebAppInfo],
                "val": None
            }
        },
        "self_kwargs": {
            "text": {
                "val": "ok."
            },
            "request_users": {
                "val": "ok."
            },
            "request_chat": {
                "val": "ok."
            },
            "request_contact": {
                "val": "ok."
            },
            "request_location": {
                "val": "ok."
            },
            "request_poll": {
                "val": "ok."
            },
            "web_app": {
                "val": "ok."
            }
        }
    },
    ReplyKeyboardMarkup: {
        "has_dese": False,
        "init_kwargs": {
            "keyboard": {
                "hinting": Optional[list[list[KeyboardButton]]],
                "val": None
            },
            "is_persistent": {
                "hinting": Optional[bool],
                "val": None
            },
            "resize_keyboard": {
                "hinting": Optional[bool],
                "val": None
            },
            "one_time_keyboard": {
                "hinting": Optional[bool],
                "val": None
            },
            "input_field_placeholder": {
                "hinting": Optional[str],
                "val": None
            },
            "selective": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "keyboard": {
                    "val": "keyboard or []"
                }
            },
            "is_persistent": {
                "val": "ok."
            },
            "resize_keyboard": {
                "val": "ok."
            },
            "one_time_keyboard": {
                "val": "ok."
            },
            "input_field_placeholder": {
                "val": "ok."
            },
            "selective": {
                "val": "ok."
            }
        }
    },
    ReplyKeyboardRemove: {
        "has_dese": False,
        "init_kwargs": {
            "selective": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "remove_keyboard": {
                    "val": True,
                    "hinting": Literal[True]
                }
            },
            "selective": {
                "val": "ok."
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
                "hinting": str
            },
            "url": {
                "hinting": Optional[str],
                "val": None
            },
            "callback_data": {
                "hinting": Optional[str],
                "val": None
            },
            "web_app": {
                "hinting": Optional[WebAppInfo],
                "val": None
            },
            "login_url": {
                "hinting": Optional[LoginUrl],
                "val": None
            },
            "switch_inline_query": {
                "hinting": Optional[str],
                "val": None
            },
            "switch_inline_query_current_chat": {
                "hinting": Optional[str],
                "val": None
            },
            "switch_inline_query_chosen_chat": {
                "hinting": Optional[SwitchInlineQueryChosenChat],
                "val": None
            },
            "callback_game": {
                "hinting": Optional[CallbackGame],
                "val": None
            },
            "pay": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "text": {
                "val": "ok."
            },
            "url": {
                "val": "ok."
            },
            "callback_data": {
                "val": "ok."
            },
            "web_app": {
                "val": "ok."
            },
            "login_url": {
                "val": "ok."
            },
            "switch_inline_query": {
                "val": "ok."
            },
            "switch_inline_query_current_chat": {
                "val": "ok."
            },
            "switch_inline_query_chosen_chat": {
                "val": "ok."
            },
            "callback_game": {
                "val": "ok."
            },
            "pay": {
                "val": "ok."
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
                "hinting": Optional[list[list[InlineKeyboardButton]]],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "inline_keyboard": {
                    "val": "inline_keyboard or []"
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
                "hinting": str
            },
            "from_user": {
                "hinting": User
            },
            "chat_instance": {
                "hinting": str
            },
            "message": {
                "hinting": Optional[MaybeInaccessibleMessage],
                "val": None
            },
            "inline_message_id": {
                "hinting": Optional[str],
                "val": None
            },
            "data": {
                "hinting": Optional[str],
                "val": None
            },
            "game_short_name": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "id": {
                "val": "ok."
            },
            "from_user": {
                "val": "ok."
            },
            "chat_instance": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
            },
            "inline_message_id": {
                "val": "ok."
            },
            "data": {
                "val": "ok."
            },
            "game_short_name": {
                "val": "ok."
            }
        }
    },
    ForceReply: {
        "has_dese": False,
        "init_kwargs": {
            "force_reply": {
                "hinting": Literal[True],
                "val": True
            },
            "input_field_placeholder": {
                "hinting": Optional[str],
                "val": None
            },
            "selective": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "force_reply": {
                "val": "ok."
            },
            "input_field_placeholder": {
                "val": "ok."
            },
            "selective": {
                "val": "ok."
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
                "hinting": str
            },
            "creator": {
                "hinting": User
            },
            "creates_join_request": {
                "hinting": bool
            },
            "is_primary": {
                "hinting": bool
            },
            "is_revoked": {
                "hinting": bool
            },
            "name": {
                "hinting": Optional[str],
                "val": None
            },
            "expire_date": {
                "hinting": Optional[int],
                "val": None
            },
            "member_limit": {
                "hinting": Optional[int],
                "val": None
            },
            "pending_join_request_count": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "invite_link": {
                "val": "ok."
            },
            "creator": {
                "val": "ok."
            },
            "creates_join_request": {
                "val": "ok."
            },
            "is_primary": {
                "val": "ok."
            },
            "is_revoked": {
                "val": "ok."
            },
            "name": {
                "val": "ok."
            },
            "expire_date": {
                "val": "ok."
            },
            "member_limit": {
                "val": "ok."
            },
            "pending_join_request_count": {
                "val": "ok."
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
                "hinting": User
            },
            "is_anonymous": {
                "hinting": bool
            },
            "custom_title": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "val": DEFAULT_CHAT_MEMBER_OWNER
                }
            },
            "user": {
                "val": "ok."
            },
            "is_anonymous": {
                "val": "ok."
            },
            "custom_title": {
                "val": "ok."
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
                "hinting": User
            },
            "can_be_edited": {
                "hinting": bool
            },
            "is_anonymous": {
                "hinting": bool
            },
            "can_manage_chat": {
                "hinting": bool
            },
            "can_delete_messages": {
                "hinting": bool
            },
            "can_manage_video_chats": {
                "hinting": bool
            },
            "can_restrict_members": {
                "hinting": bool
            },
            "can_promote_members": {
                "hinting": bool
            },
            "can_change_info": {
                "hinting": bool
            },
            "can_invite_users": {
                "hinting": bool
            },
            "can_post_messages": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_edit_messages": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_pin_messages": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_post_stories": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_edit_stories": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_delete_stories": {
                "hinting": Optional[bool],
                "val": None
            },
            "can_manage_topics": {
                "hinting": Optional[bool],
                "val": None
            },
            "custom_title": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "val": DEFAULT_CHAT_MEMBER_ADMINISTRATOR
                }
            },
            "user": {
                "val": "ok."
            },
            "can_be_edited": {
                "val": "ok."
            },
            "is_anonymous": {
                "val": "ok."
            },
            "can_manage_chat": {
                "val": "ok."
            },
            "can_delete_messages": {
                "val": "ok."
            },
            "can_manage_video_chats": {
                "val": "ok."
            },
            "can_restrict_members": {
                "val": "ok."
            },
            "can_promote_members": {
                "val": "ok."
            },
            "can_change_info": {
                "val": "ok."
            },
            "can_invite_users": {
                "val": "ok."
            },
            "can_post_messages": {
                "val": "ok."
            },
            "can_edit_messages": {
                "val": "ok."
            },
            "can_pin_messages": {
                "val": "ok."
            },
            "can_post_stories": {
                "val": "ok."
            },
            "can_edit_stories": {
                "val": "ok."
            },
            "can_delete_stories": {
                "val": "ok."
            },
            "can_manage_topics": {
                "val": "ok."
            },
            "custom_title": {
                "val": "ok."
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
                "hinting": User
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "val": DEFAULT_CHAT_MEMBER_MEMBER
                }
            },
            "user": {
                "val": "ok."
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
                "hinting": User
            },
            "is_member": {
                "hinting": bool
            },
            "can_send_messages": {
                "hinting": bool
            },
            "can_send_audios": {
                "hinting": bool
            },
            "can_send_documents": {
                "hinting": bool
            },
            "can_send_photos": {
                "hinting": bool
            },
            "can_send_videos": {
                "hinting": bool
            },
            "can_send_video_notes": {
                "hinting": bool
            },
            "can_send_voice_notes": {
                "hinting": bool
            },
            "can_send_polls": {
                "hinting": bool
            },
            "can_send_other_messages": {
                "hinting": bool
            },
            "can_add_web_page_previews": {
                "hinting": bool
            },
            "can_change_info": {
                "hinting": bool
            },
            "can_invite_users": {
                "hinting": bool
            },
            "can_pin_messages": {
                "hinting": bool
            },
            "can_manage_topics": {
                "hinting": bool
            },
            "until_date": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "val": DEFAULT_CHAT_MEMBER_RESTRICTED
                }
            },
            "user": {
                "val": "ok."
            },
            "is_member": {
                "val": "ok."
            },
            "can_send_messages": {
                "val": "ok."
            },
            "can_send_audios": {
                "val": "ok."
            },
            "can_send_documents": {
                "val": "ok."
            },
            "can_send_photos": {
                "val": "ok."
            },
            "can_send_videos": {
                "val": "ok."
            },
            "can_send_video_notes": {
                "val": "ok."
            },
            "can_send_voice_notes": {
                "val": "ok."
            },
            "can_send_polls": {
                "val": "ok."
            },
            "can_send_other_messages": {
                "val": "ok."
            },
            "can_add_web_page_previews": {
                "val": "ok."
            },
            "can_change_info": {
                "val": "ok."
            },
            "can_invite_users": {
                "val": "ok."
            },
            "can_pin_messages": {
                "val": "ok."
            },
            "can_manage_topics": {
                "val": "ok."
            },
            "until_date": {
                "val": "ok."
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
                "hinting": User
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "val": DEFAULT_CHAT_MEMBER_LEFT
                }
            },
            "user": {
                "val": "ok."
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
                "hinting": User
            },
            "until_date": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "warning": {
                "status": {
                    "val": DEFAULT_CHAT_MEMBER_BANNED
                }
            },
            "user": {
                "val": "ok."
            },
            "until_date": {
                "val": "ok."
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
                "hinting": Chat
            },
            "from_user": {
                "hinting": User
            },
            "date": {
                "hinting": int
            },
            "old_chat_member": {
                "hinting": list[ChatMember]
            },
            "new_chat_member": {
                "hinting": list[ChatMember]
            },
            "invite_link": {
                "hinting": Optional[ChatInviteLink],
                "val": None
            },
            "via_chat_folder_invite_link": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "chat": {
                "val": "ok."
            },
            "from_user": {
                "val": "ok."
            },
            "date": {
                "val": "ok."
            },
            "old_chat_member": {
                "val": "ok."
            },
            "new_chat_member": {
                "val": "ok."
            },
            "invite_link": {
                "val": "ok."
            },
            "via_chat_folder_invite_link": {
                "val": "ok."
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
                "hinting": Chat
            },
            "from_user": {
                "hinting": User
            },
            "user_chat_id": {
                "hinting": int
            },
            "date": {
                "hinting": int
            },
            "bio": {
                "hinting": Optional[str],
                "val": None
            },
            "invite_link": {
                "hinting": Optional[ChatInviteLink],
                "val": None
            }
        },
        "self_kwargs": {
            "chat": {
                "val": "ok."
            },
            "from_user": {
                "val": "ok."
            },
            "user_chat_id": {
                "val": "ok."
            },
            "date": {
                "val": "ok."
            },
            "bio": {
                "val": "ok."
            },
            "invite_link": {
                "val": "ok."
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
                "hinting": int
            },
            "name": {
                "hinting": str
            },
            "icon_color": {
                "hinting": int
            },
            "icon_custom_emoji_id": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "message_thread_id": {
                "val": "ok."
            },
            "name": {
                "val": "ok."
            },
            "icon_color": {
                "val": "ok."
            },
            "icon_custom_emoji_id": {
                "val": "ok."
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
                "hinting": str
            },
            "description": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "command": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            }
        }
    },
    BotCommandScopeDefault: {
        "has_dese": False,
        "init_kwargs": {},
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_BOT_COMMAND_SCOPE_DEFAULT
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
                    "val": DEFAULT_BOT_COMMAND_SCOPE_ALL_PRIVATE_CHATS
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
                    "val": DEFAULT_BOT_COMMAND_SCOPE_ALL_GROUP_CHATS
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
                    "val": DEFAULT_BOT_COMMAND_SCOPE_ALL_CHAT_ADMINISTRATORS
                }
            }
        }
    },
    BotCommandScopeChat: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": {
                "hinting": Union[int, str]
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_BOT_COMMAND_SCOPE_CHAT
                }
            },
            "chat_id": {
                "val": "ok."
            }
        }
    },
    BotCommandScopeChatAdministrators: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": {
                "hinting": Union[int, str]
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_BOT_COMMAND_SCOPE_CHAT_ADMINISTRATORS
                }
            },
            "chat_id": {
                "val": "ok."
            }
        }
    },
    BotCommandScopeChatMember: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": {
                "hinting": Union[int, str]
            },
            "user_id": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_BOT_COMMAND_SCOPE_CHAT_MEMBER
                }
            },
            "chat_id": {
                "val": "ok."
            },
            "user_id": {
                "val": "ok."
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
                "hinting": str
            }
        },
        "self_kwargs": {
            "name": {
                "val": "ok."
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
                "hinting": str
            }
        },
        "self_kwargs": {
            "description": {
                "val": "ok."
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
                "hinting": str
            }
        },
        "self_kwargs": {
            "short_description": {
                "val": "ok."
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
                    "val": DEFAULT_MENU_BUTTON_COMMANDS
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
                "hinting": str
            },
            "web_app": {
                "hinting": WebAppInfo
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_MENU_BUTTON_WEB_APP
                }
            },
            "text": {
                "val": "ok."
            },
            "web_app": {
                "val": "ok."
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
                    "val": DEFAULT_MENU_BUTTON_DEFAULT
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
                "hinting": Optional[int],
                "val": None
            },
            "retry_after": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "migrate_to_chat_id": {
                "val": "ok."
            },
            "retry_after": {
                "val": "ok."
            }
        }
    },
    InputMediaPhoto: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "hinting": str
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "has_spoiler": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INPUT_MEDIA_PHOTO
                }
            },
            "media": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "has_spoiler": {
                "val": "ok."
            }
        }
    },
    InputMediaVideo: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "hinting": str
            },
            "thumbnail": {
                "hinting": Optional[Union[InputFile, str]],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "width": {
                "hinting": Optional[int],
                "val": None
            },
            "height": {
                "hinting": Optional[int],
                "val": None
            },
            "duration": {
                "hinting": Optional[int],
                "val": None
            },
            "supports_streaming": {
                "hinting": Optional[bool],
                "val": None
            },
            "has_spoiler": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INPUT_MEDIA_VIDEO
                }
            },
            "media": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "width": {
                "val": "ok."
            },
            "height": {
                "val": "ok."
            },
            "duration": {
                "val": "ok."
            },
            "supports_streaming": {
                "val": "ok."
            },
            "has_spoiler": {
                "val": "ok."
            }
        }
    },
    InputMediaAnimation: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "hinting": str
            },
            "thumbnail": {
                "hinting": Optional[Union[InputFile, str]],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "width": {
                "hinting": Optional[int],
                "val": None
            },
            "height": {
                "hinting": Optional[int],
                "val": None
            },
            "duration": {
                "hinting": Optional[int],
                "val": None
            },
            "has_spoiler": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INPUT_MEDIA_ANIMATION
                }
            },
            "media": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "width": {
                "val": "ok."
            },
            "height": {
                "val": "ok."
            },
            "duration": {
                "val": "ok."
            },
            "has_spoiler": {
                "val": "ok."
            }
        }
    },
    InputMediaAudio: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "hinting": str
            },
            "thumbnail": {
                "hinting": Optional[Union[InputFile, str]],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "duration": {
                "hinting": Optional[int],
                "val": None
            },
            "performer": {
                "hinting": Optional[str],
                "val": None
            },
            "title": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INPUT_MEDIA_AUDIO
                }
            },
            "media": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "duration": {
                "val": "ok."
            },
            "performer": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            }
        }
    },
    InputMediaDocument: {
        "has_dese": False,
        "init_kwargs": {
            "media": {
                "hinting": str
            },
            "thumbnail": {
                "hinting": Optional[Union[InputFile, str]],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "disable_content_type_detection": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INPUT_MEDIA_DOCUMENT
                }
            },
            "media": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "disable_content_type_detection": {
                "val": "ok."
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
                "hinting": str
            },
            "x_shift": {
                "hinting": float
            },
            "y_shift": {
                "hinting": float
            },
            "scale": {
                "hinting": float
            }
        },
        "self_kwargs": {
            "point": {
                "val": "ok."
            },
            "x_shift": {
                "val": "ok."
            },
            "y_shift": {
                "val": "ok."
            },
            "scale": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "type": {
                "hinting": str
            },
            "width": {
                "hinting": int
            },
            "height": {
                "hinting": int
            },
            "is_animated": {
                "hinting": bool
            },
            "is_video": {
                "hinting": bool
            },
            "thumbnail": {
                "hinting": Optional[PhotoSize],
                "val": None
            },
            "emoji": {
                "hinting": Optional[str],
                "val": None
            },
            "set_name": {
                "hinting": Optional[str],
                "val": None
            },
            "premium_animation": {
                "hinting": Optional[File],
                "val": None
            },
            "mask_position": {
                "hinting": Optional[MaskPosition],
                "val": None
            },
            "custom_emoji_id": {
                "hinting": Optional[str],
                "val": None
            },
            "needs_repainting": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "file_size": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "type": {
                "val": "ok."
            },
            "width": {
                "val": "ok."
            },
            "height": {
                "val": "ok."
            },
            "is_animated": {
                "val": "ok."
            },
            "is_video": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            },
            "emoji": {
                "val": "ok."
            },
            "set_name": {
                "val": "ok."
            },
            "premium_animation": {
                "val": "ok."
            },
            "mask_position": {
                "val": "ok."
            },
            "custom_emoji_id": {
                "val": "ok."
            },
            "needs_repainting": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
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
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "sticker_type": {
                "hinting": str
            },
            "is_animated": {
                "hinting": bool
            },
            "is_video": {
                "hinting": bool
            },
            "stickers": {
                "hinting": list[Sticker]
            },
            "thumbnail": {
                "hinting": Optional[PhotoSize],
                "val": None
            }
        },
        "self_kwargs": {
            "name": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "sticker_type": {
                "val": "ok."
            },
            "is_animated": {
                "val": "ok."
            },
            "is_video": {
                "val": "ok."
            },
            "stickers": {
                "val": "ok."
            },
            "thumbnail": {
                "val": "ok."
            }
        }
    },
    InputSticker: {
        "has_dese": False,
        "init_kwargs": {
            "sticker": {
                "hinting": Union[InputFile, str]
            },
            "emoji_list": {
                "hinting": list[str]
            },
            "mask_position": {
                "hinting": Optional[MaskPosition],
                "val": None
            },
            "keywords": {
                "hinting": Optional[list[str]],
                "val": None
            }
        },
        "self_kwargs": {
            "sticker": {
                "val": "ok."
            },
            "emoji_list": {
                "val": "ok."
            },
            "mask_position": {
                "val": "ok."
            },
            "keywords": {
                "val": "ok."
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
                "hinting": str
            },
            "from_user": {
                "hinting": User
            },
            "query": {
                "hinting": str
            },
            "offset": {
                "hinting": str
            },
            "chat_type": {
                "hinting": Optional[str],
                "val": None
            },
            "location": {
                "hinting": Optional[Location],
                "val": None
            }
        },
        "self_kwargs": {
            "id": {
                "val": "ok."
            },
            "from_user": {
                "val": "ok."
            },
            "query": {
                "val": "ok."
            },
            "offset": {
                "val": "ok."
            },
            "chat_type": {
                "val": "ok."
            },
            "location": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultsButton: {
        "has_dese": False,
        "init_kwargs": {
            "text": {
                "hinting": str
            },
            "web_app": {
                "hinting": Optional[WebAppInfo],
                "val": None
            },
            "start_parameter": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "text": {
                "val": "ok."
            },
            "web_app": {
                "val": "ok."
            },
            "start_parameter": {
                "val": "ok."
            }
        }
    },
    InputTextMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "message_text": {
                "hinting": str
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "link_preview_options": {
                "hinting": Optional[LinkPreviewOptions],
                "val": None
            }
        },
        "self_kwargs": {
            "message_text": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "entities": {
                "val": "ok."
            },
            "link_preview_options": {
                "val": "ok."
            }
        }
    },
    InputLocationMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "latitude": {
                "hinting": float
            },
            "longitude": {
                "hinting": float
            },
            "horizontal_accuracy": {
                "hinting": Optional[float],
                "val": None
            },
            "live_period": {
                "hinting": Optional[int],
                "val": None
            },
            "heading": {
                "hinting": Optional[int],
                "val": None
            },
            "proximity_alert_radius": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "latitude": {
                "val": "ok."
            },
            "longitude": {
                "val": "ok."
            },
            "horizontal_accuracy": {
                "val": "ok."
            },
            "live_period": {
                "val": "ok."
            },
            "heading": {
                "val": "ok."
            },
            "proximity_alert_radius": {
                "val": "ok."
            }
        }
    },
    InputVenueMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "latitude": {
                "hinting": float
            },
            "longitude": {
                "hinting": float
            },
            "title": {
                "hinting": str
            },
            "address": {
                "hinting": str
            },
            "foursquare_id": {
                "hinting": Optional[str],
                "val": None
            },
            "foursquare_type": {
                "hinting": Optional[str],
                "val": None
            },
            "google_place_id": {
                "hinting": Optional[str],
                "val": None
            },
            "google_place_type": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "latitude": {
                "val": "ok."
            },
            "longitude": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "address": {
                "val": "ok."
            },
            "foursquare_id": {
                "val": "ok."
            },
            "foursquare_type": {
                "val": "ok."
            },
            "google_place_id": {
                "val": "ok."
            },
            "google_place_type": {
                "val": "ok."
            }
        }
    },
    InputContactMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "phone_number": {
                "hinting": str
            },
            "first_name": {
                "hinting": str
            },
            "last_name": {
                "hinting": Optional[str],
                "val": None
            },
            "vcard": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "phone_number": {
                "val": "ok."
            },
            "first_name": {
                "val": "ok."
            },
            "last_name": {
                "val": "ok."
            },
            "vcard": {
                "val": "ok."
            }
        }
    },
    InputInvoiceMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "title": {
                "hinting": str
            },
            "description": {
                "hinting": str
            },
            "payload": {
                "hinting": str
            },
            "provider_token": {
                "hinting": str
            },
            "currency": {
                "hinting": str
            },
            "prices": {
                "hinting": list[LabeledPrice]
            },
            "max_tip_amount": {
                "hinting": Optional[int],
                "val": None
            },
            "suggested_tip_amounts": {
                "hinting": Optional[list[int]],
                "val": None
            },
            "provider_data": {
                "hinting": Optional[str],
                "val": None
            },
            "photo_url": {
                "hinting": Optional[str],
                "val": None
            },
            "photo_size": {
                "hinting": Optional[int],
                "val": None
            },
            "photo_width": {
                "hinting": Optional[int],
                "val": None
            },
            "photo_height": {
                "hinting": Optional[int],
                "val": None
            },
            "need_name": {
                "hinting": Optional[bool],
                "val": None
            },
            "need_phone_number": {
                "hinting": Optional[bool],
                "val": None
            },
            "need_email": {
                "hinting": Optional[bool],
                "val": None
            },
            "need_shipping_address": {
                "hinting": Optional[bool],
                "val": None
            },
            "send_phone_number_to_provider": {
                "hinting": Optional[bool],
                "val": None
            },
            "send_email_to_provider": {
                "hinting": Optional[bool],
                "val": None
            },
            "is_flexible": {
                "hinting": Optional[bool],
                "val": None
            }
        },
        "self_kwargs": {
            "title": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "payload": {
                "val": "ok."
            },
            "provider_token": {
                "val": "ok."
            },
            "currency": {
                "val": "ok."
            },
            "prices": {
                "val": "ok."
            },
            "max_tip_amount": {
                "val": "ok."
            },
            "suggested_tip_amounts": {
                "val": "ok."
            },
            "provider_data": {
                "val": "ok."
            },
            "photo_url": {
                "val": "ok."
            },
            "photo_size": {
                "val": "ok."
            },
            "photo_width": {
                "val": "ok."
            },
            "photo_height": {
                "val": "ok."
            },
            "need_name": {
                "val": "ok."
            },
            "need_phone_number": {
                "val": "ok."
            },
            "need_email": {
                "val": "ok."
            },
            "need_shipping_address": {
                "val": "ok."
            },
            "send_phone_number_to_provider": {
                "val": "ok."
            },
            "send_email_to_provider": {
                "val": "ok."
            },
            "is_flexible": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultArticle: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "input_message_content": {
                "hinting": InputMessageContent
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "url": {
                "hinting": Optional[str],
                "val": None
            },
            "hide_url": {
                "hinting": Optional[bool],
                "val": None
            },
            "description": {
                "hinting": Optional[str],
                "val": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "val": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "val": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_ARTICLE
                }
            },
            "id": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "url": {
                "val": "ok."
            },
            "hide_url": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "thumbnail_url": {
                "val": "ok."
            },
            "thumbnail_width": {
                "val": "ok."
            },
            "thumbnail_height": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultPhoto: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "photo_url": {
                "hinting": str
            },
            "thumbnail_url": {
                "hinting": str
            },
            "photo_width": {
                "hinting": Optional[int],
                "val": None
            },
            "photo_height": {
                "hinting": Optional[int],
                "val": None
            },
            "title": {
                "hinting": Optional[str],
                "val": None
            },
            "description": {
                "hinting": Optional[str],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_PHOTO
                }
            },
            "id": {
                "val": "ok."
            },
            "photo_url": {
                "val": "ok."
            },
            "thumbnail_url": {
                "val": "ok."
            },
            "photo_width": {
                "val": "ok."
            },
            "photo_height": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultGif: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "gif_url": {
                "hinting": str
            },
            "thumbnail_url": {
                "hinting": str
            },
            "gif_width": {
                "hinting": Optional[int],
                "val": None
            },
            "gif_height": {
                "hinting": Optional[int],
                "val": None
            },
            "gif_duration": {
                "hinting": Optional[int],
                "val": None
            },
            "thumbnail_mime_type": {
                "hinting": Optional[str],
                "val": None
            },
            "title": {
                "hinting": Optional[str],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_GIF
                }
            },
            "id": {
                "val": "ok."
            },
            "gif_url": {
                "val": "ok."
            },
            "thumbnail_url": {
                "val": "ok."
            },
            "gif_width": {
                "val": "ok."
            },
            "gif_height": {
                "val": "ok."
            },
            "gif_duration": {
                "val": "ok."
            },
            "thumbnail_mime_type": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultMpeg4Gif: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "mpeg4_url": {
                "hinting": str
            },
            "thumbnail_url": {
                "hinting": str
            },
            "mpeg4_width": {
                "hinting": Optional[int],
                "val": None
            },
            "mpeg4_height": {
                "hinting": Optional[int],
                "val": None
            },
            "mpeg4_duration": {
                "hinting": Optional[int],
                "val": None
            },
            "thumbnail_mime_type": {
                "hinting": Optional[str],
                "val": None
            },
            "title": {
                "hinting": Optional[str],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_MPEG4_GIF
                }
            },
            "id": {
                "val": "ok."
            },
            "mpeg4_url": {
                "val": "ok."
            },
            "thumbnail_url": {
                "val": "ok."
            },
            "mpeg4_width": {
                "val": "ok."
            },
            "mpeg4_height": {
                "val": "ok."
            },
            "mpeg4_duration": {
                "val": "ok."
            },
            "thumbnail_mime_type": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultVideo: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "video_url": {
                "hinting": str
            },
            "mime_type": {
                "hinting": str
            },
            "thumbnail_url": {
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "video_width": {
                "hinting": Optional[int],
                "val": None
            },
            "video_height": {
                "hinting": Optional[int],
                "val": None
            },
            "video_duration": {
                "hinting": Optional[int],
                "val": None
            },
            "description": {
                "hinting": Optional[str],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_VIDEO
                }
            },
            "id": {
                "val": "ok."
            },
            "video_url": {
                "val": "ok."
            },
            "mime_type": {
                "val": "ok."
            },
            "thumbnail_url": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "video_width": {
                "val": "ok."
            },
            "video_height": {
                "val": "ok."
            },
            "video_duration": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultAudio: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "audio_url": {
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "performer": {
                "hinting": Optional[str],
                "val": None
            },
            "audio_duration": {
                "hinting": Optional[int],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_AUDIO
                }
            },
            "id": {
                "val": "ok."
            },
            "audio_url": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "performer": {
                "val": "ok."
            },
            "audio_duration": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultVoice: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "voice_url": {
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "voice_duration": {
                "hinting": Optional[int],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_VOICE
                }
            },
            "id": {
                "val": "ok."
            },
            "voice_url": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "voice_duration": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultDocument: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "document_url": {
                "hinting": str
            },
            "mime_type": {
                "hinting": str
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "description": {
                "hinting": Optional[str],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "val": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "val": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_DOCUMENT
                }
            },
            "id": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "document_url": {
                "val": "ok."
            },
            "mime_type": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            },
            "thumbnail_url": {
                "val": "ok."
            },
            "thumbnail_width": {
                "val": "ok."
            },
            "thumbnail_height": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultLocation: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "latitude": {
                "hinting": float
            },
            "longitude": {
                "hinting": float
            },
            "title": {
                "hinting": str
            },
            "horizontal_accuracy": {
                "hinting": Optional[float],
                "val": None
            },
            "live_period": {
                "hinting": Optional[int],
                "val": None
            },
            "heading": {
                "hinting": Optional[int],
                "val": None
            },
            "proximity_alert_radius": {
                "hinting": Optional[int],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "val": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "val": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_LOCATION
                }
            },
            "id": {
                "val": "ok."
            },
            "latitude": {
                "val": "ok."
            },
            "longitude": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "horizontal_accuracy": {
                "val": "ok."
            },
            "live_period": {
                "val": "ok."
            },
            "heading": {
                "val": "ok."
            },
            "proximity_alert_radius": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            },
            "thumbnail_url": {
                "val": "ok."
            },
            "thumbnail_width": {
                "val": "ok."
            },
            "thumbnail_height": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultVenue: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "latitude": {
                "hinting": float
            },
            "longitude": {
                "hinting": float
            },
            "title": {
                "hinting": str
            },
            "address": {
                "hinting": str
            },
            "foursquare_id": {
                "hinting": Optional[str],
                "val": None
            },
            "foursquare_type": {
                "hinting": Optional[str],
                "val": None
            },
            "google_place_id": {
                "hinting": Optional[str],
                "val": None
            },
            "google_place_type": {
                "hinting": Optional[str],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "val": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "val": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_VENUE
                }
            },
            "id": {
                "val": "ok."
            },
            "latitude": {
                "val": "ok."
            },
            "longitude": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "address": {
                "val": "ok."
            },
            "foursquare_id": {
                "val": "ok."
            },
            "foursquare_type": {
                "val": "ok."
            },
            "google_place_id": {
                "val": "ok."
            },
            "google_place_type": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            },
            "thumbnail_url": {
                "val": "ok."
            },
            "thumbnail_width": {
                "val": "ok."
            },
            "thumbnail_height": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultContact: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "phone_number": {
                "hinting": str
            },
            "first_name": {
                "hinting": str
            },
            "last_name": {
                "hinting": Optional[str],
                "val": None
            },
            "vcard": {
                "hinting": Optional[str],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "val": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "val": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_CONTACT
                }
            },
            "id": {
                "val": "ok."
            },
            "phone_number": {
                "val": "ok."
            },
            "first_name": {
                "val": "ok."
            },
            "last_name": {
                "val": "ok."
            },
            "vcard": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            },
            "thumbnail_url": {
                "val": "ok."
            },
            "thumbnail_width": {
                "val": "ok."
            },
            "thumbnail_height": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultGame: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "game_short_name": {
                "hinting": str
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_GAME
                }
            },
            "id": {
                "val": "ok."
            },
            "game_short_name": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultCachedPhoto: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "photo_file_id": {
                "hinting": str
            },
            "title": {
                "hinting": Optional[str],
                "val": None
            },
            "description": {
                "hinting": Optional[str],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_CACHED_PHOTO
                }
            },
            "id": {
                "val": "ok."
            },
            "photo_file_id": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultCachedGif: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "gif_file_id": {
                "hinting": str
            },
            "title": {
                "hinting": Optional[str],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_CACHED_GIF
                }
            },
            "id": {
                "val": "ok."
            },
            "gif_file_id": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultCachedMpeg4Gif: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "mpeg4_file_id": {
                "hinting": str
            },
            "title": {
                "hinting": Optional[str],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_CACHED_MPEG4_GIF
                }
            },
            "id": {
                "val": "ok."
            },
            "mpeg4_file_id": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultCachedSticker: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "sticker_file_id": {
                "hinting": str
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_CACHED_STICKER
                }
            },
            "id": {
                "val": "ok."
            },
            "sticker_file_id": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultCachedDocument: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "document_file_id": {
                "hinting": str
            },
            "description": {
                "hinting": Optional[str],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_CACHED_DOCUMENT
                }
            },
            "id": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "document_file_id": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultCachedVideo: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "video_file_id": {
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "description": {
                "hinting": Optional[str],
                "val": None
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_CACHED_VIDEO
                }
            },
            "id": {
                "val": "ok."
            },
            "video_file_id": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultCachedVoice: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "voice_file_id": {
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_CACHED_VOICE
                }
            },
            "id": {
                "val": "ok."
            },
            "voice_file_id": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
            }
        }
    },
    InlineQueryResultCachedAudio: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "audio_file_id": {
                "hinting": str
            },
            "caption": {
                "hinting": Optional[str],
                "val": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "val": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "val": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_INLINE_QUERY_RESULT_CACHED_AUDIO
                }
            },
            "id": {
                "val": "ok."
            },
            "audio_file_id": {
                "val": "ok."
            },
            "caption": {
                "val": "ok."
            },
            "parse_mode": {
                "val": "ok."
            },
            "caption_entities": {
                "val": "ok."
            },
            "reply_markup": {
                "val": "ok."
            },
            "input_message_content": {
                "val": "ok."
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
                "hinting": str
            },
            "from_user": {
                "hinting": User
            },
            "query": {
                "hinting": str
            },
            "location": {
                "hinting": Optional[Location],
                "val": None
            },
            "inline_message_id": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "result_id": {
                "val": "ok."
            },
            "from_user": {
                "val": "ok."
            },
            "query": {
                "val": "ok."
            },
            "location": {
                "val": "ok."
            },
            "inline_message_id": {
                "val": "ok."
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
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "inline_message_id": {
                "val": "ok."
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
                "hinting": str
            },
            "description": {
                "hinting": str
            },
            "start_parameter": {
                "hinting": str
            },
            "currency": {
                "hinting": str
            },
            "total_amount": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "title": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "start_parameter": {
                "val": "ok."
            },
            "currency": {
                "val": "ok."
            },
            "total_amount": {
                "val": "ok."
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
                "hinting": str
            },
            "state": {
                "hinting": str
            },
            "city": {
                "hinting": str
            },
            "street_line1": {
                "hinting": str
            },
            "street_line2": {
                "hinting": str
            },
            "post_code": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "country_code": {
                "val": "ok."
            },
            "state": {
                "val": "ok."
            },
            "city": {
                "val": "ok."
            },
            "street_line1": {
                "val": "ok."
            },
            "street_line2": {
                "val": "ok."
            },
            "post_code": {
                "val": "ok."
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
                "hinting": Optional[str],
                "val": None
            },
            "phone_number": {
                "hinting": Optional[str],
                "val": None
            },
            "email": {
                "hinting": Optional[str],
                "val": None
            },
            "shipping_address": {
                "hinting": Optional[ShippingAddress],
                "val": None
            }
        },
        "self_kwargs": {
            "name": {
                "val": "ok."
            },
            "phone_number": {
                "val": "ok."
            },
            "email": {
                "val": "ok."
            },
            "shipping_address": {
                "val": "ok."
            }
        }
    },
    ShippingOption: {
        "has_dese": False,
        "init_kwargs": {
            "id": {
                "hinting": str
            },
            "title": {
                "hinting": str
            },
            "prices": {
                "hinting": list[LabeledPrice]
            }
        },
        "self_kwargs": {
            "id": {
                "val": "ok."
            },
            "title": {
                "val": "ok."
            },
            "prices": {
                "val": "ok."
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
                "hinting": str
            },
            "total_amount": {
                "hinting": int
            },
            "invoice_payload": {
                "hinting": str
            },
            "telegram_payment_charge_id": {
                "hinting": str
            },
            "provider_payment_charge_id": {
                "hinting": str
            },
            "shipping_option_id": {
                "hinting": Optional[str],
                "val": None
            },
            "order_info": {
                "hinting": Optional[OrderInfo],
                "val": None
            }
        },
        "self_kwargs": {
            "currency": {
                "val": "ok."
            },
            "total_amount": {
                "val": "ok."
            },
            "invoice_payload": {
                "val": "ok."
            },
            "telegram_payment_charge_id": {
                "val": "ok."
            },
            "provider_payment_charge_id": {
                "val": "ok."
            },
            "shipping_option_id": {
                "val": "ok."
            },
            "order_info": {
                "val": "ok."
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
                "hinting": str
            },
            "from_user": {
                "hinting": User
            },
            "invoice_payload": {
                "hinting": str
            },
            "shipping_address": {
                "hinting": ShippingAddress
            }
        },
        "self_kwargs": {
            "id": {
                "val": "ok."
            },
            "from_user": {
                "val": "ok."
            },
            "invoice_payload": {
                "val": "ok."
            },
            "shipping_address": {
                "val": "ok."
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
                "hinting": str
            },
            "from_user": {
                "hinting": User
            },
            "currency": {
                "hinting": str
            },
            "total_amount": {
                "hinting": int
            },
            "invoice_payload": {
                "hinting": str
            },
            "shipping_option_id": {
                "hinting": Optional[str],
                "val": None
            },
            "order_info": {
                "hinting": Optional[OrderInfo],
                "val": None
            }
        },
        "self_kwargs": {
            "id": {
                "val": "ok."
            },
            "from_user": {
                "val": "ok."
            },
            "currency": {
                "val": "ok."
            },
            "total_amount": {
                "val": "ok."
            },
            "invoice_payload": {
                "val": "ok."
            },
            "shipping_option_id": {
                "val": "ok."
            },
            "order_info": {
                "val": "ok."
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
                "hinting": str
            },
            "file_unique_id": {
                "hinting": str
            },
            "file_size": {
                "hinting": int
            },
            "file_date": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "file_id": {
                "val": "ok."
            },
            "file_unique_id": {
                "val": "ok."
            },
            "file_size": {
                "val": "ok."
            },
            "file_date": {
                "val": "ok."
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
                "hinting": str
            },
            "hash": {
                "hinting": str
            },
            "data": {
                "hinting": Optional[str],
                "val": None
            },
            "phone_number": {
                "hinting": Optional[str],
                "val": None
            },
            "email": {
                "hinting": Optional[str],
                "val": None
            },
            "files": {
                "hinting": Optional[list[PassportFile]],
                "val": None
            },
            "front_side": {
                "hinting": Optional[PassportFile],
                "val": None
            },
            "reverse_side": {
                "hinting": Optional[PassportFile],
                "val": None
            },
            "selfie": {
                "hinting": Optional[PassportFile],
                "val": None
            },
            "translation": {
                "hinting": Optional[list[PassportFile]],
                "val": None
            }
        },
        "self_kwargs": {
            "type": {
                "val": "ok."
            },
            "hash": {
                "val": "ok."
            },
            "data": {
                "val": "ok."
            },
            "phone_number": {
                "val": "ok."
            },
            "email": {
                "val": "ok."
            },
            "files": {
                "val": "ok."
            },
            "front_side": {
                "val": "ok."
            },
            "reverse_side": {
                "val": "ok."
            },
            "selfie": {
                "val": "ok."
            },
            "translation": {
                "val": "ok."
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
                "hinting": str
            },
            "hash": {
                "hinting": str
            },
            "secret": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "data": {
                "val": "ok."
            },
            "hash": {
                "val": "ok."
            },
            "secret": {
                "val": "ok."
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
                "hinting": list[EncryptedPassportElement]
            },
            "credentials": {
                "hinting": EncryptedCredentials
            }
        },
        "self_kwargs": {
            "data": {
                "val": "ok."
            },
            "credentials": {
                "val": "ok."
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
                "hinting": str
            },
            "data_hash": {
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_PASSPORT_ELEMENT_ERROR_DATA_FIELD
                }
            },
            "type": {
                "val": "ok."
            },
            "field_name": {
                "val": "ok."
            },
            "data_hash": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
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
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_PASSPORT_ELEMENT_ERROR_FRONT_SIDE
                }
            },
            "type": {
                "val": "ok."
            },
            "file_hash": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
            }
        }
    },
    PassportElementErrorReverseSide: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal['driver_license', 'identity_card']
            },
            "file_hash": {
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_PASSPORT_ELEMENT_ERROR_REVERSE_SIDE
                }
            },
            "type": {
                "val": "ok."
            },
            "file_hash": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
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
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_PASSPORT_ELEMENT_ERROR_SELFIE
                }
            },
            "type": {
                "val": "ok."
            },
            "file_hash": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
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
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_PASSPORT_ELEMENT_ERROR_FILE
                }
            },
            "type": {
                "val": "ok."
            },
            "file_hash": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
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
                "hinting": list[str]
            },
            "message": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_PASSPORT_ELEMENT_ERROR_FILES
                }
            },
            "type": {
                "val": "ok."
            },
            "file_hashes": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
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
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILE
                }
            },
            "type": {
                "val": "ok."
            },
            "file_hash": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
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
                "hinting": list[str]
            },
            "message": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILES
                }
            },
            "type": {
                "val": "ok."
            },
            "file_hashes": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
            }
        }
    },
    PassportElementErrorUnspecified: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": str
            },
            "element_hash": {
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_PASSPORT_ELEMENT_ERROR_UNSPECIFIED
                }
            },
            "type": {
                "val": "ok."
            },
            "element_hash": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
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
                "hinting": str
            },
            "description": {
                "hinting": str
            },
            "photo": {
                "hinting": list[PhotoSize]
            },
            "text": {
                "hinting": Optional[str],
                "val": None
            },
            "text_entities": {
                "hinting": Optional[list[MessageEntity]],
                "val": None
            },
            "animation": {
                "hinting": Optional[Animation],
                "val": None
            }
        },
        "self_kwargs": {
            "title": {
                "val": "ok."
            },
            "description": {
                "val": "ok."
            },
            "photo": {
                "val": "ok."
            },
            "text": {
                "val": "ok."
            },
            "text_entities": {
                "val": "ok."
            },
            "animation": {
                "val": "ok."
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
                "hinting": int
            },
            "user": {
                "hinting": User
            },
            "score": {
                "hinting": int
            }
        },
        "self_kwargs": {
            "position": {
                "val": "ok."
            },
            "user": {
                "val": "ok."
            },
            "score": {
                "val": "ok."
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
                "hinting": Chat
            },
            "giveaway_message_id": {
                "hinting": int
            },
            "winners_selection_date": {
                "hinting": int
            },
            "winner_count": {
                "hinting": int
            },
            "winners": {
                "hinting": list[User]
            },
            "additional_chat_count": {
                "hinting": Optional[int],
                "val": None
            },
            "premium_subscription_month_count": {
                "hinting": Optional[int],
                "val": None
            },
            "unclaimed_prize_count": {
                "hinting": Optional[int],
                "val": None
            },
            "only_new_members": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "was_refunded": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "prize_description": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "chat": {
                "val": "ok."
            },
            "giveaway_message_id": {
                "val": "ok."
            },
            "winners_selection_date": {
                "val": "ok."
            },
            "winner_count": {
                "val": "ok."
            },
            "winners": {
                "val": "ok."
            },
            "additional_chat_count": {
                "val": "ok."
            },
            "premium_subscription_month_count": {
                "val": "ok."
            },
            "unclaimed_prize_count": {
                "val": "ok."
            },
            "only_new_members": {
                "val": "ok."
            },
            "was_refunded": {
                "val": "ok."
            },
            "prize_description": {
                "val": "ok."
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
                "hinting": int
            },
            "unclaimed_prize_count": {
                "hinting": Optional[int],
                "val": None
            },
            "giveaway_message": {
                "hinting": Optional[Message],
                "val": None
            }
        },
        "self_kwargs": {
            "winner_count": {
                "val": "ok."
            },
            "unclaimed_prize_count": {
                "val": "ok."
            },
            "giveaway_message": {
                "val": "ok."
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
                "hinting": list[Chat]
            },
            "winners_selection_date": {
                "hinting": int
            },
            "winner_count": {
                "hinting": int
            },
            "only_new_members": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "has_public_winners": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "prize_description": {
                "hinting": Optional[str],
                "val": None
            },
            "country_codes": {
                "hinting": Optional[list[str]],
                "val": None
            },
            "premium_subscription_month_count": {
                "hinting": Optional[int],
                "val": None
            }
        },
        "self_kwargs": {
            "chats": {
                "val": "ok."
            },
            "winners_selection_date": {
                "val": "ok."
            },
            "winner_count": {
                "val": "ok."
            },
            "only_new_members": {
                "val": "ok."
            },
            "has_public_winners": {
                "val": "ok."
            },
            "prize_description": {
                "val": "ok."
            },
            "country_codes": {
                "val": "ok."
            },
            "premium_subscription_month_count": {
                "val": "ok."
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
                "hinting": int
            },
            "sender_user": {
                "hinting": User
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_MESSAGE_ORIGIN_USER
                }
            },
            "date": {
                "val": "ok."
            },
            "sender_user": {
                "val": "ok."
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
                "hinting": int
            },
            "sender_user_name": {
                "hinting": str
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_MESSAGE_ORIGIN_HIDDEN_USER
                }
            },
            "date": {
                "val": "ok."
            },
            "sender_user_name": {
                "val": "ok."
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
                "hinting": int
            },
            "sender_chat": {
                "hinting": Chat
            },
            "author_signature": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_MESSAGE_ORIGIN_CHAT
                }
            },
            "date": {
                "val": "ok."
            },
            "sender_chat": {
                "val": "ok."
            },
            "author_signature": {
                "val": "ok."
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
                "hinting": int
            },
            "chat": {
                "hinting": Chat
            },
            "message_id": {
                "hinting": int
            },
            "author_signature": {
                "hinting": Optional[str],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "type": {
                    "val": DEFAULT_MESSAGE_ORIGIN_CHANNEL
                }
            },
            "date": {
                "val": "ok."
            },
            "chat": {
                "val": "ok."
            },
            "message_id": {
                "val": "ok."
            },
            "author_signature": {
                "val": "ok."
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
                "hinting": MessageOrigin
            },
            "chat": {
                "hinting": Optional[Chat],
                "val": None
            },
            "message_id": {
                "hinting": Optional[int],
                "val": None
            },
            "link_preview_options": {
                "hinting": Optional[LinkPreviewOptions],
                "val": None
            },
            "animation": {
                "hinting": Optional[Animation],
                "val": None
            },
            "audio": {
                "hinting": Optional[Audio],
                "val": None
            },
            "document": {
                "hinting": Optional[Document],
                "val": None
            },
            "photo": {
                "hinting": Optional[list[PhotoSize]],
                "val": None
            },
            "sticker": {
                "hinting": Optional[Sticker],
                "val": None
            },
            "story": {
                "hinting": Optional[Story],
                "val": None
            },
            "video": {
                "hinting": Optional[Video],
                "val": None
            },
            "video_note": {
                "hinting": Optional[VideoNote],
                "val": None
            },
            "voice": {
                "hinting": Optional[Voice],
                "val": None
            },
            "has_media_spoiler": {
                "hinting": Optional[Literal[True]],
                "val": None
            },
            "contact": {
                "hinting": Optional[Contact],
                "val": None
            },
            "dice": {
                "hinting": Optional[Dice],
                "val": None
            },
            "game": {
                "hinting": Optional[Game],
                "val": None
            },
            "giveaway": {
                "hinting": Optional[Giveaway],
                "val": None
            },
            "giveaway_winners": {
                "hinting": Optional[GiveawayWinners],
                "val": None
            },
            "invoice": {
                "hinting": Optional[Invoice],
                "val": None
            },
            "location": {
                "hinting": Optional[Location],
                "val": None
            },
            "poll": {
                "hinting": Optional[Poll],
                "val": None
            },
            "venue": {
                "hinting": Optional[Venue],
                "val": None
            }
        },
        "self_kwargs": {
            "origin": {
                "val": "ok."
            },
            "chat": {
                "val": "ok."
            },
            "message_id": {
                "val": "ok."
            },
            "link_preview_options": {
                "val": "ok."
            },
            "animation": {
                "val": "ok."
            },
            "audio": {
                "val": "ok."
            },
            "document": {
                "val": "ok."
            },
            "photo": {
                "val": "ok."
            },
            "sticker": {
                "val": "ok."
            },
            "story": {
                "val": "ok."
            },
            "video": {
                "val": "ok."
            },
            "video_note": {
                "val": "ok."
            },
            "voice": {
                "val": "ok."
            },
            "has_media_spoiler": {
                "val": "ok."
            },
            "contact": {
                "val": "ok."
            },
            "dice": {
                "val": "ok."
            },
            "game": {
                "val": "ok."
            },
            "giveaway": {
                "val": "ok."
            },
            "giveaway_winners": {
                "val": "ok."
            },
            "invoice": {
                "val": "ok."
            },
            "location": {
                "val": "ok."
            },
            "poll": {
                "val": "ok."
            },
            "venue": {
                "val": "ok."
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
                "hinting": User
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_CHAT_BOOST_SOURCE_PREMIUM
                }
            },
            "user": {
                "val": "ok."
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
                "hinting": User
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_CHAT_BOOST_SOURCE_GIFT_CODE
                }
            },
            "user": {
                "val": "ok."
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
                "hinting": int
            },
            "user": {
                "hinting": Optional[User],
                "val": None
            },
            "is_unclaimed": {
                "hinting": Optional[Literal[True]],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {
                "source": {
                    "val": DEFAULT_CHAT_BOOST_SOURCE_GIVEAWAY
                }
            },
            "giveaway_message_id": {
                "val": "ok."
            },
            "user": {
                "val": "ok."
            },
            "is_unclaimed": {
                "val": "ok."
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
                "hinting": str
            },
            "add_date": {
                "hinting": int
            },
            "expiration_date": {
                "hinting": int
            },
            "source": {
                "hinting": ChatBoostSource
            }
        },
        "self_kwargs": {
            "boost_id": {
                "val": "ok."
            },
            "add_date": {
                "val": "ok."
            },
            "expiration_date": {
                "val": "ok."
            },
            "source": {
                "val": "ok."
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
                "hinting": list[ChatBoost]
            }
        },
        "self_kwargs": {
            "boosts": {
                "val": "ok."
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
                "hinting": Chat
            },
            "boost": {
                "hinting": ChatBoost
            }
        },
        "self_kwargs": {
            "chat": {
                "val": "ok."
            },
            "boost": {
                "val": "ok."
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
                "hinting": Chat
            },
            "boost_id": {
                "hinting": str
            },
            "remove_date": {
                "hinting": int
            },
            "source": {
                "hinting": ChatBoostSource
            }
        },
        "self_kwargs": {
            "chat": {
                "val": "ok."
            },
            "boost_id": {
                "val": "ok."
            },
            "remove_date": {
                "val": "ok."
            },
            "source": {
                "val": "ok."
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
                "hinting": int
            },
            "message": {
                "hinting": Optional[Message],
                "val": None
            },
            "edited_message": {
                "hinting": Optional[Message],
                "val": None
            },
            "channel_post": {
                "hinting": Optional[Message],
                "val": None
            },
            "edited_channel_post": {
                "hinting": Optional[Message],
                "val": None
            },
            "message_reaction": {
                "hinting": Optional[MessageReactionUpdated],
                "val": None
            },
            "message_reaction_count": {
                "hinting": Optional[MessageReactionCountUpdated],
                "val": None
            },
            "inline_query": {
                "hinting": Optional[InlineQuery],
                "val": None
            },
            "chosen_inline_result": {
                "hinting": Optional[ChosenInlineResult],
                "val": None
            },
            "callback_query": {
                "hinting": Optional[CallbackQuery],
                "val": None
            },
            "shipping_query": {
                "hinting": Optional[ShippingQuery],
                "val": None
            },
            "pre_checkout_query": {
                "hinting": Optional[PreCheckoutQuery],
                "val": None
            },
            "poll": {
                "hinting": Optional[Poll],
                "val": None
            },
            "poll_answer": {
                "hinting": Optional[PollAnswer],
                "val": None
            },
            "my_chat_member": {
                "hinting": Optional[ChatMemberUpdated],
                "val": None
            },
            "chat_member": {
                "hinting": Optional[ChatMemberUpdated],
                "val": None
            },
            "chat_join_request": {
                "hinting": Optional[ChatJoinRequest],
                "val": None
            },
            "chat_boost": {
                "hinting": Optional[ChatBoostUpdated],
                "val": None
            },
            "removed_chat_boost": {
                "hinting": Optional[ChatBoostRemoved],
                "val": None
            }
        },
        "self_kwargs": {
            "warning": {},
            "update_id": {
                "val": "ok."
            },
            "message": {
                "val": "ok."
            },
            "edited_message": {
                "val": "ok."
            },
            "channel_post": {
                "val": "ok."
            },
            "edited_channel_post": {
                "val": "ok."
            },
            "message_reaction": {
                "val": "ok."
            },
            "message_reaction_count": {
                "val": "ok."
            },
            "inline_query": {
                "val": "ok."
            },
            "chosen_inline_result": {
                "val": "ok."
            },
            "callback_query": {
                "val": "ok."
            },
            "shipping_query": {
                "val": "ok."
            },
            "pre_checkout_query": {
                "val": "ok."
            },
            "poll": {
                "val": "ok."
            },
            "poll_answer": {
                "val": "ok."
            },
            "my_chat_member": {
                "val": "ok."
            },
            "chat_member": {
                "val": "ok."
            },
            "chat_join_request": {
                "val": "ok."
            },
            "chat_boost": {
                "val": "ok."
            },
            "removed_chat_boost": {
                "val": "ok."
            }
        }
    }
}

from inspect import isclass

from tglib.logger import get_logger
logger = get_logger('TypesChecker')

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
            if arg not in TYPES[k]['init_kwargs']:
                logger.warning('%s, %s: %s', k.__name__, arg, 'not in init_kwargs')
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
