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
            "can_send_messages": Optional[bool] ,
            "can_send_audios": Optional[bool] ,
            "can_send_documents": Optional[bool] ,
            "can_send_photos": Optional[bool] ,
            "can_send_videos": Optional[bool] ,
            "can_send_video_notes": Optional[bool] ,
            "can_send_voice_notes": Optional[bool] ,
            "can_send_polls": Optional[bool] ,
            "can_send_other_messages": Optional[bool] ,
            "can_add_web_page_previews": Optional[bool] ,
            "can_change_info": Optional[bool] ,
            "can_invite_users": Optional[bool] ,
            "can_pin_messages": Optional[bool] ,
            "can_manage_topics": Optional[bool] 
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
            "is_anonymous": bool,,
            "can_manage_chat": bool,,
            "can_delete_messages": bool,,
            "can_manage_video_chats": bool,,
            "can_restrict_members": bool,,
            "can_promote_members": bool,,
            "can_change_info": bool,,
            "can_invite_users": bool,,
            "can_post_messages": Optional[bool] ,
            "can_edit_messages": Optional[bool] ,
            "can_pin_messages": Optional[bool] ,
            "can_post_stories": Optional[bool] ,
            "can_edit_stories": Optional[bool] ,
            "can_delete_stories": Optional[bool] ,
            "can_manage_topics": Optional[bool] 
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
            "query": Optional[str] ,
            "allow_user_chats": Optional[bool] ,
            "allow_bot_chats": Optional[bool] ,
            "allow_group_chats": Optional[bool] ,
            "allow_channel_chats": Optional[bool] 
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
            "path": str,,
            "file_name": Optional[str] ,
            "hide_name": Optional[bool] 
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
            "url": str,,
            "forward_text": Optional[str] ,
            "bot_username": Optional[str] ,
            "request_write_access": Optional[bool] 
        }
    },
    LabeledPrice: {
        "has_dese": False,
        "init_kwargs": {
            "label": str,,
            "amount": int
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
            "is_disabled": Optional[bool] ,
            "url": Optional[str] ,
            "prefer_small_media": Optional[bool] ,
            "prefer_large_media": Optional[bool] ,
            "show_above_text": Optional[bool] 
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
            "id": int,,
            "is_bot": bool,,
            "first_name": str,,
            "last_name": Optional[str] ,
            "username": Optional[str] ,
            "language_code": Optional[str] ,
            "is_premium": Optional[Literal[True]] ,
            "added_to_attachment_menu": Optional[Literal[True]] ,
            "can_join_groups": Optional[bool] ,
            "can_read_all_group_messages": Optional[bool] ,
            "supports_inline_queries": Optional[bool] 
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
            "type": str,,
            "offset": int,,
            "length": int,,
            "url": Optional[str] ,
            "user": Optional[User] ,
            "language": Optional[str] ,
            "custom_emoji_id": Optional[str] 
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
            "text": str,,
            "position": int,,
            "entities": Optional[list[MessageEntity]] ,
            "is_manual": Optional[Literal[True]] 
        }
    },
    ReplyParameters: {
        "has_dese": False,
        "init_kwargs": {
            "message_id": int,,
            "chat_id": Optional[Union[int, str]] ,
            "allow_sending_without_reply": Optional[bool] ,
            "quote": Optional[str] ,
            "quote_parse_mode": Optional[str] ,
            "quote_entities": Optional[list[MessageEntity]] ,
            "quote_position": Optional[int] 
        }
    },
    InaccessibleMessage: {
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "message_id": None,
            "date": None
        },
        "init_kwargs": {}
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
        "init_kwargs": {}
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
            "small_file_id": str,,
            "small_file_unique_id": str,,
            "big_file_id": str,,
            "big_file_unique_id": str
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
            "longitude": float,,
            "latitude": float,,
            "horizontal_accuracy": Optional[float] ,
            "live_period": Optional[int] ,
            "heading": Optional[int] ,
            "proximity_alert_radius": Optional[int] 
        }
    },
    ChatLocation: {
        "has_dese": True,
        "dese_kwargs": {
            "location": Location,
            "address": None
        },
        "init_kwargs": {
            "location": Location,,
            "address": str
        }
    },
    ReactionTypeEmoji: {
        "has_dese": True,
        "dese_kwargs": {
            "emoji": None
        },
        "init_kwargs": {
            "emoji": str
        }
    },
    ReactionTypeCustomEmoji: {
        "has_dese": True,
        "dese_kwargs": {
            "custom_emoji_id": None
        },
        "init_kwargs": {
            "custom_emoji_id": str
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
            "id": int,,
            "type": str,,
            "title": Optional[str] ,
            "username": Optional[str] ,
            "first_name": Optional[str] ,
            "last_name": Optional[str] ,
            "is_forum": Optional[Literal[True]] ,
            "photo": Optional[ChatPhoto] ,
            "active_usernames": Optional[list[str]] ,
            "available_reactions": Optional[list[ReactionType]] ,
            "accent_color_id": Optional[int] ,
            "background_custom_emoji_id": Optional[str] ,
            "profile_accent_color_id": Optional[int] ,
            "profile_background_custom_emoji_id": Optional[str] ,
            "emoji_status_custom_emoji_id": Optional[str] ,
            "emoji_status_expiration_date": Optional[int] ,
            "bio": Optional[str] ,
            "has_private_forwards": Optional[Literal[True]] ,
            "has_restricted_voice_and_video_messages": Optional[Literal[True]] ,
            "join_to_send_messages": Optional[Literal[True]] ,
            "join_by_request": Optional[Literal[True]] ,
            "description": Optional[str] ,
            "invite_link": Optional[str] ,
            "pinned_message": Optional[Message] ,
            "permissions": Optional[ChatPermissions] ,
            "slow_mode_delay": Optional[int] ,
            "message_auto_delete_time": Optional[int] ,
            "has_aggressive_anti_spam_enabled": Optional[Literal[True]] ,
            "has_hidden_members": Optional[Literal[True]] ,
            "has_protected_content": Optional[Literal[True]] ,
            "has_visible_history": Optional[Literal[True]] ,
            "sticker_set_name": Optional[str] ,
            "can_set_sticker_set": Optional[Literal[True]] ,
            "linked_chat_id": Optional[int] ,
            "location": Optional[ChatLocation] 
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
            "chat": Chat,,
            "message_id": int,,
            "date": int,,
            "old_reaction": list[ReactionType],,
            "new_reaction": list[ReactionType],,
            "user": Optional[User] ,
            "actor_chat": Optional[Chat] 
        }
    },
    ReactionCount: {
        "has_dese": True,
        "dese_kwargs": {
            "type": None,
            "total_count": None
        },
        "init_kwargs": {
            "type": ReactionType,,
            "total_count": int
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
            "chat": Chat,,
            "message_id": int,,
            "date": int,,
            "reactions": list[ReactionCount]
        }
    },
    MessageId: {
        "has_dese": True,
        "dese_kwargs": {
            "message_id": None
        },
        "init_kwargs": {
            "message_id": int
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
            "file_id": str,,
            "file_unique_id": str,,
            "width": int,,
            "height": int,,
            "file_size": Optional[int] 
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
            "file_id": str,,
            "file_unique_id": str,,
            "width": int,,
            "height": int,,
            "duration": int,,
            "thumbnail": Optional[PhotoSize] ,
            "file_name": Optional[str] ,
            "mime_type": Optional[str] ,
            "file_size": Optional[int] 
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
            "file_id": str,,
            "file_unique_id": str,,
            "duration": int,,
            "performer": Optional[str] ,
            "title": Optional[str] ,
            "file_name": Optional[str] ,
            "mime_type": Optional[str] ,
            "file_size": Optional[int] ,
            "thumbnail": Optional[PhotoSize] 
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
            "file_id": str,,
            "file_unique_id": str,,
            "thumbnail": Optional[PhotoSize] ,
            "file_name": Optional[str] ,
            "mime_type": Optional[str] ,
            "file_size": Optional[int] 
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
            "file_id": str,,
            "file_unique_id": str,,
            "width": int,,
            "height": int,,
            "duration": int,,
            "thumbnail": Optional[PhotoSize] ,
            "file_name": Optional[str] ,
            "mime_type": Optional[str] ,
            "file_size": Optional[int] 
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
            "file_id": str,,
            "file_unique_id": str,,
            "length": int,,
            "duration": int,,
            "thumbnail": Optional[PhotoSize] ,
            "file_size": Optional[int] 
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
            "file_id": str,,
            "file_unique_id": str,,
            "duration": int,,
            "mime_type": Optional[str] ,
            "file_size": Optional[int] 
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
            "phone_number": str,,
            "first_name": str,,
            "last_name": Optional[str] ,
            "user_id": Optional[int] ,
            "vcard": Optional[str] 
        }
    },
    Dice: {
        "has_dese": True,
        "dese_kwargs": {
            "emoji": None,
            "value": None
        },
        "init_kwargs": {
            "emoji": str,,
            "value": int
        }
    },
    PollOption: {
        "has_dese": True,
        "dese_kwargs": {
            "text": None,
            "voter_count": None
        },
        "init_kwargs": {
            "text": str,,
            "voter_count": int
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
            "poll_id": str,,
            "option_ids": list[int],,
            "voter_chat": Optional[Chat] ,
            "user": Optional[User] 
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
            "id": str,,
            "question": str,,
            "options": list[PollOption],,
            "total_voter_count": int,,
            "is_closed": bool,,
            "is_anonymous": bool,,
            "type": str,,
            "allows_multiple_answers": bool,,
            "correct_option_id": Optional[int] ,
            "explanation": Optional[str] ,
            "explanation_entities": Optional[list[MessageEntity]] ,
            "open_period": Optional[int] ,
            "close_date": Optional[int] 
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
            "location": Location,,
            "title": str,,
            "address": str,,
            "foursquare_id": Optional[str] ,
            "foursquare_type": Optional[str] ,
            "google_place_id": Optional[str] ,
            "google_place_type": Optional[str] 
        }
    },
    WebAppData: {
        "has_dese": True,
        "dese_kwargs": {
            "data": None,
            "button_text": None
        },
        "init_kwargs": {
            "data": str,,
            "button_text": str
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
            "traveler": User,,
            "watcher": User,,
            "distance": int
        }
    },
    MessageAutoDeleteTimerChanged: {
        "has_dese": True,
        "dese_kwargs": {
            "message_auto_delete_time": None
        },
        "init_kwargs": {
            "message_auto_delete_time": int
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
            "name": str,,
            "icon_color": int,,
            "icon_custom_emoji_id": Optional[str] 
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
            "name": Optional[str] ,
            "icon_custom_emoji_id": Optional[str] 
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
            "request_id": int,,
            "user_ids": list[int]
        }
    },
    ChatShared: {
        "has_dese": True,
        "dese_kwargs": {
            "request_id": None,
            "chat_id": None
        },
        "init_kwargs": {
            "request_id": int,,
            "chat_id": int
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
            "from_request": Optional[bool] ,
            "web_app_name": Optional[str] ,
            "from_attachment_menu": Optional[bool] 
        }
    },
    VideoChatScheduled: {
        "has_dese": True,
        "dese_kwargs": {
            "start_date": None
        },
        "init_kwargs": {
            "start_date": int
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
            "duration": int
        }
    },
    VideoChatParticipantsInvited: {
        "has_dese": True,
        "dese_kwargs": {
            "users": list[User]
        },
        "init_kwargs": {
            "users": list[User]
        }
    },
    UserProfilePhotos: {
        "has_dese": True,
        "dese_kwargs": {
            "total_count": None,
            "photos": list[list[PhotoSize]]
        },
        "init_kwargs": {
            "total_count": int,,
            "photos": list[list[PhotoSize]]
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
            "file_id": str,,
            "file_unique_id": str,,
            "file_size": Optional[int] ,
            "file_path": Optional[str] 
        }
    },
    WebAppInfo: {
        "has_dese": True,
        "dese_kwargs": {
            "url": None
        },
        "init_kwargs": {
            "url": str
        }
    },
    KeyboardButtonRequestUsers: {
        "has_dese": False,
        "init_kwargs": {
            "request_id": int,,
            "user_is_bot": Optional[bool] ,
            "user_is_premium": Optional[bool] ,
            "max_quantity": Optional[int] 
        }
    },
    KeyboardButtonRequestChat: {
        "has_dese": False,
        "init_kwargs": {
            "request_id": int,,
            "chat_is_channel": bool,,
            "chat_is_forum": Optional[bool] ,
            "chat_has_username": Optional[bool] ,
            "chat_is_created": Optional[bool] ,
            "user_administrator_rights": Optional[ChatAdministratorRights] ,
            "bot_administrator_rights": Optional[ChatAdministratorRights] ,
            "bot_is_member": Optional[bool] 
        }
    },
    KeyboardButtonPollType: {
        "has_dese": False,
        "init_kwargs": {
            "type": Optional[str] 
        }
    },
    KeyboardButton: {
        "has_dese": False,
        "init_kwargs": {
            "text": str,,
            "request_users": Optional[KeyboardButtonRequestUsers] ,
            "request_chat": Optional[KeyboardButtonRequestChat] ,
            "request_contact": Optional[bool] ,
            "request_location": Optional[bool] ,
            "request_poll": Optional[KeyboardButtonPollType] ,
            "web_app": Optional[WebAppInfo] 
        }
    },
    ReplyKeyboardMarkup: {
        "has_dese": False,
        "init_kwargs": {
            "keyboard": Optional[list[list[KeyboardButton]]] ,
            "is_persistent": Optional[bool] ,
            "resize_keyboard": Optional[bool] ,
            "one_time_keyboard": Optional[bool] ,
            "input_field_placeholder": Optional[str] ,
            "selective": Optional[bool] 
        }
    },
    ReplyKeyboardRemove: {
        "has_dese": False,
        "init_kwargs": {
            "selective": Optional[bool] 
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
            "text": str,,
            "url": Optional[str] ,
            "callback_data": Optional[str] ,
            "web_app": Optional[WebAppInfo] ,
            "login_url": Optional[LoginUrl] ,
            "switch_inline_query": Optional[str] ,
            "switch_inline_query_current_chat": Optional[str] ,
            "switch_inline_query_chosen_chat": Optional[SwitchInlineQueryChosenChat] ,
            "callback_game": Optional[CallbackGame] ,
            "pay": Optional[bool] 
        }
    },
    InlineKeyboardMarkup: {
        "has_dese": True,
        "dese_kwargs": {
            "inline_keyboard": list[list[InlineKeyboardButton]]
        },
        "init_kwargs": {
            "inline_keyboard": Optional[list[list[InlineKeyboardButton]]] 
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
            "id": str,,
            "from_user": User,,
            "chat_instance": str,,
            "message": Optional[MaybeInaccessibleMessage] ,
            "inline_message_id": Optional[str] ,
            "data": Optional[str] ,
            "game_short_name": Optional[str] 
        }
    },
    ForceReply: {
        "has_dese": False,
        "init_kwargs": None
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
            "invite_link": str,,
            "creator": User,,
            "creates_join_request": bool,,
            "is_primary": bool,,
            "is_revoked": bool,,
            "name": Optional[str] ,
            "expire_date": Optional[int] ,
            "member_limit": Optional[int] ,
            "pending_join_request_count": Optional[int] 
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
            "user": User,,
            "is_anonymous": bool,,
            "custom_title": Optional[str] 
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
            "user": User,,
            "can_be_edited": bool,,
            "is_anonymous": bool,,
            "can_manage_chat": bool,,
            "can_delete_messages": bool,,
            "can_manage_video_chats": bool,,
            "can_restrict_members": bool,,
            "can_promote_members": bool,,
            "can_change_info": bool,,
            "can_invite_users": bool,,
            "can_post_messages": Optional[bool] ,
            "can_edit_messages": Optional[bool] ,
            "can_pin_messages": Optional[bool] ,
            "can_post_stories": Optional[bool] ,
            "can_edit_stories": Optional[bool] ,
            "can_delete_stories": Optional[bool] ,
            "can_manage_topics": Optional[bool] ,
            "custom_title": Optional[str] 
        }
    },
    ChatMemberMember: {
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": User
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
            "user": User,,
            "is_member": bool,,
            "can_send_messages": bool,,
            "can_send_audios": bool,,
            "can_send_documents": bool,,
            "can_send_photos": bool,,
            "can_send_videos": bool,,
            "can_send_video_notes": bool,,
            "can_send_voice_notes": bool,,
            "can_send_polls": bool,,
            "can_send_other_messages": bool,,
            "can_add_web_page_previews": bool,,
            "can_change_info": bool,,
            "can_invite_users": bool,,
            "can_pin_messages": bool,,
            "can_manage_topics": bool,,
            "until_date": int
        }
    },
    ChatMemberLeft: {
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": User
        }
    },
    ChatMemberBanned: {
        "has_dese": True,
        "dese_kwargs": {
            "user": User,
            "until_date": None
        },
        "init_kwargs": {
            "user": User,,
            "until_date": int
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
            "chat": Chat,,
            "from_user": User,,
            "date": int,,
            "old_chat_member": list[ChatMember],,
            "new_chat_member": list[ChatMember],,
            "invite_link": Optional[ChatInviteLink] ,
            "via_chat_folder_invite_link": Optional[bool] 
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
            "chat": Chat,,
            "from_user": User,,
            "user_chat_id": int,,
            "date": int,,
            "bio": Optional[str] ,
            "invite_link": Optional[ChatInviteLink] 
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
            "message_thread_id": int,,
            "name": str,,
            "icon_color": int,,
            "icon_custom_emoji_id": Optional[str] 
        }
    },
    BotCommand: {
        "has_dese": True,
        "dese_kwargs": {
            "command": None,
            "description": None
        },
        "init_kwargs": {
            "command": str,,
            "description": str
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
            "chat_id": Union[int, str]
        }
    },
    BotCommandScopeChatAdministrators: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": Union[int, str]
        }
    },
    BotCommandScopeChatMember: {
        "has_dese": False,
        "init_kwargs": {
            "chat_id": Union[int, str],,
            "user_id": int
        }
    },
    BotName: {
        "has_dese": True,
        "dese_kwargs": {
            "name": None
        },
        "init_kwargs": {
            "name": str
        }
    },
    BotDescription: {
        "has_dese": True,
        "dese_kwargs": {
            "description": None
        },
        "init_kwargs": {
            "description": str
        }
    },
    BotShortDescription: {
        "has_dese": True,
        "dese_kwargs": {
            "short_description": None
        },
        "init_kwargs": {
            "short_description": str
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
            "text": str,,
            "web_app": WebAppInfo
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
            "migrate_to_chat_id": Optional[int] ,
            "retry_after": Optional[int] 
        }
    },
    InputMediaPhoto: {
        "has_dese": False,
        "init_kwargs": {
            "media": str,,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "has_spoiler": Optional[bool] 
        }
    },
    InputMediaVideo: {
        "has_dese": False,
        "init_kwargs": {
            "media": str,,
            "thumbnail": Optional[Union[InputFile, str]] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "width": Optional[int] ,
            "height": Optional[int] ,
            "duration": Optional[int] ,
            "supports_streaming": Optional[bool] ,
            "has_spoiler": Optional[bool] 
        }
    },
    InputMediaAnimation: {
        "has_dese": False,
        "init_kwargs": {
            "media": str,,
            "thumbnail": Optional[Union[InputFile, str]] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "width": Optional[int] ,
            "height": Optional[int] ,
            "duration": Optional[int] ,
            "has_spoiler": Optional[bool] 
        }
    },
    InputMediaAudio: {
        "has_dese": False,
        "init_kwargs": {
            "media": str,,
            "thumbnail": Optional[Union[InputFile, str]] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "duration": Optional[int] ,
            "performer": Optional[str] ,
            "title": Optional[str] 
        }
    },
    InputMediaDocument: {
        "has_dese": False,
        "init_kwargs": {
            "media": str,,
            "thumbnail": Optional[Union[InputFile, str]] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "disable_content_type_detection": Optional[bool] 
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
            "point": str,,
            "x_shift": float,,
            "y_shift": float,,
            "scale": float
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
            "file_id": str,,
            "file_unique_id": str,,
            "type": str,,
            "width": int,,
            "height": int,,
            "is_animated": bool,,
            "is_video": bool,,
            "thumbnail": Optional[PhotoSize] ,
            "emoji": Optional[str] ,
            "set_name": Optional[str] ,
            "premium_animation": Optional[File] ,
            "mask_position": Optional[MaskPosition] ,
            "custom_emoji_id": Optional[str] ,
            "needs_repainting": Optional[Literal[True]] ,
            "file_size": Optional[int] 
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
            "name": str,,
            "title": str,,
            "sticker_type": str,,
            "is_animated": bool,,
            "is_video": bool,,
            "stickers": list[Sticker],,
            "thumbnail": Optional[PhotoSize] 
        }
    },
    InputSticker: {
        "has_dese": False,
        "init_kwargs": {
            "sticker": Union[InputFile, str],,
            "emoji_list": list[str],,
            "mask_position": Optional[MaskPosition] ,
            "keywords": Optional[list[str]] 
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
            "id": str,,
            "from_user": User,,
            "query": str,,
            "offset": str,,
            "chat_type": Optional[str] ,
            "location": Optional[Location] 
        }
    },
    InlineQueryResultsButton: {
        "has_dese": False,
        "init_kwargs": {
            "text": str,,
            "web_app": Optional[WebAppInfo] ,
            "start_parameter": Optional[str] 
        }
    },
    InputTextMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "message_text": str,,
            "parse_mode": Optional[str] ,
            "entities": Optional[list[MessageEntity]] ,
            "link_preview_options": Optional[LinkPreviewOptions] 
        }
    },
    InputLocationMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "latitude": float,,
            "longitude": float,,
            "horizontal_accuracy": Optional[float] ,
            "live_period": Optional[int] ,
            "heading": Optional[int] ,
            "proximity_alert_radius": Optional[int] 
        }
    },
    InputVenueMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "latitude": float,,
            "longitude": float,,
            "title": str,,
            "address": str,,
            "foursquare_id": Optional[str] ,
            "foursquare_type": Optional[str] ,
            "google_place_id": Optional[str] ,
            "google_place_type": Optional[str] 
        }
    },
    InputContactMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "phone_number": str,,
            "first_name": str,,
            "last_name": Optional[str] ,
            "vcard": Optional[str] 
        }
    },
    InputInvoiceMessageContent: {
        "has_dese": False,
        "init_kwargs": {
            "title": str,,
            "description": str,,
            "payload": str,,
            "provider_token": str,,
            "currency": str,,
            "prices": list[LabeledPrice],,
            "max_tip_amount": Optional[int] ,
            "suggested_tip_amounts": Optional[list[int]] ,
            "provider_data": Optional[str] ,
            "photo_url": Optional[str] ,
            "photo_size": Optional[int] ,
            "photo_width": Optional[int] ,
            "photo_height": Optional[int] ,
            "need_name": Optional[bool] ,
            "need_phone_number": Optional[bool] ,
            "need_email": Optional[bool] ,
            "need_shipping_address": Optional[bool] ,
            "send_phone_number_to_provider": Optional[bool] ,
            "send_email_to_provider": Optional[bool] ,
            "is_flexible": Optional[bool] 
        }
    },
    InlineQueryResultArticle: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "title": str,,
            "input_message_content": InputMessageContent,,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "url": Optional[str] ,
            "hide_url": Optional[bool] ,
            "description": Optional[str] ,
            "thumbnail_url": Optional[str] ,
            "thumbnail_width": Optional[int] ,
            "thumbnail_height": Optional[int] 
        }
    },
    InlineQueryResultPhoto: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "photo_url": str,,
            "thumbnail_url": str,,
            "photo_width": Optional[int] ,
            "photo_height": Optional[int] ,
            "title": Optional[str] ,
            "description": Optional[str] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultGif: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "gif_url": str,,
            "thumbnail_url": str,,
            "gif_width": Optional[int] ,
            "gif_height": Optional[int] ,
            "gif_duration": Optional[int] ,
            "thumbnail_mime_type": Optional[str] ,
            "title": Optional[str] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultMpeg4Gif: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "mpeg4_url": str,,
            "thumbnail_url": str,,
            "mpeg4_width": Optional[int] ,
            "mpeg4_height": Optional[int] ,
            "mpeg4_duration": Optional[int] ,
            "thumbnail_mime_type": Optional[str] ,
            "title": Optional[str] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultVideo: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "video_url": str,,
            "mime_type": str,,
            "thumbnail_url": str,,
            "title": str,,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "video_width": Optional[int] ,
            "video_height": Optional[int] ,
            "video_duration": Optional[int] ,
            "description": Optional[str] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultAudio: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "audio_url": str,,
            "title": str,,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "performer": Optional[str] ,
            "audio_duration": Optional[int] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultVoice: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "voice_url": str,,
            "title": str,,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "voice_duration": Optional[int] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultDocument: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "title": str,,
            "document_url": str,,
            "mime_type": str,,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "description": Optional[str] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] ,
            "thumbnail_url": Optional[str] ,
            "thumbnail_width": Optional[int] ,
            "thumbnail_height": Optional[int] 
        }
    },
    InlineQueryResultLocation: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "latitude": float,,
            "longitude": float,,
            "title": str,,
            "horizontal_accuracy": Optional[float] ,
            "live_period": Optional[int] ,
            "heading": Optional[int] ,
            "proximity_alert_radius": Optional[int] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] ,
            "thumbnail_url": Optional[str] ,
            "thumbnail_width": Optional[int] ,
            "thumbnail_height": Optional[int] 
        }
    },
    InlineQueryResultVenue: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "latitude": float,,
            "longitude": float,,
            "title": str,,
            "address": str,,
            "foursquare_id": Optional[str] ,
            "foursquare_type": Optional[str] ,
            "google_place_id": Optional[str] ,
            "google_place_type": Optional[str] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] ,
            "thumbnail_url": Optional[str] ,
            "thumbnail_width": Optional[int] ,
            "thumbnail_height": Optional[int] 
        }
    },
    InlineQueryResultContact: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "phone_number": str,,
            "first_name": str,,
            "last_name": Optional[str] ,
            "vcard": Optional[str] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] ,
            "thumbnail_url": Optional[str] ,
            "thumbnail_width": Optional[int] ,
            "thumbnail_height": Optional[int] 
        }
    },
    InlineQueryResultGame: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "game_short_name": str,,
            "reply_markup": Optional[InlineKeyboardMarkup] 
        }
    },
    InlineQueryResultCachedPhoto: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "photo_file_id": str,,
            "title": Optional[str] ,
            "description": Optional[str] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultCachedGif: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "gif_file_id": str,,
            "title": Optional[str] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultCachedMpeg4Gif: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "mpeg4_file_id": str,,
            "title": Optional[str] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultCachedSticker: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "sticker_file_id": str,,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultCachedDocument: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "title": str,,
            "document_file_id": str,,
            "description": Optional[str] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultCachedVideo: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "video_file_id": str,,
            "title": str,,
            "description": Optional[str] ,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultCachedVoice: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "voice_file_id": str,,
            "title": str,,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
        }
    },
    InlineQueryResultCachedAudio: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "audio_file_id": str,,
            "caption": Optional[str] ,
            "parse_mode": Optional[str] ,
            "caption_entities": Optional[list[MessageEntity]] ,
            "reply_markup": Optional[InlineKeyboardMarkup] ,
            "input_message_content": Optional[InputMessageContent] 
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
            "result_id": str,,
            "from_user": User,,
            "query": str,,
            "location": Optional[Location] ,
            "inline_message_id": Optional[str] 
        }
    },
    SentWebAppMessage: {
        "has_dese": True,
        "dese_kwargs": {
            "inline_message_id": None
        },
        "init_kwargs": {
            "inline_message_id": Optional[str] 
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
            "title": str,,
            "description": str,,
            "start_parameter": str,,
            "currency": str,,
            "total_amount": int
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
            "country_code": str,,
            "state": str,,
            "city": str,,
            "street_line1": str,,
            "street_line2": str,,
            "post_code": str
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
            "name": Optional[str] ,
            "phone_number": Optional[str] ,
            "email": Optional[str] ,
            "shipping_address": Optional[ShippingAddress] 
        }
    },
    ShippingOption: {
        "has_dese": False,
        "init_kwargs": {
            "id": str,,
            "title": str,,
            "prices": list[LabeledPrice]
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
            "currency": str,,
            "total_amount": int,,
            "invoice_payload": str,,
            "telegram_payment_charge_id": str,,
            "provider_payment_charge_id": str,,
            "shipping_option_id": Optional[str] ,
            "order_info": Optional[OrderInfo] 
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
            "id": str,,
            "from_user": User,,
            "invoice_payload": str,,
            "shipping_address": ShippingAddress
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
            "id": str,,
            "from_user": User,,
            "currency": str,,
            "total_amount": int,,
            "invoice_payload": str,,
            "shipping_option_id": Optional[str] ,
            "order_info": Optional[OrderInfo] 
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
            "file_id": str,,
            "file_unique_id": str,,
            "file_size": int,,
            "file_date": int
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
            "type": str,,
            "hash": str,,
            "data": Optional[str] ,
            "phone_number": Optional[str] ,
            "email": Optional[str] ,
            "files": Optional[list[PassportFile]] ,
            "front_side": Optional[PassportFile] ,
            "reverse_side": Optional[PassportFile] ,
            "selfie": Optional[PassportFile] ,
            "translation": Optional[list[PassportFile]] 
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
            "data": str,,
            "hash": str,,
            "secret": str
        }
    },
    PassportData: {
        "has_dese": True,
        "dese_kwargs": {
            "data": list[EncryptedPassportElement],
            "credentials": EncryptedCredentials
        },
        "init_kwargs": {
            "data": list[EncryptedPassportElement],,
            "credentials": EncryptedCredentials
        }
    },
    PassportElementErrorDataField: {
        "has_dese": False,
        "init_kwargs": {
            "type": Literal[,
            "field_name": str,,
            "data_hash": str,,
            "message": str
        }
    },
    PassportElementErrorFrontSide: {
        "has_dese": False,
        "init_kwargs": {
            "type": Literal[,
            "file_hash": str,,
            "message": str
        }
    },
    PassportElementErrorReverseSide: {
        "has_dese": False,
        "init_kwargs": {
            "type": Literal['driver_license', 'identity_card'],,
            "file_hash": str,,
            "message": str
        }
    },
    PassportElementErrorSelfie: {
        "has_dese": False,
        "init_kwargs": {
            "type": Literal[,
            "file_hash": str,,
            "message": str
        }
    },
    PassportElementErrorFile: {
        "has_dese": False,
        "init_kwargs": {
            "type": Literal[,
            "file_hash": str,,
            "message": str
        }
    },
    PassportElementErrorFiles: {
        "has_dese": False,
        "init_kwargs": {
            "type": Literal[,
            "file_hashes": list[str],,
            "message": str
        }
    },
    PassportElementErrorTranslationFile: {
        "has_dese": False,
        "init_kwargs": {
            "type": Literal[,
            "file_hash": str,,
            "message": str
        }
    },
    PassportElementErrorTranslationFiles: {
        "has_dese": False,
        "init_kwargs": {
            "type": Literal[,
            "file_hashes": list[str],,
            "message": str
        }
    },
    PassportElementErrorUnspecified: {
        "has_dese": False,
        "init_kwargs": {
            "type": str,,
            "element_hash": str,,
            "message": str
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
            "title": str,,
            "description": str,,
            "photo": list[PhotoSize],,
            "text": Optional[str] ,
            "text_entities": Optional[list[MessageEntity]] ,
            "animation": Optional[Animation] 
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
            "position": int,,
            "user": User,,
            "score": int
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
            "chat": Chat,,
            "giveaway_message_id": int,,
            "winners_selection_date": int,,
            "winner_count": int,,
            "winners": list[User],,
            "additional_chat_count": Optional[int] ,
            "premium_subscription_month_count": Optional[int] ,
            "unclaimed_prize_count": Optional[int] ,
            "only_new_members": Optional[Literal[True]] ,
            "was_refunded": Optional[Literal[True]] ,
            "prize_description": Optional[str] 
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
            "winner_count": int,,
            "unclaimed_prize_count": Optional[int] ,
            "giveaway_message": Optional[Message] 
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
            "chats": list[Chat],,
            "winners_selection_date": int,,
            "winner_count": int,,
            "only_new_members": Optional[Literal[True]] ,
            "has_public_winners": Optional[Literal[True]] ,
            "prize_description": Optional[str] ,
            "country_codes": Optional[list[str]] ,
            "premium_subscription_month_count": Optional[int] 
        }
    },
    MessageOriginUser: {
        "has_dese": True,
        "dese_kwargs": {
            "date": None,
            "sender_user": User
        },
        "init_kwargs": {
            "date": int,,
            "sender_user": User
        }
    },
    MessageOriginHiddenUser: {
        "has_dese": True,
        "dese_kwargs": {
            "date": None,
            "sender_user_name": None
        },
        "init_kwargs": {
            "date": int,,
            "sender_user_name": str
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
            "date": int,,
            "sender_chat": Chat,,
            "author_signature": Optional[str] 
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
            "date": int,,
            "chat": Chat,,
            "message_id": int,,
            "author_signature": Optional[str] 
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
            "origin": MessageOrigin,,
            "chat": Optional[Chat] ,
            "message_id": Optional[int] ,
            "link_preview_options": Optional[LinkPreviewOptions] ,
            "animation": Optional[Animation] ,
            "audio": Optional[Audio] ,
            "document": Optional[Document] ,
            "photo": Optional[list[PhotoSize]] ,
            "sticker": Optional[Sticker] ,
            "story": Optional[Story] ,
            "video": Optional[Video] ,
            "video_note": Optional[VideoNote] ,
            "voice": Optional[Voice] ,
            "has_media_spoiler": Optional[Literal[True]] ,
            "contact": Optional[Contact] ,
            "dice": Optional[Dice] ,
            "game": Optional[Game] ,
            "giveaway": Optional[Giveaway] ,
            "giveaway_winners": Optional[GiveawayWinners] ,
            "invoice": Optional[Invoice] ,
            "location": Optional[Location] ,
            "poll": Optional[Poll] ,
            "venue": Optional[Venue] 
        }
    },
    ChatBoostSourcePremium: {
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": User
        }
    },
    ChatBoostSourceGiftCode: {
        "has_dese": True,
        "dese_kwargs": {
            "user": User
        },
        "init_kwargs": {
            "user": User
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
            "giveaway_message_id": int,,
            "user": Optional[User] ,
            "is_unclaimed": Optional[Literal[True]] 
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
            "boost_id": str,,
            "add_date": int,,
            "expiration_date": int,,
            "source": ChatBoostSource
        }
    },
    UserChatBoosts: {
        "has_dese": True,
        "dese_kwargs": {
            "boosts": list[ChatBoost]
        },
        "init_kwargs": {
            "boosts": list[ChatBoost]
        }
    },
    ChatBoostUpdated: {
        "has_dese": True,
        "dese_kwargs": {
            "chat": Chat,
            "boost": ChatBoost
        },
        "init_kwargs": {
            "chat": Chat,,
            "boost": ChatBoost
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
            "chat": Chat,,
            "boost_id": str,,
            "remove_date": int,,
            "source": ChatBoostSource
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
            "update_id": int,,
            "message": Optional[Message] ,
            "edited_message": Optional[Message] ,
            "channel_post": Optional[Message] ,
            "edited_channel_post": Optional[Message] ,
            "message_reaction": Optional[MessageReactionUpdated] ,
            "message_reaction_count": Optional[MessageReactionCountUpdated] ,
            "inline_query": Optional[InlineQuery] ,
            "chosen_inline_result": Optional[ChosenInlineResult] ,
            "callback_query": Optional[CallbackQuery] ,
            "shipping_query": Optional[ShippingQuery] ,
            "pre_checkout_query": Optional[PreCheckoutQuery] ,
            "poll": Optional[Poll] ,
            "poll_answer": Optional[PollAnswer] ,
            "my_chat_member": Optional[ChatMemberUpdated] ,
            "chat_member": Optional[ChatMemberUpdated] ,
            "chat_join_request": Optional[ChatJoinRequest] ,
            "chat_boost": Optional[ChatBoostUpdated] ,
            "removed_chat_boost": Optional[ChatBoostRemoved] 
        }
    }
}

for k in TYPES:
    if not issubclass(k, TelegramType):
        raise TypeError(k)
