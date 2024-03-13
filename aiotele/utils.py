#!/bin/env python3

__all__ = (
    'escape_markdown',
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
    return text.translate(str.maketrans(MARKDOWN_ESCAPES))
