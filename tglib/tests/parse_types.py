#!/bin/python3

from logging import DEBUG, INFO
from typing import Optional, Any

LOGGER_LEVEL = INFO
LOGGER_LEVEL = DEBUG

import sys
sys.path.append('../')

import re
import json
import tglib.types
from tglib.logger import get_logger

with open('types.py') as r:
    LINES = r.readlines()

TYPES: dict[str, dict | Any] = {}
TG_TYPES = []

LINE_N = 0

logger = get_logger('TypeChecker')
logger.setLevel(LOGGER_LEVEL)

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


def get_subclass_hint(__func_name: str) -> str:
    '''
    Function to get the type-hint of the subclasses.
    '''
    dese_function = re.compile(
        r'^def\s*' + __func_name + r'\s*\(.*\)\s*->\s*(.*?)\s*:',
    )
    ln = 0
    while ln != len(LINES):
        if dese_function.match(LINES[ln]):
            type_hint = dese_function.match(LINES[ln]).group(1)
            if OPTIONAL.match(type_hint):
                type_hint = OPTIONAL.match(type_hint).group(1)
            return type_hint
        ln += 1
    else:
        raise_err(58, f'Function {__func_name}() not found.')


def get_multiline_hint(__type: str, __arg: str, __start_hint: str, ) -> dict[str, Any]:
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

    type_hint = __start_hint
    LINE_N += 1

    while LINE_N != len(LINES):

        end_of_hint_default = re.match(r'\s*((\]\s*)' + n_brackets + r')\s*=\s*(.*?),*\s*\n', LINES[LINE_N])
        end_of_hint =         re.match(r'\s*((\]\s*)' + n_brackets + r')\s*,*\s*\n', LINES[LINE_N])

        if end_of_hint_default:
            match = end_of_hint_default.group(1, 2, 3)
            type_hint += match[0].rstrip() # right stripped because of spaces after the last bracket.
            default_value = JSON_LITERALS[match[2]] if match[2] in JSON_LITERALS else match[2]
            if OPTIONAL.match(type_hint) and default_value is not None:
                raise_err(86, __arg, 'in', __type, 'should be None by default.')
            return {'type_hint': type_hint, 'default': default_value}

        elif end_of_hint:
            return {'type_hint': type_hint + end_of_hint.group(1)}
        else:
            type_hint += re.sub(r'(.*?,)', r'\1 ', re.match(r'\s*(.*?\s*,*)\s*\n', LINES[LINE_N]).group(1))

        LINE_N += 1
    else:
        raise_err(92, f'No multiline hint found for argument {__arg!r} of the type {__type}.')


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
            if (match[0] == match[1] == match[2]):
                dese_kwargs[match[0]] = {'type_hint': None, 'optional': True}
            else:
                raise_err(115, LINE_N, LINES[LINE_N])

        elif dese_default:
            match = dese_default.group(1, 2)
            if (match[0] == match[1]):
                dese_kwargs[match[0]] = {'type_hint': None, 'optional': False}
            else:
                raise_err(122, LINE_N, LINES[LINE_N])
        else:
            raise_err(124, LINE_N, LINES[LINE_N])

        dese_nested_subclass = re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*\[\s*(_dese_.*?)\s*\(", LINES[LINE_N])
        dese_list_subclass =   re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*(_dese_.*?)\s*\(", LINES[LINE_N])
        dese_subclass =        re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*(_dese_.*?)\s*\(", LINES[LINE_N])
        dese_nested_tg_type =  re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*\[\s*(.*?)\s*\._dese", LINES[LINE_N])
        dese_list_tg_type =    re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*\[\s*(.*?)\s*\._dese", LINES[LINE_N])
        dese_tg_type =         re.match(r"\s*obj\s*\[\s*'(.*?)'\s*\]\s*=\s*(.*?)\s*\._dese", LINES[LINE_N])

        if dese_nested_subclass:
            match = dese_nested_subclass.group(1, 2)
            type_hint = get_subclass_hint(match[1])
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]]['type_hint'] = f'Optional[list[list[{type_hint}]]]'
            else:
                dese_kwargs[match[0]]['type_hint'] = f'list[list[{type_hint}]]'

        elif dese_list_subclass:
            match = dese_list_subclass.group(1, 2)
            type_hint = get_subclass_hint(match[1])
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]]['type_hint'] = f'Optional[list[{type_hint}]]'
            else:
                dese_kwargs[match[0]]['type_hint'] = f'list[{type_hint}]'

        elif dese_subclass:
            match = dese_subclass.group(1, 2)
            type_hint = get_subclass_hint(match[1])
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]]['type_hint'] = f'Optional[{type_hint}]'
            else:
                dese_kwargs[match[0]]['type_hint'] = type_hint

        elif dese_nested_tg_type:
            match = dese_nested_tg_type.group(1, 2)
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]]['type_hint'] = f'Optional[list[list[{match[1]}]]]'
            else:
                dese_kwargs[match[0]]['type_hint'] = f'list[list[{match[1]}]]'

        elif dese_list_tg_type:
            match = dese_list_tg_type.group(1, 2)
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]]['type_hint'] = f'Optional[list[{match[1]}]]'
            else:
                dese_kwargs[match[0]]['type_hint'] = f'list[{match[1]}]'

        elif dese_tg_type:
            match = dese_tg_type.group(1, 2)
            if dese_kwargs[match[0]]['optional']:
                dese_kwargs[match[0]]['type_hint'] = f'Optional[{match[1]}]'
            else:
                dese_kwargs[match[0]]['type_hint'] = match[1]

        dese_kwargs[match[0]] = dese_kwargs[match[0]]['type_hint']

        LINE_N += 1
    else:
        raise_err(182)


def get_init_kwargs(__type: str) -> dict[str, Any]:
    self_found = False
    global LINE_N
    init_kwargs = {}
    while LINE_N != len(LINES):

        if re.match(r'\s*def\s*__init__\s*\(\s*self\s*\)\s*:\s*\n', LINES[LINE_N]):
            return init_kwargs

        elif re.match(r'\s*def\s*__init__\s*\(\s*\n', LINES[LINE_N]):
            LINE_N += 1
            continue

        elif re.match(r'\s*self\s*,\s*\n', LINES[LINE_N]):
            self_found = True
            LINE_N += 1
            continue

        elif re.match(r'\s*\)\s*:\s*\n', LINES[LINE_N]):
            if self_found:
                return init_kwargs
            else:
                raise_err(207, f'self argument not found in {__type}.__init__()', LINE_N, LINES[LINE_N])

        match_multiline_hinting =     re.match(r"\s*(.*?)\s*:\s*(.*?\[[^\]]*)\s*\n", LINES[LINE_N])
        match_hinting_default =       re.match(r'\s*(.*?)\s*:\s*(.*?)\s*=\s*(.*?)\s*,*\s*\n', LINES[LINE_N])
        match_hinting_no_default =    re.match(r"\s*(.*?)\s*:\s*(.*?)\s*,*\s*\n", LINES[LINE_N])
        match_no_hinting_default =    re.match(r"\s*(.*?)\s*=\s*(.*?)\s*,*\n", LINES[LINE_N])
        match_no_hinting_no_default = re.match(r"\s*(.*?)\s*,*\s*\n", LINES[LINE_N])

        if match_multiline_hinting:
            match = match_multiline_hinting.group(1, 2)
            (arg, start_hint) = match[0], match[1]
            multi_line_hint = get_multiline_hint(__type, arg, start_hint)
            type_hint = multi_line_hint['type_hint']
            if TYPES[__type]['has_dese']:
                dese_hint = TYPES[__type]['dese_kwargs'][arg]
                if dese_hint is not None:
                    if dese_hint != type_hint:
                        raise_err(224, f'{dese_hint} != {type_hint}', LINE_N, LINES[LINE_N])
            init_kwargs[arg] = multi_line_hint

        elif match_hinting_default:
            match = match_hinting_default.group(1, 2, 3)
            (arg, type_hint) = match[0], match[1]
            default_value = JSON_LITERALS[match[2]] if match[2] in JSON_LITERALS else match[2]
            if TYPES[__type]['has_dese']:
                dese_hint = TYPES[__type]['dese_kwargs'][arg]
                if dese_hint is not None:
                    if OPTIONAL.match(type_hint):
                        if default_value is not None:
                            raise_err(237, __type, arg, 'should be None by default', LINE_N, LINES[LINE_N])
                        if not OPTIONAL.match(dese_hint):
                            __type_hint = OPTIONAL.match(type_hint).group(1)
                        else:
                            __type_hint = type_hint
                    else:
                        __type_hint = type_hint
                    if dese_hint != __type_hint:
                        raise_err(245, f'{dese_hint} != {type_hint}', LINE_N, LINES[LINE_N])
            init_kwargs[arg] = {'type_hint': type_hint, 'default': default_value}

        elif match_hinting_no_default:
            match = match_hinting_no_default.group(1, 2)
            (arg, type_hint) = match[0], match[1]
            if TYPES[__type]['has_dese']:
                dese_hint = TYPES[__type]['dese_kwargs'][arg]
                if dese_hint is not None:
                    if dese_hint != type_hint:
                        raise_err(255, f'{dese_hint} != {type_hint}', LINE_N, LINES[LINE_N])
            init_kwargs[arg] = {'type_hint': type_hint}

        elif match_no_hinting_default:
            match = match_no_hinting_default.group(1, 2)
            (arg, default_value) = match[0], match[1]
            if default_value in JSON_LITERALS:
                default_value = JSON_LITERALS[default_value]
            elif default_value.isdigit():
                default_value = int(default_value)
            type_hint = None
            if TYPES[__type]['has_dese']:
                dese_hint = TYPES[__type]['dese_kwargs'][arg]
                if dese_hint is not None:
                    type_hint = dese_hint
            result = {'default': default_value} if type_hint is None else {'type_hint': type_hint, 'default': default_value}
            init_kwargs[arg] = result

        elif match_no_hinting_no_default:
            arg = match_no_hinting_no_default.group(1)
            type_hint = None
            if TYPES[__type]['has_dese']:
                dese_hint = TYPES[__type]['dese_kwargs'][arg]
                if dese_hint is not None:
                    type_hint = dese_hint
            result = None if type_hint is None else {'type_hint': type_hint}
            init_kwargs[arg] = result
        else:
            raise_err(283, LINE_N, LINES[LINE_N])

        LINE_N += 1
    else:
        raise_err(287)


def get_self_kwargs(__type: str) -> dict[str, Any]:
    global LINE_N

    if not re.match(r"\s*\)\s*:\s*\n|\s*def\s*__init__\s*\(\s*self\s*\)\s*:\s*\n", LINES[LINE_N]):
        raise_err(294)

    self_kwargs = {}
    LINE_N += 1

    while LINE_N != len(LINES):

        if re.match(r'\n$|\s*\.\.\.\s*\n', LINES[LINE_N]):
            return self_kwargs

        new_attribute_type_hint = re.match(r"\s*self\s*\.\s*(.*?)\s*:\s*(.*?)\s*=\s*(.*?)\s*\n", LINES[LINE_N])
        new_attribute =         re.match(r"\s*self\s*\.\s*(.*?)\s*=\s*(.*?)\s*\n", LINES[LINE_N])

        if not (new_attribute_type_hint or new_attribute):
            raise_err(308, LINE_N, LINES[LINE_N])
        else:
            if new_attribute_type_hint:
                match = new_attribute_type_hint.group(1, 2, 3)
                (arg, type_hint, default_value) = match[0], match[1], match[2]
                warnings = []
                if arg not in TYPES[__type]['kwargs']:
                    warnings.append('not in __init__()')
                else:
                    check_arg = TYPES[__type]['kwargs'][arg]
                    if check_arg is not None:
                        if 'type_hint' in check_arg:
                            __type_hint = type_hint
                            if OPTIONAL.match(type_hint):
                                if TYPES[type]['kwargs'][arg]['default'] is not None:
                                    raise_err(323, arg, LINES[LINE_N], LINE_N)
                                if not OPTIONAL.match(check_arg['type_hint']):
                                    __type_hint = OPTIONAL.match(type_hint).group(1)
                            if check_arg['type_hint'] != __type_hint:
                                raise_err(327, check_arg, type_hint)
                        else:
                            TYPES[__type]['kwargs'][arg]['type_hint'] = type_hint
                    else:
                        TYPES[__type]['kwargs'][arg] = {'type_hint': type_hint}

                self_kwargs[arg] = {}
                if arg != default_value:
                    warnings.append(f'default value is: {default_value}')
                self_kwargs[arg] = {'type_hint': type_hint, 'warnings': warnings}

            elif new_attribute:
                match = new_attribute.group(1, 2)
                (arg, default_value) = match[0], match[1]
                warnings = []
                if arg not in TYPES[__type]['kwargs']:
                    warnings.append('not in __init__()')
                if arg != default_value:
                    warnings.append(f'default value is: {default_value}')
                self_kwargs[arg] = {}
                self_kwargs[arg]['warnings'] = warnings

        LINE_N += 1
    else:
        return self_kwargs


while LINE_N != len(LINES):

    class_matched = re.match(r'class\s*(.*?)\s*\(\s*(.*?)\s*\)\s*:', LINES[LINE_N])

    if class_matched:
        match = class_matched.group(1, 2)

        type = match[0]
        inheritance = match[1]

        TYPES[type] = {'has_dese': False, 'kwargs': {}, 'init_kwargs': {}, 'self_kwargs': {}}

        if inheritance == 'TelegramType':
            TG_TYPES.append(type)

    if re.match(r'\s*def\s*_dese\s*\(', LINES[LINE_N]):

        if not re.match(r'\s*@_parse_result\s*\n', LINES[LINE_N - 1]):
            raise_err(311, LINE_N - 1, LINES[LINE_N - 1])

        if not re.match(r'\s*@classmethod\s*\n', LINES[LINE_N - 2]):
            raise_err(314, LINE_N - 2, LINES[LINE_N - 2])

        TYPES[type]['has_dese'] = True
        LINE_N += 1
        TYPES[type]['dese_kwargs'] = get_dese_kwargs(type)

    if re.match(r'\s*def\s*__init__\s*\(', LINES[LINE_N]):
        # Not add a line to check
        # def __init__(self): ...
        init_kwargs = get_init_kwargs(type)
        if TYPES[type]['has_dese']:
            for arg in TYPES[type]['dese_kwargs']:
                if arg not in init_kwargs:
                    raise_err(369, type, arg, LINE_N, LINES[LINE_N])

            for arg in TYPES[type]['dese_kwargs']:
                if arg not in init_kwargs:
                    raise_err(393, arg, type)

            TYPES[type].pop('dese_kwargs')

        TYPES[type]['kwargs'] = init_kwargs
        TYPES[type].pop('init_kwargs')
        self_kwargs = get_self_kwargs(type)
        for arg in TYPES[type]['kwargs']:
            if arg not in self_kwargs:
                TYPES[type]['kwargs'][arg].update({'warnings': [f'no match self.{arg} = ...']})

        for arg in self_kwargs.copy():
            warnings = self_kwargs[arg]['warnings']
            if warnings:
                if arg in TYPES[type]['kwargs']:
                    assert len(warnings) == 1
                    if 'warnings' in TYPES[type]['kwargs'][arg]:
                        TYPES[type]['kwargs'][arg]['warnings'].append(warnings[0])
                    else:
                        TYPES[type]['kwargs'][arg].update({'warnings': warnings})
                else:
                    if 'warnings' in TYPES[type]:
                        TYPES[type]['warnings'].update({arg: self_kwargs[arg]})
                    else:
                        TYPES[type].update({'warnings': {arg: self_kwargs[arg]}})

        TYPES[type].pop('self_kwargs')


    LINE_N += 1 if LINE_N != len(LINES) else 0


NOT_IN_ALL = []
NOT_IN_TYPES = []
TYPES_WITH_DESE = []
TYPES_WITHOUT_DESE = []

for type in tglib.types.__all__:
    if type not in TYPES:
        NOT_IN_TYPES.append(type)

for type in TYPES:
    if type not in tglib.types.__all__:
        NOT_IN_ALL.append(type)

    if TYPES[type]['has_dese']:
        TYPES_WITH_DESE.append(type)
    else:
        TYPES_WITHOUT_DESE.append(type)

logger.info('Length of __all__ is: %s', len(tglib.types.__all__))
logger.info('Length of types is: %s', len(TYPES))
logger.info('TelegramTypes are: %s', len(TG_TYPES))
logger.info('Missing types are: %s', len(NOT_IN_ALL) or len(NOT_IN_TYPES))
logger.info('Types with _dese(): %s', len(TYPES_WITH_DESE))
logger.info('Types without _dese(): %s\n', len(TYPES_WITHOUT_DESE))
#"""

with open('test_types.json', 'w') as w:
    w.write(json.dumps(TYPES, indent = 4))
    logger.info('test_types.json has been written.')

with open('test_types.json', 'r') as r:
    lines = r.readlines()

f = '''\
#!/bin/python3

import sys
sys.path.append('../')

from typing import (
    Union,
    Optional,
    Literal
)
from tglib.types import *
from tglib.types import (
    TelegramType,
    ChatMember,
    MessageOrigin,
    ReactionType,
    ChatBoostSource,
    InputMessageContent,
    MaybeInaccessibleMessage
)
from tglib.default_literals import *

TYPES = '''

for line in lines:
    line = re.sub(r'(\s*)"([A-Z]\w*)"(\s*:\s*\{)', r'\1\2\3', line)
    line = re.sub(r'(\s*".*"\s*)(:\s*)"(\w+|\w*\[.*?\])"', r'\1\2\3', line)
    line = re.sub(r'(\s*)null(\s*)', r'\1None\2', line)
    line = re.sub(r'(\s*)true(\s*)', r'\1True\2', line)
    line = re.sub(r'(\s*)false(\s*)', r'\1False\2', line)
    f += line

f += '''

from inspect import isclass

from tglib.logger import get_logger
logger = get_logger('TypesChecker')

logger.setLevel(20)

warnings = []

for type in TYPES:

    if not isclass(type):
        raise TypeError(
            f'Invalid key {type!r}: expected a type, got {type.__class__.__name__}.'
        )
    if not issubclass(type, TelegramType):
        raise TypeError(
            f'{type.__name__} is not a subclass of TelegramType.'
        )
    if 'warnings' in TYPES[type]:
        logger.debug('{!r}, {!r}'.format(type.__name__, TYPES[type]['warnings']))
        for arg in TYPES[type]['warnings']:
            warnings.append(f'{type.__name__}.{arg}: ' + ' & '.join(TYPES[type]['warnings'][arg]['warnings']))

    for arg in TYPES[type]['kwargs']:
        if 'warnings' in TYPES[type]['kwargs'][arg]:
            logger.debug('{!r}, {!r}, {!r}'.format(type.__name__, arg, TYPES[type]['kwargs'][arg]['warnings']))
            warnings.append(f'{type.__name__}.{arg}: ' + ' & '.join(TYPES[type]['kwargs'][arg]['warnings']))
        type_hint = TYPES[type]['kwargs'][arg]['type_hint']
        if type_hint.__name__ == 'Optional' and TYPES[type]['kwargs'][arg]['default'] is not None:
            raise ValueError(f"\\n\\nIn {type.__name__}, argument {arg!r} should be None by default, got {TYPES[type]['kwargs'][arg]['default']!r}")

if warnings:
    with open('types_warnings.txt', 'w') as w:
        w.write('\\n'.join(warnings))
        logger.warning(f'{len(warnings)} warnings have been saved in "types_warnings.txt"')
else:
    logger.info(f'{len(warnings)} warnings')
'''
with open('test_types.py', 'w') as w:
    w.write(f)
    logger.info('test_types.py has been written.')
