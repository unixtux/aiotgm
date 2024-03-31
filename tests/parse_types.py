#!/bin/env python3

if __name__ != '__main__':
    import os
    raise OSError(f'{os.path.basename(__file__)} must be launched from __main__')

import sys
sys.path.append('../')

from logging import DEBUG, INFO, WARNING
from typing import Any

LOGGER_LEVEL = INFO
LOGGER_LEVEL = DEBUG
#LOGGER_LEVEL = WARNING

import re
import json
import aiotgm.types
from aiotgm._logging import get_logger
logger = get_logger('TypeChecker')
logger.setLevel(LOGGER_LEVEL)

with open('../aiotgm/types.py') as r:
    LINES = r.readlines()

TYPES: dict[str, dict[str, dict[str, dict | Any] | Any | list] | Any] = {}
TG_TYPES = []

LINE_N = 0

JSON_LITERALS = {
    'True': True,
    'False': False,
    'None': None
}
OPTIONAL = re.compile(r'Optional\s*\[\s*(.*)\s*\]')


def raise_err(__file_line: int, *args: Any):
    if not isinstance(__file_line, int):
        raise TypeError(f'__file_line must be int, got {__file_line.__class__.__name__}')
    raise ValueError(f'at line: {__file_line}', *args)


def check_link(type: str) -> str:
    global LINE_N
    triple_quotes = re.compile(r".*'''")

    while LINE_N != len(LINES):

        if triple_quotes.match(LINES[LINE_N]):

            api_link = re.match(r'\s*(https://core.telegram.org/bots/api#(.*))\n', LINES[LINE_N + 1])

            if not api_link:
                raise_err(57)
            if api_link.group(2) != type.lower():
                raise_err(59)
            return api_link.group(1)

        LINE_N += 1
    else:
        raise_err(64)


def parse_number(val: str) -> int | float | str:
    integer = re.match(r'([0-9]+$)', val)
    double = re.match(r'([0-9]+\.[0-9]*$)|([0-9]*\.[0-9]+$)', val)
    if integer:
        return int(integer.group(1))
    elif double:
        return float(double.group(1))
    else:
        return val


def get_subclass_hint(func_name: str) -> str:
    '''
    Function to get the type-hint of the subclasses.
    '''
    dese_function = re.compile(r'^def\s*' + func_name + r'\s*\(.*\)\s*->\s*(.*?)\s*:')
    ln = 0
    while ln != len(LINES):
        if dese_function.match(LINES[ln]):
            type_hint = dese_function.match(LINES[ln]).group(1)
            if OPTIONAL.match(type_hint):
                type_hint = OPTIONAL.match(type_hint).group(1)
            return type_hint
        ln += 1
    else:
        raise_err(92, f'Function {func_name}() not found.')


def get_multiline_hint(type: str, arg: str, start_hint: str, ) -> dict[str, Any]:
    '''
    Function to get the type-hint of an __init__() argument in more than one line.\n
    E.g. Literal[
        ...
    ]
    '''
    global LINE_N
    open_brackets = LINES[LINE_N].count('[')
    closed_brackets = LINES[LINE_N].count(']')
    n_brackets = '{%s}' % (open_brackets - closed_brackets)

    type_hint = start_hint
    LINE_N += 1

    while LINE_N != len(LINES):

        end_of_hint_default = re.match(r'\s*(\]\s*)' + n_brackets + r'\s*=\s*(.*?),*\s*\n', LINES[LINE_N])
        end_of_hint =         re.match(r'\s*(\]\s*)' + n_brackets + r'\s*,*\s*\n', LINES[LINE_N])

        if end_of_hint_default:
            match = end_of_hint_default.group(1, 2)
            type_hint += match[0].rstrip() # right stripped because of spaces after the last bracket.
            default_value = JSON_LITERALS[match[1]] if match[1] in JSON_LITERALS else match[1]
            if OPTIONAL.match(type_hint) and default_value is not None:
                raise_err(120, arg, 'in', type, 'should be None by default.')
            return {'type_hint': type_hint, 'default': default_value}

        elif end_of_hint:
            return {'type_hint': type_hint + end_of_hint.group(1)}
        else:
            type_hint += re.sub(r'(.*?,)', r'\1 ', re.match(r'\s*(.*?\s*,*)\s*\n', LINES[LINE_N]).group(1))

        LINE_N += 1
    else:
        raise_err(130, f'No multiline hint found for argument {arg!r} of the type {type}.')


def get_dese_kwargs(__type: str) -> dict[str, Any]:
    global LINE_N
    dese_kwargs = {}
    while LINE_N != len(LINES):

        if re.match(r'\s*return\s*cls\s*\(\s*\*\*obj\s*\)\s*\n', LINES[LINE_N]):
            return dese_kwargs
 
        elif re.match(r'\s*obj\s*=\s*\{\s*\}\n', LINES[LINE_N]):
            LINE_N += 1
            continue

        dese_default_if = re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=.*?res\s*\.get\s*\(\s*'(.*?)'\s*\).*?if\s*'(.*?)'\s*in\s*res\s*else\s*None\s*\n", LINES[LINE_N])
        dese_default =    re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=.*?res\s*\.get\s*\(\s*'(.*?)'\s*\)", LINES[LINE_N])

        if dese_default_if:
            match = dese_default_if.group(1, 2, 3)
            if not (match[0] == match[1] == match[2]):
                raise_err(151, LINE_N, LINES[LINE_N])
            dese_kwargs[match[0]] = {'optional': True}

        elif dese_default:
            match = dese_default.group(1, 2)
            if not (match[0] == match[1]):
                raise_err(157, LINE_N, LINES[LINE_N])
            dese_kwargs[match[0]] = {'optional': False}

        else:
            raise_err(187, LINE_N, LINES[LINE_N])

        dese_nested_subclass = re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*\[\s*(_dese_.*?)\s*\(", LINES[LINE_N])
        dese_list_subclass =   re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*(_dese_.*?)\s*\(", LINES[LINE_N])
        dese_subclass =        re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*(_dese_.*?)\s*\(", LINES[LINE_N])
        dese_nested_tg_type =  re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*\[\s*(.*?)\s*\._dese", LINES[LINE_N])
        dese_list_tg_type =    re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*(.*?)\s*\._dese", LINES[LINE_N])
        dese_tg_type =         re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*(.*?)\s*\._dese", LINES[LINE_N])
        dese_unknown =         re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*res\s*\.\s*get\s*\(\s*'(.*?)'\s*\)", LINES[LINE_N])


        if dese_nested_subclass:
            match = dese_nested_subclass.group(1, 2)
            type_hint = get_subclass_hint(match[1])
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]] = f'Optional[list[list[{type_hint}]]]'
            else:
                dese_kwargs[match[0]] = f'list[list[{type_hint}]]'

        elif dese_list_subclass:
            match = dese_list_subclass.group(1, 2)
            type_hint = get_subclass_hint(match[1])
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]] = f'Optional[list[{type_hint}]]'
            else:
                dese_kwargs[match[0]] = f'list[{type_hint}]'

        elif dese_subclass:
            match = dese_subclass.group(1, 2)
            type_hint = get_subclass_hint(match[1])
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]] = f'Optional[{type_hint}]'
            else:
                dese_kwargs[match[0]] = type_hint

        elif dese_nested_tg_type:
            match = dese_nested_tg_type.group(1, 2)
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]] = f'Optional[list[list[{match[1]}]]]'
            else:
                dese_kwargs[match[0]] = f'list[list[{match[1]}]]'

        elif dese_list_tg_type:
            match = dese_list_tg_type.group(1, 2)
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]] = f'Optional[list[{match[1]}]]'
            else:
                dese_kwargs[match[0]] = f'list[{match[1]}]'

        elif dese_tg_type:
            match = dese_tg_type.group(1, 2)
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]] = f'Optional[{match[1]}]'
            else:
                dese_kwargs[match[0]] = match[1]

        elif dese_unknown:
            match = dese_unknown.group(1, 2)
            dese_kwargs[match[0]] = None

        else:
            raise_err(222, LINE_N, LINES[LINE_N])

        LINE_N += 1
    else:
        raise_err(226)


def get_init_kwargs(type: str) -> dict[str, Any]:
    global LINE_N
    init_kwargs = {}
    self_found = False
    if re.match(r'\s*def\s*__init__\s*\(\s*self\s*\)\s*:\s*\n', LINES[LINE_N]):
        return init_kwargs

    while LINE_N != len(LINES):

        if re.match(r'\s*def\s*__init__\s*\(\s*\n', LINES[LINE_N]):
            LINE_N += 1
            continue

        elif re.match(r'\s*self\s*,\s*\n', LINES[LINE_N]):
            self_found = True
            LINE_N += 1
            continue

        elif re.match(r'\s*\)\s*:\s*\n', LINES[LINE_N]):
            if not self_found:
                raise_err(249, f'self argument not found in {type}.__init__()', LINE_N, LINES[LINE_N])
            return init_kwargs

        match_multiline_hint =  re.match(r"\s*(.*?)\s*:\s*(.*?\[[^\]]*)\s*\n", LINES[LINE_N])
        match_hint_default =    re.match(r'\s*(.*?)\s*:\s*(.*?)\s*=\s*(.*?)\s*,*\s*\n', LINES[LINE_N])
        match_hint_no_default = re.match(r"\s*(.*?)\s*:\s*(.*?)\s*,*\s*\n", LINES[LINE_N])

        if match_multiline_hint:
            match = match_multiline_hint.group(1, 2)
            (arg, start_hint) = match[0], match[1]
            multi_line_hint = get_multiline_hint(type, arg, start_hint)
            type_hint = multi_line_hint['type_hint']
            if TYPES[type]['has_dese']:
                dese_hint = TYPES[type]['dese_kwargs'][arg]
                if dese_hint is not None:
                    if dese_hint != type_hint:
                        raise_err(265, f'{dese_hint} != {type_hint}', LINE_N, LINES[LINE_N])
            init_kwargs[arg] = multi_line_hint

        elif match_hint_default:
            match = match_hint_default.group(1, 2, 3)
            (arg, type_hint) = match[0], match[1]
            default_value = JSON_LITERALS[match[2]] if match[2] in JSON_LITERALS else match[2]
            if TYPES[type]['has_dese']:
                dese_hint = TYPES[type]['dese_kwargs'][arg]
                if dese_hint is not None:
                    if OPTIONAL.match(type_hint) and not OPTIONAL.match(dese_hint):
                        type_hint_checker = OPTIONAL.match(type_hint).group(1)
                    elif OPTIONAL.match(dese_hint):
                        type_hint_checker = type_hint
                    if dese_hint != type_hint_checker:
                        raise_err(280, f'{dese_hint!r} != {type_hint!r}', LINE_N, LINES[LINE_N])
            init_kwargs[arg] = {'type_hint': type_hint, 'default': default_value}

        elif match_hint_no_default:
            match = match_hint_no_default.group(1, 2)
            (arg, type_hint) = match[0], match[1]
            if TYPES[type]['has_dese']:
                dese_hint = TYPES[type]['dese_kwargs'][arg]
                if dese_hint is not None:
                    if dese_hint != type_hint:
                        raise_err(290, f'{dese_hint} != {type_hint}', LINE_N, LINES[LINE_N])
            init_kwargs[arg] = {'type_hint': type_hint}

        else:
            raise_err(294, LINE_N, LINES[LINE_N])

        LINE_N += 1
    else:
        raise_err(298)


def get_self_kwargs(type: str) -> dict[str, Any]:
    global LINE_N

    if not re.match(r"\s*\)\s*:\s*\n|\s*def\s*__init__\s*\(\s*self\s*\)\s*:\s*\n", LINES[LINE_N]):
        raise_err(305)

    self_kwargs = {'args': [], 'warnings': []}
    LINE_N += 1 # added new line now, because we didn't do before.

    while LINE_N != len(LINES):

        if re.match(r'\n$|\s*\.\.\.\s*\n', LINES[LINE_N]):
            return self_kwargs

        new_attribute = re.match(r"\s*self\s*\.\s*(.*?)\s*=\s*(.*?)\s*\n", LINES[LINE_N])

        if new_attribute:
            match = new_attribute.group(1, 2)
            (arg, default_value) = match[0], match[1]
            if arg not in TYPES[type]['kwargs']:
                self_kwargs['warnings'].append(f'{arg!r} is not in __init__()')
            if arg != default_value:
                self_kwargs['warnings'].append(f'{arg!r} default value is: {default_value}')
            self_kwargs['args'].append(arg)
        else:
            raise_err(325, LINES[LINE_N])

        LINE_N += 1
    else:
        return self_kwargs


while LINE_N != len(LINES):

    class_matched = re.match(r'class\s*(.*?)\s*\(\s*(.*?)\s*\)\s*:', LINES[LINE_N])

    if class_matched:
        match = class_matched.group(1, 2)

        type = match[0]
        inheritance = match[1]

        if type in [TYPES]:
            raise_err(344, type, 'is already in TYPES.')

        if inheritance == 'TelegramType':
            TG_TYPES.append(type)

        api_link = check_link(type)
        TYPES[type] = {
            'link': api_link,
            'has_dese': False,
            'warnings': [],
            'kwargs': {},
            'dese_kwargs': {},
            'init_kwargs': {}
        }

    if re.match(r'\s*def\s*_dese\s*\(', LINES[LINE_N]):

        if not re.match(r'\s*@_parse_result\s*\n', LINES[LINE_N - 1]):
            raise_err(482, LINE_N - 1, LINES[LINE_N - 1])

        if not re.match(r'\s*@classmethod\s*\n', LINES[LINE_N - 2]):
            raise_err(485, LINE_N - 2, LINES[LINE_N - 2])

        TYPES[type]['has_dese'] = True
        LINE_N += 1
        TYPES[type]['dese_kwargs'] = get_dese_kwargs(type)

    if re.match(r'\s*def\s*__init__\s*\(', LINES[LINE_N]):

        # Don't add a line here it will
        # be added in the next function
        init_kwargs = get_init_kwargs(type)
        TYPES[type]['init_kwargs'] = init_kwargs
        if TYPES[type]['has_dese']:
            dese_kwargs = TYPES[type]['dese_kwargs']
            for arg in init_kwargs:
                if arg not in dese_kwargs:
                    raise_err(377)
            for arg in dese_kwargs:
                if arg not in init_kwargs:
                    raise_err(380)

        TYPES[type]['kwargs'] = init_kwargs
        del TYPES[type]['dese_kwargs']
        del TYPES[type]['init_kwargs']

        self_kwargs = get_self_kwargs(type)
        TYPES[type]['self_kwargs'] = self_kwargs
        if self_kwargs['warnings']:
            TYPES[type]['warnings'] = self_kwargs['warnings']

        for arg in init_kwargs:
            if arg not in self_kwargs['args']:
                TYPES[type]['warnings'].append(f'Not found {type}.{arg}')

        del TYPES[type]['self_kwargs']

    LINE_N += 1 if LINE_N != len(LINES) else 0


NOT_IN_ALL = []
NOT_IN_TYPES = []
TYPES_WITH_DESE = []
TYPES_WITHOUT_DESE = []

for type in aiotgm.types.__all__:
    if type not in TYPES:
        NOT_IN_TYPES.append(type)

for type in TYPES:

    if not TYPES[type]['warnings']:
        TYPES[type].pop('warnings')

    if type not in aiotgm.types.__all__:
        NOT_IN_ALL.append(type)

    if TYPES[type]['link'] is None:
        raise_err(550, type)

    if TYPES[type]['has_dese']:
        TYPES_WITH_DESE.append(type)
    else:
        TYPES_WITHOUT_DESE.append(type)

logger.info('Length of __all__ is: %s', len(aiotgm.types.__all__))
logger.info('Length of TYPES is: %s', len(TYPES))
logger.info('TelegramTypes are: %s', len(TG_TYPES))
logger.info('Types with _dese(): %s', len(TYPES_WITH_DESE))
logger.info('Types without _dese(): %s', len(TYPES_WITHOUT_DESE))
logger.info('Not in __all__ are: %s. %s', len(NOT_IN_ALL), NOT_IN_ALL)
logger.info('Not in TYPES are: %s. %s\n', len(NOT_IN_TYPES), NOT_IN_TYPES)
#"""

with open('types.json', 'w') as w:
    w.write(json.dumps(TYPES, indent = 4))
    logger.info("'types.json' has been written.")

with open('types.json', 'r') as r:
    lines = r.readlines()

f = '''\
#!/bin/env python3

if __name__ != '__main__':
    raise OSError("__name__ is not '__main__'")

from aiotgm._logging import get_logger
logger = get_logger(__name__)

from typing import (
    Union,
    Optional,
    Literal
)
from aiotgm.types import *
from aiotgm.types import (
    TelegramType,
    ChatMember,
    MessageOrigin,
    ReactionType,
    ChatBoostSource,
    InputMessageContent,
    MaybeInaccessibleMessage
)
from aiotgm.constants import *

TYPES = '''

for line in lines:
    line = re.sub(r'(\s*)"([A-Z]\w*)"(\s*:\s*\{)', r'\1\2\3', line)
    line = re.sub(r'(\s*".*"\s*)(:\s*)"(\w+|\w*\[.*?\])"', r'\1\2\3', line)
    line = re.sub(r'(\s*)null(\s*)', r'\1None\2', line)
    line = re.sub(r'(\s*)true(\s*)', r'\1True\2', line)
    line = re.sub(r'(\s*)false(\s*)', r'\1False\2', line)
    f += line

f += '''

warnings = []

for type in TYPES:
    if 'warnings' in TYPES[type]:
        warnings.append(f'{type.__name__}: ' + ' and '.join(TYPES[type]['warnings']))

with open('warnings.txt', 'w') as w:
    w.write('\\n'.join(warnings))
    logger.info(f"{len(warnings)} warnings written in 'warnings.txt'.")
'''

with open('types.py', 'w') as w:
    w.write(f)
    logger.info("'types.py' has been written.")
