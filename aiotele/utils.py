#!/bin/env python3

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
