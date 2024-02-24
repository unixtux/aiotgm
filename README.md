[![pypi](https://img.shields.io/badge/pypi-tglib-blue)](https://pypi.org/project/tglib/) [![tele](https://img.shields.io/badge/telegram-@unixtux-blue)](https://t.me/geko1) [![docs](https://readthedocs.org/projects/tglib/badge/?version=latest)](https://tglib.readthedocs.io/en/latest/?badge=latest)

#

<h3 align="center">Asynchronous python implementation of the Telegram Bot API <a href="https://core.telegram.org/bots/api#february-16-2024">7.1</a></h3>

#

* #### Prerequisites
You require a good python knowledge with the [asyncio module](https://docs.python.org/3/library/asyncio.html) and a Telegram Bot API token, you can get it via [@BotFather](https://t.me/botfather).

#

* #### Dependencies
  * Python >= 3.8
  * [aiohttp](https://github.com/aio-libs/aiohttp)
  * Optional [ujson](https://github.com/ultrajson/ultrajson) & [certifi](https://github.com/certifi/python-certifi)

* #### Installation
```powershell
$ pip install tglib
```

* #### Keep it updated
```powershell
$ pip install -U tglib
```

#

* #### Reply Markups
**InlineKeyboardMarkup** and **ReplyKeyboardMarkup** have the method "**add**", so you can create new buttons after the object has been initialized.

```python
markup = ReplyKeyboardMarkup()
markup.add(KeyboardButton('x'), KeyboardButton('y'))

# All the buttons added with this method will be in
# the same row, you can change the row width after the
# object initialization using the property setter 'row_width'.

markup.row_width = 4

# The keyboard will be rearranged with 4 buttons each row.
```

#

* #### Notes

> Webhook has not been implemented yet.

#

* #### Usage
```python
#!/bin/python3

from tglib import (
    Client,
    NextManager,
    TelegramError
)
# Import all the types.
from tglib.types import *

# Create a bot instance.
bot = Client('<your_token>')

# Add some rules for incoming updates. Managers
# check rules in the same order they were added.

@bot.manage_message(lambda message: message.text == '/start')
async def foo(message: Message):
    try:
        await bot.send_message(message.chat.id, 'Welcome!')
    except (TimeoutError, TelegramError):
        pass
        # Two errors can be raised in requests:
        # - TimeoutError if a response
        #   is not returned in 5 minutes.
        # - TelegramError if a response is
        #   returned but got a bad status code.
    else:
        return NextManager()
        # Returning a NextManager instance, you will pass
        # the update to the following manager of the same kind.

# You can also add rules with the
# method 'add_rule' of the managers.

def checker(message: Message):
    return message.text == '/help'

async def bar(message: Message):
    await bot.send_message(message.chat.id, 'Need help?')

bot.message_manager.add_rule(checker, bar)

# Calling the method 'long_polling',
# the bot starts receiving updates by
# the telegram server and process them.

import asyncio

if __name__ == '__main__':
    asyncio.run(bot.long_polling())
```
