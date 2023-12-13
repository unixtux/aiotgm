[![pypi](https://img.shields.io/badge/pypi-tglib-blue)](https://pypi.org/project/tglib/) [![tele](https://img.shields.io/badge/telegram-@unixtux-blue)](https://t.me/geko1)

<h2 style="text-align: center;">Async telegram library to build your bot client</h2>

* #### Dependencies
    * [aiohttp](https://github.com/aio-libs/aiohttp)
    * Optional [ujson](https://github.com/ultrajson/ultrajson), [certifi](https://github.com/certifi/python-certifi)

* #### Installation
    * Classic ```python3 -m pip install tglib```
    * With optional dependencies ```python3 -m pip install tglib[all]```
    * To update to the latest version ```python3 -m pip install -U tglib```

* #### Managers for different [updates](https://core.telegram.org/bots/api#update)
    * message_manager
    * edited_message_manager
    * channel_post_manager
    * edited_channel_post_manager
    * inline_query_manager
    * chosen_inline_result_manager
    * callback_query_manager
    * shipping_query_manager
    * pre_checkout_query_manager
    * poll_manager
    * poll_answer_manager
    * my_chat_member_manager
    * chat_member_manager
    * chat_join_request_manager


* #### [Available methods](https://core.telegram.org/bots/api#available-methods)
    * get_updates
    * get_me
    * log_out
    * close
    * send_message
    * forward_message
    * copy_message
    * send_photo
    * send_audio
    * send_document
    * send_video
    * send_animation
    * send_voice
    * send_video_note
    * send_media_group
    * send_location
    * send_venue
    * send_contact
    * send_poll
    * send_dice
    * send_chat_action
    * get_user_profile_photos
    * get_file
    * ban_chat_member
    * unban_chat_member
    * restrict_chat_member
    * promote_chat_member
    * set_chat_administrator_custom_title
    * ban_chat_sender_chat
    * unban_chat_sender_chat
    * set_chat_permissions
    * export_chat_invite_link
    * create_chat_invite_link
    * edit_chat_invite_link
    * revoke_chat_invite_link
    * approve_chat_join_request
    * decline_chat_join_request
    * set_chat_photo
    * delete_chat_photo
    * set_chat_title
    * set_chat_description
    * pin_chat_message
    * unpin_chat_message
    * unpin_all_chat_messages
    * leave_chat
    * get_chat
    * get_chat_administrators
    * get_chat_member_count
    * get_chat_member
    * set_chat_sticker_set
    * delete_chat_sticker_set
    * get_forum_topic_icon_stickers
    * create_forum_topic
    * edit_forum_topic
    * close_forum_topic
    * reopen_forum_topic
    * delete_forum_topic
    * unpin_all_forum_topic_messages
    * edit_general_forum_topic
    * close_general_forum_topic
    * reopen_general_forum_topic
    * hide_general_forum_topic
    * unhide_general_forum_topic
    * unpin_all_general_forum_topic_messages
    * answer_callback_query
    * set_my_commands
    * delete_my_commands
    * get_my_commands
    * set_my_name
    * get_my_name
    * set_my_description
    * get_my_description
    * set_my_short_description
    * get_my_short_description
    * set_chat_menu_button
    * get_chat_menu_button
    * set_my_default_administrator_rights
    * get_my_default_administrator_rights
    * edit_message_text
    * edit_message_caption
    * edit_message_media
    * edit_message_live_location
    * stop_message_live_location
    * edit_message_reply_markup
    * stop_poll
    * delete_message
    * send_sticker
    * get_sticker_set
    * get_custom_emoji_stickers
    * upload_sticker_file
    * create_new_sticker_set
    * add_sticker_to_set
    * set_sticker_position_in_set
    * delete_sticker_from_set
    * set_sticker_emoji_list
    * set_sticker_keywords
    * set_sticker_mask_position
    * set_sticker_set_title
    * set_sticker_set_thumbnail
    * set_custom_emoji_sticker_set_thumbnail
    * delete_sticker_set
    * answer_inline_query
    * answer_web_app_query
    * send_invoice
    * create_invoice_link
    * answer_shipping_query
    * answer_pre_checkout_query
    * set_passport_data_errors
    * send_game
    * set_game_score
    * get_game_high_scores

* #### Usage
```
import asyncio
from tglib import (
    Client,
    NextManager,
    TelegramError
)
# To import all the telegram types
# like Message, User, Chat, ...
from tglib.objects import *

bot = Client('<your_token>')

# Add some rules for incoming updates. Managers
# check for rules in the same order they were added.

@bot.manage_message(lambda mex: mex.text == '/start')
async def welcome(mex: Message):
    await bot.send_message(mex.chat.id, 'welcome')
    return NextManager()

    # returning a NextManager instance, you will pass
    # the update to the following manager of same kind.

@bot.manage_message(lambda x: True)
async def last_manager(mex: Message):
    await bot.send_message(mex.chat.id, 'What?')

# You can also use the method 'add_rule' of managers to add rules

checker = lambda mex: mex.text in ['/start', '/help']

async def delete(mex):
    await bot.delete_message(mex.chat.id, mex.message_id)
    return NextManager()

bot.message_manager.add_rule(checker, delete)

# Finally you call the method 'long_polling' to
# start receiving updates from the telegram server

if __name__ == '__main__':
    asyncio.run(bot.long_polling())
```