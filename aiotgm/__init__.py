#!/bin/env python3

__all__ = (
    'Client',
    'NextFunction',
    'TelegramError',
)

__version__ = '0.2.7'
VERSION = __version__

from ._logging import get_logger
logger = get_logger('aiotgm ' + VERSION)
del get_logger

from .client import (
    Client,
    TelegramError,
)
from .update_manager import NextFunction
