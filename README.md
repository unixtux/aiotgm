[![pypi](https://img.shields.io/badge/pypi-tglib-blue)](https://pypi.org/project/tglib/) [![tele](https://img.shields.io/badge/telegram-@unixtux-blue)](https://t.me/geko1)

<h3 align="center">Async python module to build your telegram bot client</h3>

* #### Requirements
  * Python >= 3.8
  * [aiohttp](https://github.com/aio-libs/aiohttp)
  * Optional [ujson](https://github.com/ultrajson/ultrajson) & [certifi](https://github.com/certifi/python-certifi)

* #### Installation
```python -m pip install tglib```

* #### Update the module
```python -m pip install -U tglib```

* #### 14 managers for different [updates](https://core.telegram.org/bots/api#update)
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


* #### Available methods
All the methods of the Client are the same described in the *[offical documentation](https://core.telegram.org/bots/api#available-methods)*, changed from camelCase to snake_case. All the methods are **async**, so you must use them in **await** expression.

* #### Available Types
All the types are the same described in the *[offical documentation](https://core.telegram.org/bots/api#available-types)*.

> Attribute **'from'** of the types, has been changed to **'from_user'** because in python it causes conflict.

> If the attribute **'text'** of the Message is empty, it's **str()** instead of **None**, so you can use for example text.startswith() without getting errors.

> All other optional attributes of the objects are None if they are not in the **JSON** received as response.

* #### Notes

> Webhook has not been implemented yet.

* #### ReplyMarkups
**InlineKeyboardMarkup** and **ReplyKeyboardMarkup** have the method **'add'**, so you can create new buttons after the object has been initialized.
```python
markup = ReplyKeyboardMarkup()
markup.add(KeyboardButton('xyz'), ...)

# All the buttons added with this method will be in
# the same row, you can change the row width after the
# object initialization using the property setter 'row_width'.

markup.row_width = 4

# this will reorder all the buttons in a row of 4.
```

* #### Prerequisites
You require a basic Python knowledge and a telegram bot API token, you can get it via *[@BotFather](https://t.me/botfather)*.

* #### Usage
```python
import asyncio

from tglib import (
    Client,
    NextManager,
    TelegramError
)
from tglib.objects import *

bot = Client('<your_token>')

# Add some rules for incoming updates. Managers
# check rules in the same order they were added.

@bot.manage_message(lambda message: message.text == '/start')
async def welcome(message: Message):
    try:
        await bot.send_message(message.chat.id, 'welcome')
    except (TimeoutError, TelegramError):
        # Two errors can be raised in requests.
        # - TimeoutError if a response
        #   is not returned in 5 minutes.
        # - TelegramError if a response is
        #   returned but got a bad status code.

    return NextManager()
    # Returning a NextManager instance, you will pass
    # the update to the following manager of same kind.


# You can also add rules with the
# method 'add_rule' of the managers.

def checker(message: Message):
    return message.text == '/start'

async def welcome(message: Message):
    ...

bot.message_manager.add_rule(checker, welcome)

# Calling the method 'long_polling',
# the bot starts receiving updates by
# the telegram server and process them.

if __name__ == '__main__':
    asyncio.run(bot.long_polling())
```
