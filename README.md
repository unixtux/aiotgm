[![pypi](https://img.shields.io/badge/pypi-aiotele-blue)](https://pypi.org/project/aiotele/) [![tele](https://img.shields.io/badge/telegram-@unixtux-blue)](https://t.me/geko1) [![Documentation Status](https://readthedocs.org/projects/aiotele/badge/?version=latest)](https://aiotele.readthedocs.io/?badge=latest)

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

Install the module using [pip](https://pypi.org/project/aiotele/).

```powershell
$ pip install aiotele
```

Update the module regurarly with the following command.

```powershell
$ pip install -U aiotele
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
