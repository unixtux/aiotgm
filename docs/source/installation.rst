=============
*Get Started*
=============

Installation
~~~~~~~~~~~~

Install the module using `pip <https://pypi.org/project/aiotele/>`_ from your shell.

.. code-block:: bash

    $ pip install aiotele

Update the module regurarly with the following command.

.. code-block:: bash

    $ pip install -U aiotele

Usage
~~~~~

Using the method :meth:`~aiotele.Client.long_polling` you manage every incoming :obj:`~aiotele.types.Update`.

.. code-block:: python3

    import asyncio
    import aiotele
    from aiotele.types import Message, CallbackQuery

    bot = aiotele.Client('<your_api_token>')

    @bot.manage_message()
    async def foo(msg: Message):
        await bot.send_message(msg.chat.id, 'hello')

    @bot.manage_callback_query()
    async def foo(call: CallbackQuery):
        await bot.answer_callback_query(call.id, 'hello')

    asyncio.run(bot.long_polling())

There are 18 decorator method to manage differrent updates:

* :meth:`~aiotele.Client.manage_message`
* :meth:`~aiotele.Client.manage_edited_message`
* :meth:`~aiotele.Client.manage_channel_post`
* :meth:`~aiotele.Client.manage_edited_channel_post`
* :meth:`~aiotele.Client.manage_message_reaction`
* :meth:`~aiotele.Client.manage_message_reaction_count`
* :meth:`~aiotele.Client.manage_inline_query`
* :meth:`~aiotele.Client.manage_chosen_inline_result`
* :meth:`~aiotele.Client.manage_callback_query`
* :meth:`~aiotele.Client.manage_shipping_query`
* :meth:`~aiotele.Client.manage_pre_checkout_query`
* :meth:`~aiotele.Client.manage_poll`
* :meth:`~aiotele.Client.manage_poll_answer`
* :meth:`~aiotele.Client.manage_my_chat_member`
* :meth:`~aiotele.Client.manage_chat_member`
* :meth:`~aiotele.Client.manage_chat_join_request`
* :meth:`~aiotele.Client.manage_chat_boost`
* :meth:`~aiotele.Client.manage_removed_chat_boost`
