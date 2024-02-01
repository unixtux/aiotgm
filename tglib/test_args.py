#!/bin/python3

import re
import json
import tglib

with open('types.py') as r:
    LINES = r.readlines()

TYPES = {}
TG_TYPES = 0

LINE_N = 0

def get_dese_kwargs() -> list[str]:
    global LINE_N
    dese_kwargs = {'args': {}}
    while True:
        if re.search(r'return.*', LINES[LINE_N]):
            return dese_kwargs
        dese_match_2 = re.search(
            r"obj\s*\[\s*'(.*?)'\s*\]\s*=.*res\s*\.get\s*\(\s*'(.*?)'\s*\)",
            LINES[LINE_N]
        )
        dese_match_3 = re.search(
            r"obj\s*\[\s*'(.*?)'\s*\]\s*=.*res\s*\.get\s*\(\s*'(.*?)'\s*\).*if\s*'(.*?)'\s*in\s*res",
            LINES[LINE_N]
        )
        dese_match_type_2 = re.search(
            r"obj\s*\[\s*'(.*)'\s*\]\s*=.*([A-Z].*)\s*\.\s*_dese.*res\s*\.get\s*\(\s*'(.*?)'\s*\)",
            LINES[LINE_N]
        )
        dese_match_type_3 = re.search(
            r"obj\s*\[\s*'(.*)'\s*\]\s*=.*([A-Z].*)\s*\.\s*_dese.*res\s*\.get\s*\(\s*'(.*?)'\s*\).*if\s*'(.*?)'\s*in\s*res",
            LINES[LINE_N]
        )
        if dese_match_2:
            group = dese_match_2.group(1, 2)
            if (group[0] == group[1]):
                dese_kwargs['args'].update({group[0]: {'tg_type': None}})
            else:
                raise ValueError(LINES[LINE_N])

        if dese_match_3:
            group = dese_match_3.group(1, 2, 3)
            if (group[0] == group[1] == group[2]):
                dese_kwargs['args'].update({group[0]: {'tg_type': None}})
            else:
                raise ValueError(LINES[LINE_N])

        if dese_match_type_2:
            group = dese_match_type_2.group(1, 2, 3)
            if (group[0] == group[2]):
                dese_kwargs['args'].update({group[0]: {'tg_type': group[1]}})
            else:
                raise ValueError(LINES[LINE_N])

        if dese_match_type_3:
            group = dese_match_type_3.group(1, 2, 3, 4)
            if (group[0] == group[2] == group[3]):
                dese_kwargs['args'].update({group[0]: {'tg_type': group[1]}})
            else:
                raise ValueError(LINES[LINE_N])

        LINE_N += 1


while LINE_N != len(LINES):

    if re.search(
            r'class\s*.*\s*\(.*\)\s*:',
            LINES[LINE_N]
        ):
        match = re.search(
            r'class\s*(.*)\s*\(\s*(.*)\s*\)\s*:',
            LINES[LINE_N]
        ).group(1, 2)

        type = match[0]
        inheritance = match[1]

        TYPES[type] = {'has_dese': False, 'dese_kwargs': None}

        if inheritance == 'TelegramType':
            TG_TYPES += 1

    if re.search(r'def.*dese\s*\(.*\)', LINES[LINE_N]):
        TYPES[type]['has_dese'] = True
        TYPES[type]['dese_kwargs'] = get_dese_kwargs()

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
        print(json.dumps({type: TYPES[type]['dese_kwargs']}, indent = 2))
    else:
        TYPES_WITHOUT_DESE.append(type)
    #print(json.dumps({type: TYPES[type]}, indent = 2))

print('Length of __all__ is:', len(tglib.types.__all__))
print('Length of types is:', len(TYPES))
print('TelegramTypes are:', TG_TYPES)
print('Missing types are:', len(NOT_IN_ALL) or len(NOT_IN_TYPES))
print('Types with _dese():', len(TYPES_WITH_DESE))
print('Types without _dese():', len(TYPES_WITHOUT_DESE))

#"""
