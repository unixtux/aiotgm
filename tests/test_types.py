#!/bin/env python3

if __name__ != '__main__':
    import os
    raise OSError(f'{os.path.basename(__file__)} must be launched from __main__')

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
from tglib.constants import *

TYPES = {
    ChatBoostAdded: {
        "link": "https://core.telegram.org/bots/api#chatboostadded",
        "has_dese": True,
        "kwargs": {
            "boost_count": {
                "type_hint": int
            }
        }
    },
    ChatPermissions: {
        "link": "https://core.telegram.org/bots/api#chatpermissions",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ChatAdministratorRights: {
        "link": "https://core.telegram.org/bots/api#chatadministratorrights",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    SwitchInlineQueryChosenChat: {
        "link": "https://core.telegram.org/bots/api#switchinlinequerychosenchat",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    CallbackGame: {
        "link": "https://core.telegram.org/bots/api#callbackgame",
        "has_dese": True,
        "kwargs": {}
    },
    InputFile: {
        "link": "https://core.telegram.org/bots/api#inputfile",
        "has_dese": False,
        "kwargs": {
            "path": {
                "type_hint": str
            },
            "file_name": {
                "type_hint": Optional[str],
                "default": None,
                "warnings": [
                    "no match self.file_name = ..."
                ]
            },
            "hide_name": {
                "type_hint": bool,
                "default": False,
                "warnings": [
                    "no match self.hide_name = ..."
                ]
            }
        }
    },
    LoginUrl: {
        "link": "https://core.telegram.org/bots/api#loginurl",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    LabeledPrice: {
        "link": "https://core.telegram.org/bots/api#labeledprice",
        "has_dese": False,
        "kwargs": {
            "label": {
                "type_hint": str
            },
            "amount": {
                "type_hint": int
            }
        }
    },
    LinkPreviewOptions: {
        "link": "https://core.telegram.org/bots/api#linkpreviewoptions",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    User: {
        "link": "https://core.telegram.org/bots/api#user",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    MessageEntity: {
        "link": "https://core.telegram.org/bots/api#messageentity",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    TextQuote: {
        "link": "https://core.telegram.org/bots/api#textquote",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ReplyParameters: {
        "link": "https://core.telegram.org/bots/api#replyparameters",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    InaccessibleMessage: {
        "link": "https://core.telegram.org/bots/api#inaccessiblemessage",
        "has_dese": True,
        "kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "message_id": {
                "type_hint": int
            },
            "date": {
                "type_hint": int,
                "default": 0
            }
        }
    },
    Message: {
        "link": "https://core.telegram.org/bots/api#message",
        "has_dese": True,
        "kwargs": {
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
                "default": None,
                "warnings": [
                    "default value is: text or str() # If not text, it's str() instead of None"
                ]
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
        }
    },
    ChatPhoto: {
        "link": "https://core.telegram.org/bots/api#chatphoto",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Location: {
        "link": "https://core.telegram.org/bots/api#location",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ChatLocation: {
        "link": "https://core.telegram.org/bots/api#chatlocation",
        "has_dese": True,
        "kwargs": {
            "location": {
                "type_hint": Location
            },
            "address": {
                "type_hint": str
            }
        }
    },
    ReactionTypeEmoji: {
        "link": "https://core.telegram.org/bots/api#reactiontypeemoji",
        "has_dese": True,
        "kwargs": {
            "emoji": {
                "type_hint": str
            }
        },
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_REACTION_TYPE_EMOJI"
                ]
            }
        }
    },
    ReactionTypeCustomEmoji: {
        "link": "https://core.telegram.org/bots/api#reactiontypecustomemoji",
        "has_dese": True,
        "kwargs": {
            "custom_emoji_id": {
                "type_hint": str
            }
        },
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_REACTION_TYPE_CUSTOM_EMOJI"
                ]
            }
        }
    },
    Chat: {
        "link": "https://core.telegram.org/bots/api#chat",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    MessageReactionUpdated: {
        "link": "https://core.telegram.org/bots/api#messagereactionupdated",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ReactionCount: {
        "link": "https://core.telegram.org/bots/api#reactioncount",
        "has_dese": True,
        "kwargs": {
            "type": {
                "type_hint": ReactionType
            },
            "total_count": {
                "type_hint": int
            }
        }
    },
    MessageReactionCountUpdated: {
        "link": "https://core.telegram.org/bots/api#messagereactioncountupdated",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    MessageId: {
        "link": "https://core.telegram.org/bots/api#messageid",
        "has_dese": True,
        "kwargs": {
            "message_id": {
                "type_hint": int
            }
        }
    },
    PhotoSize: {
        "link": "https://core.telegram.org/bots/api#photosize",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Animation: {
        "link": "https://core.telegram.org/bots/api#animation",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Audio: {
        "link": "https://core.telegram.org/bots/api#audio",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Document: {
        "link": "https://core.telegram.org/bots/api#document",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Story: {
        "link": "https://core.telegram.org/bots/api#story",
        "has_dese": True,
        "kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "id": {
                "type_hint": int
            }
        }
    },
    Video: {
        "link": "https://core.telegram.org/bots/api#video",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    VideoNote: {
        "link": "https://core.telegram.org/bots/api#videonote",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Voice: {
        "link": "https://core.telegram.org/bots/api#voice",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Contact: {
        "link": "https://core.telegram.org/bots/api#contact",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Dice: {
        "link": "https://core.telegram.org/bots/api#dice",
        "has_dese": True,
        "kwargs": {
            "emoji": {
                "type_hint": str
            },
            "value": {
                "type_hint": int
            }
        }
    },
    PollOption: {
        "link": "https://core.telegram.org/bots/api#polloption",
        "has_dese": True,
        "kwargs": {
            "text": {
                "type_hint": str
            },
            "voter_count": {
                "type_hint": int
            }
        }
    },
    PollAnswer: {
        "link": "https://core.telegram.org/bots/api#pollanswer",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Poll: {
        "link": "https://core.telegram.org/bots/api#poll",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Venue: {
        "link": "https://core.telegram.org/bots/api#venue",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    WebAppData: {
        "link": "https://core.telegram.org/bots/api#webappdata",
        "has_dese": True,
        "kwargs": {
            "data": {
                "type_hint": str
            },
            "button_text": {
                "type_hint": str
            }
        }
    },
    ProximityAlertTriggered: {
        "link": "https://core.telegram.org/bots/api#proximityalerttriggered",
        "has_dese": True,
        "kwargs": {
            "traveler": {
                "type_hint": User
            },
            "watcher": {
                "type_hint": User
            },
            "distance": {
                "type_hint": int
            }
        }
    },
    MessageAutoDeleteTimerChanged: {
        "link": "https://core.telegram.org/bots/api#messageautodeletetimerchanged",
        "has_dese": True,
        "kwargs": {
            "message_auto_delete_time": {
                "type_hint": int
            }
        }
    },
    ForumTopicCreated: {
        "link": "https://core.telegram.org/bots/api#forumtopiccreated",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ForumTopicClosed: {
        "link": "https://core.telegram.org/bots/api#forumtopicclosed",
        "has_dese": True,
        "kwargs": {}
    },
    ForumTopicEdited: {
        "link": "https://core.telegram.org/bots/api#forumtopicedited",
        "has_dese": True,
        "kwargs": {
            "name": {
                "type_hint": Optional[str],
                "default": None
            },
            "icon_custom_emoji_id": {
                "type_hint": Optional[str],
                "default": None
            }
        }
    },
    ForumTopicReopened: {
        "link": "https://core.telegram.org/bots/api#forumtopicreopened",
        "has_dese": True,
        "kwargs": {}
    },
    GeneralForumTopicHidden: {
        "link": "https://core.telegram.org/bots/api#generalforumtopichidden",
        "has_dese": True,
        "kwargs": {}
    },
    GeneralForumTopicUnhidden: {
        "link": "https://core.telegram.org/bots/api#generalforumtopicunhidden",
        "has_dese": True,
        "kwargs": {}
    },
    UsersShared: {
        "link": "https://core.telegram.org/bots/api#usersshared",
        "has_dese": True,
        "kwargs": {
            "request_id": {
                "type_hint": int
            },
            "user_ids": {
                "type_hint": list[int]
            }
        }
    },
    ChatShared: {
        "link": "https://core.telegram.org/bots/api#chatshared",
        "has_dese": True,
        "kwargs": {
            "request_id": {
                "type_hint": int
            },
            "chat_id": {
                "type_hint": int
            }
        }
    },
    WriteAccessAllowed: {
        "link": "https://core.telegram.org/bots/api#writeaccessallowed",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    VideoChatScheduled: {
        "link": "https://core.telegram.org/bots/api#videochatscheduled",
        "has_dese": True,
        "kwargs": {
            "start_date": {
                "type_hint": int
            }
        }
    },
    VideoChatStarted: {
        "link": "https://core.telegram.org/bots/api#videochatstarted",
        "has_dese": True,
        "kwargs": {}
    },
    VideoChatEnded: {
        "link": "https://core.telegram.org/bots/api#videochatended",
        "has_dese": True,
        "kwargs": {
            "duration": {
                "type_hint": int
            }
        }
    },
    VideoChatParticipantsInvited: {
        "link": "https://core.telegram.org/bots/api#videochatparticipantsinvited",
        "has_dese": True,
        "kwargs": {
            "users": {
                "type_hint": list[User]
            }
        }
    },
    UserProfilePhotos: {
        "link": "https://core.telegram.org/bots/api#userprofilephotos",
        "has_dese": True,
        "kwargs": {
            "total_count": {
                "type_hint": int
            },
            "photos": {
                "type_hint": list[list[PhotoSize]]
            }
        }
    },
    File: {
        "link": "https://core.telegram.org/bots/api#file",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    WebAppInfo: {
        "link": "https://core.telegram.org/bots/api#webappinfo",
        "has_dese": True,
        "kwargs": {
            "url": {
                "type_hint": str
            }
        }
    },
    KeyboardButtonRequestUsers: {
        "link": "https://core.telegram.org/bots/api#keyboardbuttonrequestusers",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    KeyboardButtonRequestChat: {
        "link": "https://core.telegram.org/bots/api#keyboardbuttonrequestchat",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    KeyboardButtonPollType: {
        "link": "https://core.telegram.org/bots/api#keyboardbuttonpolltype",
        "has_dese": False,
        "kwargs": {
            "type": {
                "type_hint": Optional[str],
                "default": None
            }
        }
    },
    KeyboardButton: {
        "link": "https://core.telegram.org/bots/api#keyboardbutton",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    ReplyKeyboardMarkup: {
        "link": "https://core.telegram.org/bots/api#replykeyboardmarkup",
        "has_dese": False,
        "kwargs": {
            "keyboard": {
                "type_hint": Optional[list[list[KeyboardButton]]],
                "default": None,
                "warnings": [
                    "default value is: keyboard or []"
                ]
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
        }
    },
    ReplyKeyboardRemove: {
        "link": "https://core.telegram.org/bots/api#replykeyboardremove",
        "has_dese": False,
        "kwargs": {
            "selective": {
                "type_hint": Optional[bool],
                "default": None
            }
        },
        "warnings": {
            "remove_keyboard": {
                "type_hint": Literal[True],
                "warnings": [
                    "not in __init__()",
                    "default value is: True"
                ]
            }
        }
    },
    InlineKeyboardButton: {
        "link": "https://core.telegram.org/bots/api#inlinekeyboardbutton",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    InlineKeyboardMarkup: {
        "link": "https://core.telegram.org/bots/api#inlinekeyboardmarkup",
        "has_dese": True,
        "kwargs": {
            "inline_keyboard": {
                "type_hint": Optional[list[list[InlineKeyboardButton]]],
                "default": None,
                "warnings": [
                    "default value is: inline_keyboard or []"
                ]
            }
        }
    },
    CallbackQuery: {
        "link": "https://core.telegram.org/bots/api#callbackquery",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ForceReply: {
        "link": "https://core.telegram.org/bots/api#forcereply",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    ChatInviteLink: {
        "link": "https://core.telegram.org/bots/api#chatinvitelink",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ChatMemberOwner: {
        "link": "https://core.telegram.org/bots/api#chatmemberowner",
        "has_dese": True,
        "kwargs": {
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
        "warnings": {
            "status": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_CHAT_MEMBER_OWNER"
                ]
            }
        }
    },
    ChatMemberAdministrator: {
        "link": "https://core.telegram.org/bots/api#chatmemberadministrator",
        "has_dese": True,
        "kwargs": {
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
        "warnings": {
            "status": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_CHAT_MEMBER_ADMINISTRATOR"
                ]
            }
        }
    },
    ChatMemberMember: {
        "link": "https://core.telegram.org/bots/api#chatmembermember",
        "has_dese": True,
        "kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "warnings": {
            "status": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_CHAT_MEMBER_MEMBER"
                ]
            }
        }
    },
    ChatMemberRestricted: {
        "link": "https://core.telegram.org/bots/api#chatmemberrestricted",
        "has_dese": True,
        "kwargs": {
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
        "warnings": {
            "status": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_CHAT_MEMBER_RESTRICTED"
                ]
            }
        }
    },
    ChatMemberLeft: {
        "link": "https://core.telegram.org/bots/api#chatmemberleft",
        "has_dese": True,
        "kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "warnings": {
            "status": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_CHAT_MEMBER_LEFT"
                ]
            }
        }
    },
    ChatMemberBanned: {
        "link": "https://core.telegram.org/bots/api#chatmemberbanned",
        "has_dese": True,
        "kwargs": {
            "user": {
                "type_hint": User
            },
            "until_date": {
                "type_hint": int
            }
        },
        "warnings": {
            "status": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_CHAT_MEMBER_BANNED"
                ]
            }
        }
    },
    ChatMemberUpdated: {
        "link": "https://core.telegram.org/bots/api#chatmemberupdated",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ChatJoinRequest: {
        "link": "https://core.telegram.org/bots/api#chatjoinrequest",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ForumTopic: {
        "link": "https://core.telegram.org/bots/api#forumtopic",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    BotCommand: {
        "link": "https://core.telegram.org/bots/api#botcommand",
        "has_dese": True,
        "kwargs": {
            "command": {
                "type_hint": str
            },
            "description": {
                "type_hint": str
            }
        }
    },
    BotCommandScopeDefault: {
        "link": "https://core.telegram.org/bots/api#botcommandscopedefault",
        "has_dese": False,
        "kwargs": {},
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_BOT_COMMAND_SCOPE_DEFAULT"
                ]
            }
        }
    },
    BotCommandScopeAllPrivateChats: {
        "link": "https://core.telegram.org/bots/api#botcommandscopeallprivatechats",
        "has_dese": False,
        "kwargs": {},
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_BOT_COMMAND_SCOPE_ALL_PRIVATE_CHATS"
                ]
            }
        }
    },
    BotCommandScopeAllGroupChats: {
        "link": "https://core.telegram.org/bots/api#botcommandscopeallgroupchats",
        "has_dese": False,
        "kwargs": {},
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_BOT_COMMAND_SCOPE_ALL_GROUP_CHATS"
                ]
            }
        }
    },
    BotCommandScopeAllChatAdministrators: {
        "link": "https://core.telegram.org/bots/api#botcommandscopeallchatadministrators",
        "has_dese": False,
        "kwargs": {},
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_BOT_COMMAND_SCOPE_ALL_CHAT_ADMINISTRATORS"
                ]
            }
        }
    },
    BotCommandScopeChat: {
        "link": "https://core.telegram.org/bots/api#botcommandscopechat",
        "has_dese": False,
        "kwargs": {
            "chat_id": {
                "type_hint": Union[int, str]
            }
        },
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_BOT_COMMAND_SCOPE_CHAT"
                ]
            }
        }
    },
    BotCommandScopeChatAdministrators: {
        "link": "https://core.telegram.org/bots/api#botcommandscopechatadministrators",
        "has_dese": False,
        "kwargs": {
            "chat_id": {
                "type_hint": Union[int, str]
            }
        },
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_BOT_COMMAND_SCOPE_CHAT_ADMINISTRATORS"
                ]
            }
        }
    },
    BotCommandScopeChatMember: {
        "link": "https://core.telegram.org/bots/api#botcommandscopechatmember",
        "has_dese": False,
        "kwargs": {
            "chat_id": {
                "type_hint": Union[int, str]
            },
            "user_id": {
                "type_hint": int
            }
        },
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_BOT_COMMAND_SCOPE_CHAT_MEMBER"
                ]
            }
        }
    },
    BotName: {
        "link": "https://core.telegram.org/bots/api#botname",
        "has_dese": True,
        "kwargs": {
            "name": {
                "type_hint": str
            }
        }
    },
    BotDescription: {
        "link": "https://core.telegram.org/bots/api#botdescription",
        "has_dese": True,
        "kwargs": {
            "description": {
                "type_hint": str
            }
        }
    },
    BotShortDescription: {
        "link": "https://core.telegram.org/bots/api#botshortdescription",
        "has_dese": True,
        "kwargs": {
            "short_description": {
                "type_hint": str
            }
        }
    },
    MenuButtonCommands: {
        "link": "https://core.telegram.org/bots/api#menubuttoncommands",
        "has_dese": True,
        "kwargs": {},
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_MENU_BUTTON_COMMANDS"
                ]
            }
        }
    },
    MenuButtonWebApp: {
        "link": "https://core.telegram.org/bots/api#menubuttonwebapp",
        "has_dese": True,
        "kwargs": {
            "text": {
                "type_hint": str
            },
            "web_app": {
                "type_hint": WebAppInfo
            }
        },
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_MENU_BUTTON_WEB_APP"
                ]
            }
        }
    },
    MenuButtonDefault: {
        "link": "https://core.telegram.org/bots/api#menubuttondefault",
        "has_dese": True,
        "kwargs": {},
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_MENU_BUTTON_DEFAULT"
                ]
            }
        }
    },
    ResponseParameters: {
        "link": "https://core.telegram.org/bots/api#responseparameters",
        "has_dese": True,
        "kwargs": {
            "migrate_to_chat_id": {
                "type_hint": Optional[int],
                "default": None
            },
            "retry_after": {
                "type_hint": Optional[int],
                "default": None
            }
        }
    },
    InputMediaPhoto: {
        "link": "https://core.telegram.org/bots/api#inputmediaphoto",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INPUT_MEDIA_PHOTO"
                ]
            }
        }
    },
    InputMediaVideo: {
        "link": "https://core.telegram.org/bots/api#inputmediavideo",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INPUT_MEDIA_VIDEO"
                ]
            }
        }
    },
    InputMediaAnimation: {
        "link": "https://core.telegram.org/bots/api#inputmediaanimation",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INPUT_MEDIA_ANIMATION"
                ]
            }
        }
    },
    InputMediaAudio: {
        "link": "https://core.telegram.org/bots/api#inputmediaaudio",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INPUT_MEDIA_AUDIO"
                ]
            }
        }
    },
    InputMediaDocument: {
        "link": "https://core.telegram.org/bots/api#inputmediadocument",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INPUT_MEDIA_DOCUMENT"
                ]
            }
        }
    },
    MaskPosition: {
        "link": "https://core.telegram.org/bots/api#maskposition",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Sticker: {
        "link": "https://core.telegram.org/bots/api#sticker",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    StickerSet: {
        "link": "https://core.telegram.org/bots/api#stickerset",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    InputSticker: {
        "link": "https://core.telegram.org/bots/api#inputsticker",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    InlineQuery: {
        "link": "https://core.telegram.org/bots/api#inlinequery",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    InlineQueryResultsButton: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultsbutton",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    InputTextMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputtextmessagecontent",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    InputLocationMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputlocationmessagecontent",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    InputVenueMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputvenuemessagecontent",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    InputContactMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputcontactmessagecontent",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    InputInvoiceMessageContent: {
        "link": "https://core.telegram.org/bots/api#inputinvoicemessagecontent",
        "has_dese": False,
        "kwargs": {
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
        }
    },
    InlineQueryResultArticle: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultarticle",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_ARTICLE"
                ]
            }
        }
    },
    InlineQueryResultPhoto: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultphoto",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_PHOTO"
                ]
            }
        }
    },
    InlineQueryResultGif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultgif",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_GIF"
                ]
            }
        }
    },
    InlineQueryResultMpeg4Gif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_MPEG4_GIF"
                ]
            }
        }
    },
    InlineQueryResultVideo: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultvideo",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_VIDEO"
                ]
            }
        }
    },
    InlineQueryResultAudio: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultaudio",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_AUDIO"
                ]
            }
        }
    },
    InlineQueryResultVoice: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultvoice",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_VOICE"
                ]
            }
        }
    },
    InlineQueryResultDocument: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultdocument",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_DOCUMENT"
                ]
            }
        }
    },
    InlineQueryResultLocation: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultlocation",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_LOCATION"
                ]
            }
        }
    },
    InlineQueryResultVenue: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultvenue",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_VENUE"
                ]
            }
        }
    },
    InlineQueryResultContact: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcontact",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_CONTACT"
                ]
            }
        }
    },
    InlineQueryResultGame: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultgame",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_GAME"
                ]
            }
        }
    },
    InlineQueryResultCachedPhoto: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedphoto",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_CACHED_PHOTO"
                ]
            }
        }
    },
    InlineQueryResultCachedGif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedgif",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_CACHED_GIF"
                ]
            }
        }
    },
    InlineQueryResultCachedMpeg4Gif: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_CACHED_MPEG4_GIF"
                ]
            }
        }
    },
    InlineQueryResultCachedSticker: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedsticker",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_CACHED_STICKER"
                ]
            }
        }
    },
    InlineQueryResultCachedDocument: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcacheddocument",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_CACHED_DOCUMENT"
                ]
            }
        }
    },
    InlineQueryResultCachedVideo: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedvideo",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_CACHED_VIDEO"
                ]
            }
        }
    },
    InlineQueryResultCachedVoice: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedvoice",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_CACHED_VOICE"
                ]
            }
        }
    },
    InlineQueryResultCachedAudio: {
        "link": "https://core.telegram.org/bots/api#inlinequeryresultcachedaudio",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_INLINE_QUERY_RESULT_CACHED_AUDIO"
                ]
            }
        }
    },
    ChosenInlineResult: {
        "link": "https://core.telegram.org/bots/api#choseninlineresult",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    SentWebAppMessage: {
        "link": "https://core.telegram.org/bots/api#sentwebappmessage",
        "has_dese": True,
        "kwargs": {
            "inline_message_id": {
                "type_hint": Optional[str],
                "default": None
            }
        }
    },
    Invoice: {
        "link": "https://core.telegram.org/bots/api#invoice",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ShippingAddress: {
        "link": "https://core.telegram.org/bots/api#shippingaddress",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    OrderInfo: {
        "link": "https://core.telegram.org/bots/api#orderinfo",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ShippingOption: {
        "link": "https://core.telegram.org/bots/api#shippingoption",
        "has_dese": False,
        "kwargs": {
            "id": {
                "type_hint": str
            },
            "title": {
                "type_hint": str
            },
            "prices": {
                "type_hint": list[LabeledPrice]
            }
        }
    },
    SuccessfulPayment: {
        "link": "https://core.telegram.org/bots/api#successfulpayment",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ShippingQuery: {
        "link": "https://core.telegram.org/bots/api#shippingquery",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    PreCheckoutQuery: {
        "link": "https://core.telegram.org/bots/api#precheckoutquery",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    PassportFile: {
        "link": "https://core.telegram.org/bots/api#passportfile",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    EncryptedPassportElement: {
        "link": "https://core.telegram.org/bots/api#encryptedpassportelement",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    EncryptedCredentials: {
        "link": "https://core.telegram.org/bots/api#encryptedcredentials",
        "has_dese": True,
        "kwargs": {
            "data": {
                "type_hint": str
            },
            "hash": {
                "type_hint": str
            },
            "secret": {
                "type_hint": str
            }
        }
    },
    PassportData: {
        "link": "https://core.telegram.org/bots/api#passportdata",
        "has_dese": True,
        "kwargs": {
            "data": {
                "type_hint": list[EncryptedPassportElement]
            },
            "credentials": {
                "type_hint": EncryptedCredentials
            }
        }
    },
    PassportElementErrorDataField: {
        "link": "https://core.telegram.org/bots/api#passportelementerrordatafield",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_PASSPORT_ELEMENT_ERROR_DATA_FIELD"
                ]
            }
        }
    },
    PassportElementErrorFrontSide: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorfrontside",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_PASSPORT_ELEMENT_ERROR_FRONT_SIDE"
                ]
            }
        }
    },
    PassportElementErrorReverseSide: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorreverseside",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_PASSPORT_ELEMENT_ERROR_REVERSE_SIDE"
                ]
            }
        }
    },
    PassportElementErrorSelfie: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorselfie",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_PASSPORT_ELEMENT_ERROR_SELFIE"
                ]
            }
        }
    },
    PassportElementErrorFile: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorfile",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_PASSPORT_ELEMENT_ERROR_FILE"
                ]
            }
        }
    },
    PassportElementErrorFiles: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorfiles",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_PASSPORT_ELEMENT_ERROR_FILES"
                ]
            }
        }
    },
    PassportElementErrorTranslationFile: {
        "link": "https://core.telegram.org/bots/api#passportelementerrortranslationfile",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILE"
                ]
            }
        }
    },
    PassportElementErrorTranslationFiles: {
        "link": "https://core.telegram.org/bots/api#passportelementerrortranslationfiles",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILES"
                ]
            }
        }
    },
    PassportElementErrorUnspecified: {
        "link": "https://core.telegram.org/bots/api#passportelementerrorunspecified",
        "has_dese": False,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_PASSPORT_ELEMENT_ERROR_UNSPECIFIED"
                ]
            }
        }
    },
    Game: {
        "link": "https://core.telegram.org/bots/api#game",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    GameHighScore: {
        "link": "https://core.telegram.org/bots/api#gamehighscore",
        "has_dese": True,
        "kwargs": {
            "position": {
                "type_hint": int
            },
            "user": {
                "type_hint": User
            },
            "score": {
                "type_hint": int
            }
        }
    },
    GiveawayCreated: {
        "link": "https://core.telegram.org/bots/api#giveawaycreated",
        "has_dese": True,
        "kwargs": {}
    },
    GiveawayWinners: {
        "link": "https://core.telegram.org/bots/api#giveawaywinners",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    GiveawayCompleted: {
        "link": "https://core.telegram.org/bots/api#giveawaycompleted",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Giveaway: {
        "link": "https://core.telegram.org/bots/api#giveaway",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    MessageOriginUser: {
        "link": "https://core.telegram.org/bots/api#messageoriginuser",
        "has_dese": True,
        "kwargs": {
            "date": {
                "type_hint": int
            },
            "sender_user": {
                "type_hint": User
            }
        },
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_MESSAGE_ORIGIN_USER"
                ]
            }
        }
    },
    MessageOriginHiddenUser: {
        "link": "https://core.telegram.org/bots/api#messageoriginhiddenuser",
        "has_dese": True,
        "kwargs": {
            "date": {
                "type_hint": int
            },
            "sender_user_name": {
                "type_hint": str
            }
        },
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_MESSAGE_ORIGIN_HIDDEN_USER"
                ]
            }
        }
    },
    MessageOriginChat: {
        "link": "https://core.telegram.org/bots/api#messageoriginchat",
        "has_dese": True,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_MESSAGE_ORIGIN_CHAT"
                ]
            }
        }
    },
    MessageOriginChannel: {
        "link": "https://core.telegram.org/bots/api#messageoriginchannel",
        "has_dese": True,
        "kwargs": {
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
        "warnings": {
            "type": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_MESSAGE_ORIGIN_CHANNEL"
                ]
            }
        }
    },
    ExternalReplyInfo: {
        "link": "https://core.telegram.org/bots/api#externalreplyinfo",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    ChatBoostSourcePremium: {
        "link": "https://core.telegram.org/bots/api#chatboostsourcepremium",
        "has_dese": True,
        "kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_CHAT_BOOST_SOURCE_PREMIUM"
                ]
            }
        }
    },
    ChatBoostSourceGiftCode: {
        "link": "https://core.telegram.org/bots/api#chatboostsourcegiftcode",
        "has_dese": True,
        "kwargs": {
            "user": {
                "type_hint": User
            }
        },
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_CHAT_BOOST_SOURCE_GIFT_CODE"
                ]
            }
        }
    },
    ChatBoostSourceGiveaway: {
        "link": "https://core.telegram.org/bots/api#chatboostsourcegiveaway",
        "has_dese": True,
        "kwargs": {
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
        "warnings": {
            "source": {
                "warnings": [
                    "not in __init__()",
                    "default value is: DEFAULT_CHAT_BOOST_SOURCE_GIVEAWAY"
                ]
            }
        }
    },
    ChatBoost: {
        "link": "https://core.telegram.org/bots/api#chatboost",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    UserChatBoosts: {
        "link": "https://core.telegram.org/bots/api#userchatboosts",
        "has_dese": True,
        "kwargs": {
            "boosts": {
                "type_hint": list[ChatBoost]
            }
        }
    },
    ChatBoostUpdated: {
        "link": "https://core.telegram.org/bots/api#chatboostupdated",
        "has_dese": True,
        "kwargs": {
            "chat": {
                "type_hint": Chat
            },
            "boost": {
                "type_hint": ChatBoost
            }
        }
    },
    ChatBoostRemoved: {
        "link": "https://core.telegram.org/bots/api#chatboostremoved",
        "has_dese": True,
        "kwargs": {
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
        }
    },
    Update: {
        "link": "https://core.telegram.org/bots/api#update",
        "has_dese": True,
        "kwargs": {
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
        }
    }
}

from inspect import isclass

from tglib.logger import get_logger
logger = get_logger('TypesChecker')

logger.setLevel(20)

warnings = []

for type in TYPES:

    if not isclass(type):
        raise TypeError(
            f'Invalid key {type!r}: expected a type, got {type.__class__.__name__}.'
        )
    if not issubclass(type, TelegramType):
        raise TypeError(
            f'{type.__name__} is not a subclass of TelegramType.'
        )
    if 'warnings' in TYPES[type]:
        logger.debug('{!r}, {!r}'.format(type.__name__, TYPES[type]['warnings']))
        for arg in TYPES[type]['warnings']:
            warnings.append(f'{type.__name__}.{arg}: ' + ' & '.join(TYPES[type]['warnings'][arg]['warnings']))

    for arg in TYPES[type]['kwargs']:
        if 'warnings' in TYPES[type]['kwargs'][arg]:
            logger.debug('{!r}, {!r}, {!r}'.format(type.__name__, arg, TYPES[type]['kwargs'][arg]['warnings']))
            warnings.append(f'{type.__name__}.{arg}: ' + ' & '.join(TYPES[type]['kwargs'][arg]['warnings']))
        type_hint = TYPES[type]['kwargs'][arg]['type_hint']
        if type_hint.__name__ == 'Optional' and TYPES[type]['kwargs'][arg]['default'] is not None:
            raise ValueError(f"\n\nIn {type.__name__}, argument {arg!r} should be None by default, got {TYPES[type]['kwargs'][arg]['default']!r}")

if warnings:
    with open('types_warnings.txt', 'w') as w:
        w.write('\n'.join(warnings))
        logger.warning(f'{len(warnings)} warnings have been saved in "types_warnings.txt"')
else:
    logger.info(f'{len(warnings)} warnings')
