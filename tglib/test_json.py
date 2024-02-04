from typing import Optional
from tglib.types import *
from tglib.types import TelegramType

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
                "default_value": None
            },
            "can_send_audios": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_send_documents": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_send_photos": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_send_videos": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_send_video_notes": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_send_voice_notes": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_send_polls": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_send_other_messages": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_add_web_page_previews": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_change_info": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_invite_users": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_pin_messages": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_manage_topics": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "can_edit_messages": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_pin_messages": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_post_stories": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_edit_stories": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_delete_stories": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_manage_topics": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "allow_user_chats": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "allow_bot_chats": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "allow_group_chats": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "allow_channel_chats": {
                "hinting": Optional[bool],
                "default_value": None
            }
        }
    },
    CallbackGame: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
    },
    InputFile: {
        "has_dese": False,
        "init_kwargs": {
            "path": {
                "hinting": str
            },
            "file_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "hide_name": {
                "hinting": Optional[bool],
                "default_value": False
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
                "default_value": None
            },
            "bot_username": {
                "hinting": Optional[str],
                "default_value": None
            },
            "request_write_access": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "url": {
                "hinting": Optional[str],
                "default_value": None
            },
            "prefer_small_media": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "prefer_large_media": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "show_above_text": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "username": {
                "hinting": Optional[str],
                "default_value": None
            },
            "language_code": {
                "hinting": Optional[str],
                "default_value": None
            },
            "is_premium": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "added_to_attachment_menu": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "can_join_groups": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_read_all_group_messages": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "supports_inline_queries": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "user": {
                "hinting": Optional[User],
                "default_value": None
            },
            "language": {
                "hinting": Optional[str],
                "default_value": None
            },
            "custom_emoji_id": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            },
            "is_manual": {
                "hinting": Optional[Literal[True]],
                "default_value": None
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
                "default_value": None
            },
            "allow_sending_without_reply": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "quote": {
                "hinting": Optional[str],
                "default_value": None
            },
            "quote_parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "quote_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "quote_position": {
                "hinting": Optional[int],
                "default_value": None
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
            "c": {
                "hinting": None
            },
            "m": {
                "hinting": None
            },
            "d": {
                "hinting": None
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
            "forward_origin": None,
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
            "pinned_message": None,
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
            "m": {
                "hinting": None
            },
            "d": {
                "hinting": None
            },
            "c": {
                "hinting": None
            },
            "f": {
                "hinting": None
            },
            "s": {
                "hinting": None
            },
            "i": {
                "hinting": None
            },
            "r": {
                "hinting": None
            },
            "e": {
                "hinting": None
            },
            "q": {
                "hinting": None
            },
            "v": {
                "hinting": None
            },
            "h": {
                "hinting": None
            },
            "a": {
                "hinting": None
            },
            "t": {
                "hinting": None
            },
            "l": {
                "hinting": None
            },
            "p": {
                "hinting": None
            },
            "g": {
                "hinting": None
            },
            "n": {
                "hinting": None
            },
            "u": {
                "hinting": None
            },
            "w": {
                "hinting": None
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
                "default_value": None
            },
            "live_period": {
                "hinting": Optional[int],
                "default_value": None
            },
            "heading": {
                "hinting": Optional[int],
                "default_value": None
            },
            "proximity_alert_radius": {
                "hinting": Optional[int],
                "default_value": None
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
            "available_reactions": None,
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
                "default_value": None
            },
            "username": {
                "hinting": Optional[str],
                "default_value": None
            },
            "first_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "last_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "is_forum": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "photo": {
                "hinting": Optional[ChatPhoto],
                "default_value": None
            },
            "active_usernames": {
                "hinting": Optional[list[str]],
                "default_value": None
            },
            "available_reactions": {
                "hinting": Optional[list[ReactionType]],
                "default_value": None
            },
            "accent_color_id": {
                "hinting": Optional[int],
                "default_value": None
            },
            "background_custom_emoji_id": {
                "hinting": Optional[str],
                "default_value": None
            },
            "profile_accent_color_id": {
                "hinting": Optional[int],
                "default_value": None
            },
            "profile_background_custom_emoji_id": {
                "hinting": Optional[str],
                "default_value": None
            },
            "emoji_status_custom_emoji_id": {
                "hinting": Optional[str],
                "default_value": None
            },
            "emoji_status_expiration_date": {
                "hinting": Optional[int],
                "default_value": None
            },
            "bio": {
                "hinting": Optional[str],
                "default_value": None
            },
            "has_private_forwards": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "has_restricted_voice_and_video_messages": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "join_to_send_messages": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "join_by_request": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "description": {
                "hinting": Optional[str],
                "default_value": None
            },
            "invite_link": {
                "hinting": Optional[str],
                "default_value": None
            },
            "pinned_message": {
                "hinting": Optional[Message],
                "default_value": None
            },
            "permissions": {
                "hinting": Optional[ChatPermissions],
                "default_value": None
            },
            "slow_mode_delay": {
                "hinting": Optional[int],
                "default_value": None
            },
            "message_auto_delete_time": {
                "hinting": Optional[int],
                "default_value": None
            },
            "has_aggressive_anti_spam_enabled": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "has_hidden_members": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "has_protected_content": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "has_visible_history": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "sticker_set_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "can_set_sticker_set": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "linked_chat_id": {
                "hinting": Optional[int],
                "default_value": None
            },
            "location": {
                "hinting": Optional[ChatLocation],
                "default_value": None
            }
        }
    },
    MessageReactionUpdated: {
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "message_id": None,
            "date": None,
            "old_reaction": None,
            "new_reaction": None,
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
                "default_value": None
            },
            "actor_chat": {
                "hinting": Optional[Chat],
                "default_value": None
            }
        }
    },
    ReactionCount: {
        "has_dese": True,
        "dese_kwargs": {
            "type": None,
            "total_count": None
        },
        "init_kwargs": {
            "type": {
                "hinting": ReactionType
            },
            "total_count": {
                "hinting": int
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
                "default_value": None
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
                "default_value": None
            },
            "file_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "mime_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "file_size": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "title": {
                "hinting": Optional[str],
                "default_value": None
            },
            "file_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "mime_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "file_size": {
                "hinting": Optional[int],
                "default_value": None
            },
            "thumbnail": {
                "hinting": Optional[PhotoSize],
                "default_value": None
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
                "default_value": None
            },
            "file_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "mime_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "file_size": {
                "hinting": Optional[int],
                "default_value": None
            }
        }
    },
    Story: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
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
                "default_value": None
            },
            "file_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "mime_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "file_size": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "file_size": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "file_size": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "user_id": {
                "hinting": Optional[int],
                "default_value": None
            },
            "vcard": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            },
            "user": {
                "hinting": Optional[User],
                "default_value": None
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
                "default_value": None
            },
            "explanation": {
                "hinting": Optional[str],
                "default_value": None
            },
            "explanation_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "open_period": {
                "hinting": Optional[int],
                "default_value": None
            },
            "close_date": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "foursquare_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "google_place_id": {
                "hinting": Optional[str],
                "default_value": None
            },
            "google_place_type": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            }
        }
    },
    ForumTopicClosed: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
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
                "default_value": None
            },
            "icon_custom_emoji_id": {
                "hinting": Optional[str],
                "default_value": None
            }
        }
    },
    ForumTopicReopened: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
    },
    GeneralForumTopicHidden: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
    },
    GeneralForumTopicUnhidden: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
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
                "default_value": None
            },
            "web_app_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "from_attachment_menu": {
                "hinting": Optional[bool],
                "default_value": None
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
        }
    },
    VideoChatStarted: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
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
                "default_value": None
            },
            "file_path": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            },
            "user_is_premium": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "max_quantity": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "chat_has_username": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "chat_is_created": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "user_administrator_rights": {
                "hinting": Optional[ChatAdministratorRights],
                "default_value": None
            },
            "bot_administrator_rights": {
                "hinting": Optional[ChatAdministratorRights],
                "default_value": None
            },
            "bot_is_member": {
                "hinting": Optional[bool],
                "default_value": None
            }
        }
    },
    KeyboardButtonPollType: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            },
            "request_chat": {
                "hinting": Optional[KeyboardButtonRequestChat],
                "default_value": None
            },
            "request_contact": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "request_location": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "request_poll": {
                "hinting": Optional[KeyboardButtonPollType],
                "default_value": None
            },
            "web_app": {
                "hinting": Optional[WebAppInfo],
                "default_value": None
            }
        }
    },
    ReplyKeyboardMarkup: {
        "has_dese": False,
        "init_kwargs": {
            "keyboard": {
                "hinting": Optional[list[list[KeyboardButton]]],
                "default_value": None
            },
            "is_persistent": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "resize_keyboard": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "one_time_keyboard": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "input_field_placeholder": {
                "hinting": Optional[str],
                "default_value": None
            },
            "selective": {
                "hinting": Optional[bool],
                "default_value": None
            }
        }
    },
    ReplyKeyboardRemove: {
        "has_dese": False,
        "init_kwargs": {
            "selective": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "callback_data": {
                "hinting": Optional[str],
                "default_value": None
            },
            "web_app": {
                "hinting": Optional[WebAppInfo],
                "default_value": None
            },
            "login_url": {
                "hinting": Optional[LoginUrl],
                "default_value": None
            },
            "switch_inline_query": {
                "hinting": Optional[str],
                "default_value": None
            },
            "switch_inline_query_current_chat": {
                "hinting": Optional[str],
                "default_value": None
            },
            "switch_inline_query_chosen_chat": {
                "hinting": Optional[SwitchInlineQueryChosenChat],
                "default_value": None
            },
            "callback_game": {
                "hinting": Optional[CallbackGame],
                "default_value": None
            },
            "pay": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            }
        }
    },
    CallbackQuery: {
        "has_dese": True,
        "dese_kwargs": {
            "id": None,
            "from_user": User,
            "message": None,
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
                "default_value": None
            },
            "inline_message_id": {
                "hinting": Optional[str],
                "default_value": None
            },
            "data": {
                "hinting": Optional[str],
                "default_value": None
            },
            "game_short_name": {
                "hinting": Optional[str],
                "default_value": None
            }
        }
    },
    ForceReply: {
        "has_dese": False,
        "init_kwargs": {
            "force_reply": {
                "hinting": Literal[True],
                "default_value": True
            },
            "input_field_placeholder": {
                "hinting": Optional[str],
                "default_value": None
            },
            "selective": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "expire_date": {
                "hinting": Optional[int],
                "default_value": None
            },
            "member_limit": {
                "hinting": Optional[int],
                "default_value": None
            },
            "pending_join_request_count": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
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
                "default_value": None
            },
            "can_edit_messages": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_pin_messages": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_post_stories": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_edit_stories": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_delete_stories": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "can_manage_topics": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "custom_title": {
                "hinting": Optional[str],
                "default_value": None
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
        }
    },
    ChatMemberUpdated: {
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "from_user": User,
            "date": None,
            "old_chat_member": None,
            "new_chat_member": None,
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
                "default_value": None
            },
            "via_chat_folder_invite_link": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "invite_link": {
                "hinting": Optional[ChatInviteLink],
                "default_value": None
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
                "default_value": None
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
        }
    },
    BotCommandScopeDefault: {
        "has_dese": False,
        "init_kwargs": {}
    },
    BotCommandScopeAllPrivateChats: {
        "has_dese": False,
        "init_kwargs": {}
    },
    BotCommandScopeAllGroupChats: {
        "has_dese": False,
        "init_kwargs": {}
    },
    BotCommandScopeAllChatAdministrators: {
        "has_dese": False,
        "init_kwargs": {}
    },
    BotCommandScopeChat: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": {
                "hinting": Union[int, str]
            }
        }
    },
    BotCommandScopeChatAdministrators: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": {
                "hinting": Union[int, str]
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
        }
    },
    MenuButtonCommands: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
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
        }
    },
    MenuButtonDefault: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
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
                "default_value": None
            },
            "retry_after": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "has_spoiler": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "width": {
                "hinting": Optional[int],
                "default_value": None
            },
            "height": {
                "hinting": Optional[int],
                "default_value": None
            },
            "duration": {
                "hinting": Optional[int],
                "default_value": None
            },
            "supports_streaming": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "has_spoiler": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "width": {
                "hinting": Optional[int],
                "default_value": None
            },
            "height": {
                "hinting": Optional[int],
                "default_value": None
            },
            "duration": {
                "hinting": Optional[int],
                "default_value": None
            },
            "has_spoiler": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "duration": {
                "hinting": Optional[int],
                "default_value": None
            },
            "performer": {
                "hinting": Optional[str],
                "default_value": None
            },
            "title": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "disable_content_type_detection": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "emoji": {
                "hinting": Optional[str],
                "default_value": None
            },
            "set_name": {
                "hinting": Optional[str],
                "default_value": None
            },
            "premium_animation": {
                "hinting": Optional[File],
                "default_value": None
            },
            "mask_position": {
                "hinting": Optional[MaskPosition],
                "default_value": None
            },
            "custom_emoji_id": {
                "hinting": Optional[str],
                "default_value": None
            },
            "needs_repainting": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "file_size": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
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
                "default_value": None
            },
            "keywords": {
                "hinting": Optional[list[str]],
                "default_value": None
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
                "default_value": None
            },
            "location": {
                "hinting": Optional[Location],
                "default_value": None
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
                "default_value": None
            },
            "start_parameter": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            },
            "entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "link_preview_options": {
                "hinting": Optional[LinkPreviewOptions],
                "default_value": None
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
                "default_value": None
            },
            "live_period": {
                "hinting": Optional[int],
                "default_value": None
            },
            "heading": {
                "hinting": Optional[int],
                "default_value": None
            },
            "proximity_alert_radius": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "foursquare_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "google_place_id": {
                "hinting": Optional[str],
                "default_value": None
            },
            "google_place_type": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            },
            "vcard": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            },
            "suggested_tip_amounts": {
                "hinting": Optional[list[int]],
                "default_value": None
            },
            "provider_data": {
                "hinting": Optional[str],
                "default_value": None
            },
            "photo_url": {
                "hinting": Optional[str],
                "default_value": None
            },
            "photo_size": {
                "hinting": Optional[int],
                "default_value": None
            },
            "photo_width": {
                "hinting": Optional[int],
                "default_value": None
            },
            "photo_height": {
                "hinting": Optional[int],
                "default_value": None
            },
            "need_name": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "need_phone_number": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "need_email": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "need_shipping_address": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "send_phone_number_to_provider": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "send_email_to_provider": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "is_flexible": {
                "hinting": Optional[bool],
                "default_value": None
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
                "default_value": None
            },
            "url": {
                "hinting": Optional[str],
                "default_value": None
            },
            "hide_url": {
                "hinting": Optional[bool],
                "default_value": None
            },
            "description": {
                "hinting": Optional[str],
                "default_value": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "photo_height": {
                "hinting": Optional[int],
                "default_value": None
            },
            "title": {
                "hinting": Optional[str],
                "default_value": None
            },
            "description": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "gif_height": {
                "hinting": Optional[int],
                "default_value": None
            },
            "gif_duration": {
                "hinting": Optional[int],
                "default_value": None
            },
            "thumbnail_mime_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "title": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "mpeg4_height": {
                "hinting": Optional[int],
                "default_value": None
            },
            "mpeg4_duration": {
                "hinting": Optional[int],
                "default_value": None
            },
            "thumbnail_mime_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "title": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "video_width": {
                "hinting": Optional[int],
                "default_value": None
            },
            "video_height": {
                "hinting": Optional[int],
                "default_value": None
            },
            "video_duration": {
                "hinting": Optional[int],
                "default_value": None
            },
            "description": {
                "hinting": Optional[str],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "performer": {
                "hinting": Optional[str],
                "default_value": None
            },
            "audio_duration": {
                "hinting": Optional[int],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "voice_duration": {
                "hinting": Optional[int],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "description": {
                "hinting": Optional[str],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "live_period": {
                "hinting": Optional[int],
                "default_value": None
            },
            "heading": {
                "hinting": Optional[int],
                "default_value": None
            },
            "proximity_alert_radius": {
                "hinting": Optional[int],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "foursquare_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "google_place_id": {
                "hinting": Optional[str],
                "default_value": None
            },
            "google_place_type": {
                "hinting": Optional[str],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
            },
            "vcard": {
                "hinting": Optional[str],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
            },
            "thumbnail_url": {
                "hinting": Optional[str],
                "default_value": None
            },
            "thumbnail_width": {
                "hinting": Optional[int],
                "default_value": None
            },
            "thumbnail_height": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
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
                "default_value": None
            },
            "description": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "caption": {
                "hinting": Optional[str],
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "parse_mode": {
                "hinting": Optional[str],
                "default_value": None
            },
            "caption_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "reply_markup": {
                "hinting": Optional[InlineKeyboardMarkup],
                "default_value": None
            },
            "input_message_content": {
                "hinting": Optional[InputMessageContent],
                "default_value": None
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
                "default_value": None
            },
            "inline_message_id": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
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
                "default_value": None
            },
            "phone_number": {
                "hinting": Optional[str],
                "default_value": None
            },
            "email": {
                "hinting": Optional[str],
                "default_value": None
            },
            "shipping_address": {
                "hinting": Optional[ShippingAddress],
                "default_value": None
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
                "default_value": None
            },
            "order_info": {
                "hinting": Optional[OrderInfo],
                "default_value": None
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
                "default_value": None
            },
            "order_info": {
                "hinting": Optional[OrderInfo],
                "default_value": None
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
                "default_value": None
            },
            "phone_number": {
                "hinting": Optional[str],
                "default_value": None
            },
            "email": {
                "hinting": Optional[str],
                "default_value": None
            },
            "files": {
                "hinting": Optional[list[PassportFile]],
                "default_value": None
            },
            "front_side": {
                "hinting": Optional[PassportFile],
                "default_value": None
            },
            "reverse_side": {
                "hinting": Optional[PassportFile],
                "default_value": None
            },
            "selfie": {
                "hinting": Optional[PassportFile],
                "default_value": None
            },
            "translation": {
                "hinting": Optional[list[PassportFile]],
                "default_value": None
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
        }
    },
    PassportElementErrorDataField: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal[
            },
            "'": {
                "hinting": None
            },
            "]": {
                "hinting": None
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
        }
    },
    PassportElementErrorFrontSide: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal[
            },
            "'": {
                "hinting": None
            },
            "]": {
                "hinting": None
            },
            "file_hash": {
                "hinting": str
            },
            "message": {
                "hinting": str
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
        }
    },
    PassportElementErrorSelfie: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal[
            },
            "'": {
                "hinting": None
            },
            "]": {
                "hinting": None
            },
            "file_hash": {
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        }
    },
    PassportElementErrorFile: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal[
            },
            "'": {
                "hinting": None
            },
            "]": {
                "hinting": None
            },
            "file_hash": {
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        }
    },
    PassportElementErrorFiles: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal[
            },
            "'": {
                "hinting": None
            },
            "]": {
                "hinting": None
            },
            "file_hashes": {
                "hinting": list[str]
            },
            "message": {
                "hinting": str
            }
        }
    },
    PassportElementErrorTranslationFile: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal[
            },
            "'": {
                "hinting": None
            },
            "]": {
                "hinting": None
            },
            "file_hash": {
                "hinting": str
            },
            "message": {
                "hinting": str
            }
        }
    },
    PassportElementErrorTranslationFiles: {
        "has_dese": False,
        "init_kwargs": {
            "type": {
                "hinting": Literal[
            },
            "'": {
                "hinting": None
            },
            "]": {
                "hinting": None
            },
            "file_hashes": {
                "hinting": list[str]
            },
            "message": {
                "hinting": str
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
                "default_value": None
            },
            "text_entities": {
                "hinting": Optional[list[MessageEntity]],
                "default_value": None
            },
            "animation": {
                "hinting": Optional[Animation],
                "default_value": None
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
        }
    },
    GiveawayCreated: {
        "has_dese": True,
        "dese_kwargs": {},
        "init_kwargs": {}
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
                "default_value": None
            },
            "premium_subscription_month_count": {
                "hinting": Optional[int],
                "default_value": None
            },
            "unclaimed_prize_count": {
                "hinting": Optional[int],
                "default_value": None
            },
            "only_new_members": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "was_refunded": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "prize_description": {
                "hinting": Optional[str],
                "default_value": None
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
                "default_value": None
            },
            "giveaway_message": {
                "hinting": Optional[Message],
                "default_value": None
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
                "default_value": None
            },
            "has_public_winners": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "prize_description": {
                "hinting": Optional[str],
                "default_value": None
            },
            "country_codes": {
                "hinting": Optional[list[str]],
                "default_value": None
            },
            "premium_subscription_month_count": {
                "hinting": Optional[int],
                "default_value": None
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
                "default_value": None
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
                "default_value": None
            }
        }
    },
    ExternalReplyInfo: {
        "has_dese": True,
        "dese_kwargs": {
            "origin": None,
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
                "default_value": None
            },
            "message_id": {
                "hinting": Optional[int],
                "default_value": None
            },
            "link_preview_options": {
                "hinting": Optional[LinkPreviewOptions],
                "default_value": None
            },
            "animation": {
                "hinting": Optional[Animation],
                "default_value": None
            },
            "audio": {
                "hinting": Optional[Audio],
                "default_value": None
            },
            "document": {
                "hinting": Optional[Document],
                "default_value": None
            },
            "photo": {
                "hinting": Optional[list[PhotoSize]],
                "default_value": None
            },
            "sticker": {
                "hinting": Optional[Sticker],
                "default_value": None
            },
            "story": {
                "hinting": Optional[Story],
                "default_value": None
            },
            "video": {
                "hinting": Optional[Video],
                "default_value": None
            },
            "video_note": {
                "hinting": Optional[VideoNote],
                "default_value": None
            },
            "voice": {
                "hinting": Optional[Voice],
                "default_value": None
            },
            "has_media_spoiler": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            },
            "contact": {
                "hinting": Optional[Contact],
                "default_value": None
            },
            "dice": {
                "hinting": Optional[Dice],
                "default_value": None
            },
            "game": {
                "hinting": Optional[Game],
                "default_value": None
            },
            "giveaway": {
                "hinting": Optional[Giveaway],
                "default_value": None
            },
            "giveaway_winners": {
                "hinting": Optional[GiveawayWinners],
                "default_value": None
            },
            "invoice": {
                "hinting": Optional[Invoice],
                "default_value": None
            },
            "location": {
                "hinting": Optional[Location],
                "default_value": None
            },
            "poll": {
                "hinting": Optional[Poll],
                "default_value": None
            },
            "venue": {
                "hinting": Optional[Venue],
                "default_value": None
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
                "default_value": None
            },
            "is_unclaimed": {
                "hinting": Optional[Literal[True]],
                "default_value": None
            }
        }
    },
    ChatBoost: {
        "has_dese": True,
        "dese_kwargs": {
            "boost_id": None,
            "add_date": None,
            "expiration_date": None,
            "source": None
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
        }
    },
    ChatBoostRemoved: {
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "boost_id": None,
            "remove_date": None,
            "source": None
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
                "default_value": None
            },
            "edited_message": {
                "hinting": Optional[Message],
                "default_value": None
            },
            "channel_post": {
                "hinting": Optional[Message],
                "default_value": None
            },
            "edited_channel_post": {
                "hinting": Optional[Message],
                "default_value": None
            },
            "message_reaction": {
                "hinting": Optional[MessageReactionUpdated],
                "default_value": None
            },
            "message_reaction_count": {
                "hinting": Optional[MessageReactionCountUpdated],
                "default_value": None
            },
            "inline_query": {
                "hinting": Optional[InlineQuery],
                "default_value": None
            },
            "chosen_inline_result": {
                "hinting": Optional[ChosenInlineResult],
                "default_value": None
            },
            "callback_query": {
                "hinting": Optional[CallbackQuery],
                "default_value": None
            },
            "shipping_query": {
                "hinting": Optional[ShippingQuery],
                "default_value": None
            },
            "pre_checkout_query": {
                "hinting": Optional[PreCheckoutQuery],
                "default_value": None
            },
            "poll": {
                "hinting": Optional[Poll],
                "default_value": None
            },
            "poll_answer": {
                "hinting": Optional[PollAnswer],
                "default_value": None
            },
            "my_chat_member": {
                "hinting": Optional[ChatMemberUpdated],
                "default_value": None
            },
            "chat_member": {
                "hinting": Optional[ChatMemberUpdated],
                "default_value": None
            },
            "chat_join_request": {
                "hinting": Optional[ChatJoinRequest],
                "default_value": None
            },
            "chat_boost": {
                "hinting": Optional[ChatBoostUpdated],
                "default_value": None
            },
            "removed_chat_boost": {
                "hinting": Optional[ChatBoostRemoved],
                "default_value": None
            }
        }
    }
}

for k in TYPES:
    if not issubclass(k, TelegramType):
        raise TypeError(k)
