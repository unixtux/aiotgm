=================
*Available Types*
=================

All the names of the types are exactly the same described in the `offical documentation <https://core.telegram.org/bots/api#available-types>`_.

* **Note**:
    * Attribute *from* of the types, has been changed to *from_user* because in python it causes conflict.
    * If the :obj:`~tglib.types.Message` has not *text*, it's an empty string instead of :obj:`None`, so you can do as follows without getting an `AttributeError <https://docs.python.org/3/library/exceptions.html#AttributeError>`_.

    .. code-block:: python3

        bot = Client('api_token')

        @bot.manage_message()
        async def foo(message: Message):
            if message.text.startswith('/start'): ...
                # An error will never be raised
                # because the text is always of type string.

    * All other attributes are :obj:`None` if they are not in the received *JSON*.

---------------------------

.. automodule:: tglib.types
    :members:
    :undoc-members:
