========
*Client*
========

.. autoclass:: tglib.Client
    :members:
    :undoc-members:
    :no-index:

    :param token: Api token obtained from `@BotFather <https://t.me/botfather>`_.
    :param parse_mode: Select a default `parse mode <https://core.telegram.org/bots/api#formatting-options>`_ option (it can be overridden in the methods).
    :type parse_mode: str, optional
    :param protect_content: Pass :obj:`True` to use the protect content option by default (it can be overridden in the methods).
    :type protect_content: bool, optional
    :param proxy: Pass a proxy string to be used in the http requests.
    :type proxy: str, optional
    :param debug: Pass :obj:`True` for more information about http requests (useful for debugging).
    :type debug: bool, optional
