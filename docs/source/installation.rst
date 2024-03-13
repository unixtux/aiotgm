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