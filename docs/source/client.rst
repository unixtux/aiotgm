========
*Client*
========

.. autoclass:: tglib.Client
    :members:
    :undoc-members:
    :no-index:
        tglib.Client.manage_message,
        tglib.Client.manage_edited_message,
        tglib.Client.manage_channel_post,
        tglib.Client.manage_edited_channel_post,
        tglib.Client.manage_message_reaction,
        tglib.Client.manage_message_reaction_count,
        tglib.Client.manage_inline_query,
        tglib.Client.manage_chosen_inline_result,
        tglib.Client.manage_callback_query,
        tglib.Client.manage_shipping_query,
        tglib.Client.manage_pre_checkout_query,
        tglib.Client.manage_poll,
        tglib.Client.manage_poll_answer,
        tglib.Client.manage_my_chat_member,
        tglib.Client.manage_chat_member,
        tglib.Client.manage_chat_join_request,
        tglib.Client.manage_chat_boost,
        tglib.Client.manage_removed_chat_boost,
        tglib.Client.message_manager,
        tglib.Client.edited_message_manager,
        tglib.Client.channel_post_manager,
        tglib.Client.edited_channel_post_manager,
        tglib.Client.message_reaction_manager,
        tglib.Client.message_reaction_count_manager,
        tglib.Client.inline_query_manager,
        tglib.Client.chosen_inline_result_manager,
        tglib.Client.callback_query_manager,
        tglib.Client.shipping_query_manager,
        tglib.Client.pre_checkout_query_manager,
        tglib.Client.poll_manager,
        tglib.Client.poll_answer_manager,
        tglib.Client.my_chat_member_manager,
        tglib.Client.chat_member_manager,
        tglib.Client.chat_join_request_manager,
        tglib.Client.chat_boost_manager,
        tglib.Client.removed_chat_boost_manager

    *Decorators*
    ------------

    .. autodecorator:: tglib.Client::manage_message(checker=lambda message: True, /)

    .. autodecorator:: tglib.Client::manage_edited_message(checker=lambda edited_message: True, /)

    .. autodecorator:: tglib.Client::manage_channel_post(checker=lambda channel_post: True, /)

    .. autodecorator:: tglib.Client::manage_edited_channel_post(checker=lambda edited_channel_post: True, /)

    .. autodecorator:: tglib.Client::manage_message_reaction(checker=lambda message_reaction: True, /)

    .. autodecorator:: tglib.Client::manage_message_reaction_count(checker=lambda message_reaction_count: True, /)

    .. autodecorator:: tglib.Client::manage_inline_query(checker=lambda inline_query: True, /)

    .. autodecorator:: tglib.Client::manage_chosen_inline_result(checker=lambda chosen_inline_result: True, /)

    .. autodecorator:: tglib.Client::manage_callback_query(checker=lambda callback_query: True, /)

    .. autodecorator:: tglib.Client::manage_shipping_query(checker=lambda shipping_query: True, /)

    .. autodecorator:: tglib.Client::manage_pre_checkout_query(checker=lambda pre_checkout_query: True, /)

    .. autodecorator:: tglib.Client::manage_poll(checker=lambda poll: True, /)

    .. autodecorator:: tglib.Client::manage_poll_answer(checker=lambda poll_answer: True, /)

    .. autodecorator:: tglib.Client::manage_my_chat_member(checker=lambda my_chat_member: True, /)

    .. autodecorator:: tglib.Client::manage_chat_member(checker=lambda chat_member: True, /)

    .. autodecorator:: tglib.Client::manage_chat_join_request(checker=lambda chat_join_request: True, /)

    .. autodecorator:: tglib.Client::manage_chat_boost(checker=lambda chat_boost: True, /)

    .. autodecorator:: tglib.Client::manage_removed_chat_boost(checker=lambda removed_chat_boost: True, /)

    *UpdateManagers*
    ----------------

    .. autoproperty:: tglib::Client.message_manager
    .. autoproperty:: tglib::Client.edited_message_manager
    .. autoproperty:: tglib::Client.channel_post_manager
    .. autoproperty:: tglib::Client.edited_channel_post_manager
    .. autoproperty:: tglib::Client.message_reaction_manager
    .. autoproperty:: tglib::Client.message_reaction_count_manager
    .. autoproperty:: tglib::Client.inline_query_manager
    .. autoproperty:: tglib::Client.chosen_inline_result_manager
    .. autoproperty:: tglib::Client.callback_query_manager
    .. autoproperty:: tglib::Client.shipping_query_manager
    .. autoproperty:: tglib::Client.pre_checkout_query_manager
    .. autoproperty:: tglib::Client.poll_manager
    .. autoproperty:: tglib::Client.poll_answer_manager
    .. autoproperty:: tglib::Client.my_chat_member_manager
    .. autoproperty:: tglib::Client.chat_member_manager
    .. autoproperty:: tglib::Client.chat_join_request_manager
    .. autoproperty:: tglib::Client.chat_boost_manager
    .. autoproperty:: tglib::Client.removed_chat_boost_manager

    *Available methods*
    -------------------
