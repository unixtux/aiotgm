#!/bin/python3

from logging import DEBUG, INFO

LOGGER_LEVEL = INFO
#LOGGER_LEVEL = DEBUG

import re
import json
import tglib
from tglib.logger import get_logger


with open('types.py') as r:
    LINES = r.readlines()

TYPES = {}
TG_TYPES = 0

LINE_N = 0

logger = get_logger('TypeChecker')
logger.setLevel(LOGGER_LEVEL)

def get_dese_kwargs(__type: str) -> dict[str, str]:
    global LINE_N
    dese_kwargs = {}
    while True:

        if re.match(r'\s*return\s*cls', LINES[LINE_N]):
            return dese_kwargs
 
        elif re.match(r'\s*((def\s*_dese)|(obj\s*=\s*\{\s*\}))', LINES[LINE_N]):
            LINE_N += 1
            continue

        dese_default = re.match(
            r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=.*res\s*\.get\s*\(\s*'(.*?)'\s*\)",
            LINES[LINE_N]
        )
        dese_default_if = re.match(
            r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=.*res\s*\.get\s*\(\s*'(.*?)'\s*\).*if\s*'(.*?)'\s*in\s*res\s*else\s*None",
            LINES[LINE_N]
        )

        if dese_default_if:
            group = dese_default_if.group(1, 2, 3)
            logger.debug(f'{__type} parameter {group[0]!r} is optional; line {LINE_N}.')
            if (group[0] == group[1] == group[2]):
                dese_kwargs.update({group[0]: {'tg_type': None, 'optional': True}})
            else: # err 111
                raise ValueError('111 at line', LINE_N, '\n' + LINES[LINE_N])

        elif dese_default:
            group = dese_default.group(1, 2)
            if (group[0] == group[1]):
                dese_kwargs.update({group[0]: {'tg_type': None, 'optional': False}})
            else: # err 222
                raise ValueError('222 at line', LINE_N, '\n' + LINES[LINE_N])

        else: # err 333
            raise ValueError('333 at line', LINE_N, '\n' + LINES[LINE_N])

        dese_tg_type = re.match(
            r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*(.*?)\s*\._dese",
            LINES[LINE_N]
        )
        dese_list_tg_type = re.match(
            r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*(.*?)\s*\._dese",
            LINES[LINE_N]
        )
        dese_nested_tg_type = re.match(
            r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*\[\s*(.*?)\s*\._dese",
            LINES[LINE_N]
        )

        if dese_nested_tg_type:
            group = dese_nested_tg_type.group(1, 2)
            if dese_kwargs[group[0]]['optional']:
                dese_kwargs[group[0]]['tg_type'] = f'Optional[list[list[{group[1]}]]]' 
            else:
                dese_kwargs[group[0]]['tg_type'] = f'list[list[{group[1]}]]'

        elif dese_list_tg_type:
            group = dese_list_tg_type.group(1, 2)
            if dese_kwargs[group[0]]['optional']:
                dese_kwargs[group[0]]['tg_type'] = f'Optional[list[{group[1]}]]'
            else:
                dese_kwargs[group[0]]['tg_type'] = f'list[{group[1]}]'

        elif dese_tg_type:
            group = dese_tg_type.group(1, 2)
            if dese_kwargs[group[0]]['optional']:
                dese_kwargs[group[0]]['tg_type'] = f'Optional[{group[1]}]'
            else:
                dese_kwargs[group[0]]['tg_type'] = group[1]

        dese_kwargs[group[0]] = dese_kwargs[group[0]]['tg_type']

        LINE_N += 1


while LINE_N != len(LINES):

    class_matched = re.match(
        r'class\s*(.*)\s*\(\s*(.*)\s*\)\s*:',
        LINES[LINE_N]
    )
    if class_matched:

        match = class_matched.group(1, 2)

        type = match[0]
        inheritance = match[1]

        TYPES[type] = {'has_dese': False}

        if inheritance == 'TelegramType':
            TG_TYPES += 1

    if re.match(r'\s*def\s*_dese\s*\(', LINES[LINE_N]):
        TYPES[type]['has_dese'] = True
        TYPES[type]['dese_kwargs'] = get_dese_kwargs(type)

    LINE_N += 1


NOT_IN_ALL = []
NOT_IN_TYPES = []
TYPES_WITH_DESE = []
TYPES_WITHOUT_DESE = []

for type in tglib.types.__all__:
    if type not in TYPES:
        NOT_IN_ALL.append(type)

for type in TYPES:
    if type not in tglib.types.__all__:
        NOT_IN_TYPES.append(type)
    if TYPES[type]['has_dese']:
        TYPES_WITH_DESE.append(type)
        #print(json.dumps({type: TYPES[type]}, indent = 2))
    else:
        TYPES_WITHOUT_DESE.append(type)
    #print(json.dumps({type: TYPES[type]}, indent = 2))

print('Length of __all__ is:', len(tglib.types.__all__))
print('Length of types is:', len(TYPES))
print('TelegramTypes are:', TG_TYPES)
print('Missing types are:', len(NOT_IN_ALL) or len(NOT_IN_TYPES))
print('Types with _dese():', len(TYPES_WITH_DESE))
print('Types without _dese():', len(TYPES_WITHOUT_DESE))



"""
with open('test_json.json', 'w') as w:
    w.write(json.dumps(TYPES, indent = 4))

with open('test_json.json', 'r') as r:
    lines = r.readlines()

f = '''\
from typing import Optional
from tglib.types import *
from tglib.types import TelegramType

TYPES = '''

for line in lines:
    line = re.sub(r'(\s*)"([A-Z].*)"(\s*:\s*\{)', r'\1\2\3', line)
    line = re.sub(r'(\s*".*"\s*)(:\s*)"(.*)"', r'\1\2\3', line)
    line = re.sub(r'(\s*)null(\s*)', r'\1None\2', line)
    line = re.sub(r'(\s*)true(\s*)', r'\1True\2', line)
    line = re.sub(r'(\s*)false(\s*)', r'\1False\2', line)
    f += line

f += '''

for k in TYPES:
    if not issubclass(k, TelegramType):
        raise TypeError(k)
'''

with open('test_json.py', 'w') as w:
    w.write(f)

#"""
