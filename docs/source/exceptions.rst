==========
Exceptions
==========

Example:

.. code-block:: python3

    import aiotgm
    import asyncio
    from aiotgm.types import Message

    bot = aiotgm.Client('<your_api_token>')

    @bot.manage_message()
    async def foo(msg: Message):
        try:
            await bot.send_message(msg.chat.id, "I'm here.")
        except (TelegramError, TimeoutError) as e:
            print(e)        

.. autoexception:: aiotgm.TelegramError
    :members:
    :undoc-members:
    :show-inheritance:

.. exception:: TimeoutError

    This `error <https://docs.python.org/3/library/exceptions.html#TimeoutError>`_
    is raised when a request is not returned in 5 minutes.
