#!/bin/env python3

__all__ = (
    'escape_markdown',
    'seconds_until_next_hour',
)

MARKDOWN_ESCAPES = {
    '_': '\_',
    '*': '\*',
    '[': '\[',
    ']': '\]',
    '(': '\(',
    ')': '\)',
    '~': '\~',
    '`': '\`',
    '>': '\>',
    '#': '\#',
    '+': '\+',
    '-': '\-',
    '=': '\=',
    '|': '\|',
    '{': '\{',
    '}': '\}',
    '.': '\.',
    '!': '\!'
}

def escape_markdown(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(
            'In escape_markdown(), text must'
            f' be str, got {text.__class__.__name__}'
        )
    return text.translate(str.maketrans(MARKDOWN_ESCAPES))

def seconds_until_next_hour() -> float:
    from datetime import datetime as dtm
    now = dtm.now()
    return 3600 - (now.minute * 60 + now.second)
