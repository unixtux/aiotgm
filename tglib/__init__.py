#!/bin/python3

__version__ = '1.2.7'
VERSION = __version__

__all__ = [
    '__version__',
    'VERSION',
    'Client',
    'NextManager',
    'TelegramError',
    'MARKDOWN_ESCAPES'
]

from .client import (
    Client,
    NextManager,
    TelegramError
)

from .utils import MARKDOWN_ESCAPES
