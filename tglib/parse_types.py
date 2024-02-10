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

TYPES = {}
TG_TYPES = []

LINE_N = 0

logger = get_logger('TypeChecker')
logger.setLevel(LOGGER_LEVEL)

JSON_LITERALS = {
    'True': True,
    'False': False,
    'None': None
}

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
            optional = re.match(r'Optional\s*\[\s*(.*)\s*\]', type_hint)
            if optional:
                type_hint = optional.group(1)
            return type_hint
        ln += 1
    else:
        raise_err(57, f'Function {__func_name}() not found.')


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
            return {'type_hint': type_hint, 'default': match[2]}

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
            (arg, start_hinting) = match[0], match[1]
            init_kwargs[arg] = get_multiline_hint(__type, arg, start_hinting)

        elif match_hinting_default:
            match = match_hinting_default.group(1, 2, 3)
            (arg, type_hint) = match[0], match[1]
            default_value = JSON_LITERALS[match[2]] if match[2] in JSON_LITERALS else match[2]
            init_kwargs[arg] = {'type_hint': type_hint, 'default': default_value}

        elif match_hinting_no_default:
            match = match_hinting_no_default.group(1, 2)
            (arg, type_hint) = match[0], match[1]
            init_kwargs[arg] = {'type_hint': type_hint}

        elif match_no_hinting_default:
            match = match_no_hinting_default.group(1, 2)
            (arg, default_value) = match[0], match[1]
            if default_value in JSON_LITERALS:
                default_value = JSON_LITERALS[default_value]
            elif default_value.isdigit():
                default_value = int(default_value)
            init_kwargs[arg] = {'default': default_value}

        elif match_no_hinting_no_default:
            arg = match_no_hinting_no_default.group(1)
            init_kwargs[arg] = None
        else:
            raise_err(244, LINE_N, LINES[LINE_N])

        LINE_N += 1
    else:
        raise_err(248)


def get_self_kwargs(__type: str) -> dict[str, Any]:
    global LINE_N

    if not re.match(r"\s*\)\s*:\s*\n|\s*def\s*__init__\s*\(\s*self\s*\)\s*:\s*\n", LINES[LINE_N]):
        raise_err(255)

    self_kwargs = {'warning': {}}
    LINE_N += 1

    while LINE_N != len(LINES):

        if re.match(r'\n$|\s*\.\.\.\s*\n', LINES[LINE_N]):
            if not self_kwargs['warning']: self_kwargs.pop('warning')
            return self_kwargs

        new_attribute_hinting = re.match(r"\s*self\s*\.\s*(.*?)\s*:\s*(.*?)\s*=\s*(.*?)\s*\n", LINES[LINE_N])
        new_attribute =         re.match(r"\s*self\s*\.\s*(.*?)\s*=\s*(.*?)\s*\n", LINES[LINE_N])

        if not (new_attribute_hinting or new_attribute):
            raise_err(270, LINE_N, LINES[LINE_N])
        else:
            if new_attribute_hinting:
                match = new_attribute_hinting.group(1, 2, 3)
                (arg, type_hint, default_value) = match[0], match[1], match[2]
                if arg != default_value:
                    self_kwargs['warning'][arg] = {'default': default_value, 'type_hint': type_hint}
                else:
                    self_kwargs[arg] = {'default': 'ok.', 'type_hint': type_hint}

            elif new_attribute:
                match = new_attribute.group(1, 2)
                (arg, default_value) = match[0], match[1]
                if arg != default_value:
                    self_kwargs['warning'][arg] = {'default': default_value}
                else:
                    self_kwargs[arg] = {'default': 'ok.'}

        LINE_N += 1
    else:
        return self_kwargs


while LINE_N != len(LINES):

    class_matched = re.match(r'class\s*(.*?)\s*\(\s*(.*?)\s*\)\s*:', LINES[LINE_N])

    if class_matched:
        match = class_matched.group(1, 2)

        type = match[0]
        inheritance = match[1]

        TYPES[type] = {'has_dese': False}

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
        TYPES[type]['init_kwargs'] = get_init_kwargs(type)
        TYPES[type]['self_kwargs'] = get_self_kwargs(type)


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
logger.info('Types without _dese(): %s', len(TYPES_WITHOUT_DESE))
#"""

args = []

for type in TYPES:
    type_hint = None
    default = None
    has_dese = True if TYPES[type]['has_dese'] else False
    dede_kwargs = TYPES[type]['dese_kwargs'] if has_dese else None
    init_kwargs = TYPES[type]['init_kwargs']
    self_kwargs = TYPES[type]['self_kwargs']

    if has_dese:
        for dese_argument in dede_kwargs:
            if dese_argument not in init_kwargs:
                raise_err(369, type, dese_argument, 'missing in init_kwargs')
            if dese_argument not in self_kwargs:
                if dese_argument not in self_kwargs['warning']:
                    raise_err(372, type, dese_argument, 'missing in self_kwargs and self_kwargs["warning"]')



"""
with open('test_types.json', 'w') as w:
    w.write(json.dumps(TYPES, indent = 4))
    logger.info('test_types.json has been written.')

with open('test_types.json', 'r') as r:
    lines = r.readlines()

f = '''\
#!/bin/python3

IGNORE = ()
IGNORE = ('InputFile', )

import sys
sys.path.append('../')

from typing import (
    Union,
    Optional,
    Literal,
    _UnionGenericAlias
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

logger.setLevel(10)

for k in TYPES:

    if not isclass(k):
        raise TypeError(
            f'Invalid key {k!r}: expected a type, got {k.__class__.__name__}.'
        )
    if not issubclass(k, TelegramType):
        raise TypeError(
            f'{k.__name__} is not a subclass of TelegramType.'
        )
    if k.__name__ in IGNORE:
        continue

    if TYPES[k]['has_dese']:
        has_dese = True
        for arg in TYPES[k]['dese_kwargs']:
            if TYPES[k]['dese_kwargs'][arg] is None:
                continue
            if arg not in TYPES[k]['init_kwargs']:
                logger.warning('%s, %s: %s', k.__name__, arg, 'not in init_kwargs')
            else:
                init_arg = TYPES[k]['init_kwargs'][arg]
                if init_arg is not None and 'type_hint' in init_arg:
                    init_type_hint = init_arg['type_hint']
                    dese_type_hint = TYPES[k]['dese_kwargs'][arg]

                    if type(dese_type_hint) is _UnionGenericAlias and type(init_type_hint) is _UnionGenericAlias:
                        if type(None) in dese_type_hint.__dict__['__args__']:
                            if not type(None) in init_type_hint.__dict__['__args__']:
                                raise ValueError(f'Argument {arg!r} should be Optional in {k.__name__}.__init__(), got {dese_type_hint}')
                            else:
                                logger.debug('{} was optional in {}.dese()'.format(dese_type_hint, k.__name__))

                        if type(None) not in dese_type_hint.__dict__['__args__'] and type(None) in init_type_hint.__dict__['__args__']:
                            dese_type_hint = Optional[dese_type_hint]

                    elif not type(dese_type_hint) is _UnionGenericAlias and type(init_type_hint) is _UnionGenericAlias:
                        if type(None) in init_type_hint.__dict__['__args__']:
                            dese_type_hint = Optional[dese_type_hint]

                    if dese_type_hint != init_type_hint:
                        raise ValueError(init_type_hint, dese_type_hint, k.__name__)

            if arg not in TYPES[k]['self_kwargs']:
                if (
                    'warning' in TYPES[k]['self_kwargs']
                    and arg in TYPES[k]['self_kwargs']['warning']
                ):
                    continue
                logger.warning('%s, %s: %s', k.__name__, arg, 'not in self_kwargs')
    else:
        has_dese = False

    for arg in TYPES[k]['init_kwargs']:
        if has_dese and arg not in TYPES[k]['dese_kwargs']:
            logger.warning('%s, %s: %s', k.__name__, arg, 'not in dese_kwargs')
        if arg not in TYPES[k]['self_kwargs']:
            if (
                'warning' in TYPES[k]['self_kwargs']
                and arg in TYPES[k]['self_kwargs']['warning']
            ):
                continue
            logger.warning('%s, %s: %s', k.__name__, arg, 'not in self_kwargs')

    for arg in TYPES[k]['self_kwargs']:
        if arg == 'warning':
            continue
        if has_dese and arg not in TYPES[k]['dese_kwargs']:
            logger.warning('%s, %s: %s', k.__name__, arg, 'not in dese_kwargs')
        if arg not in TYPES[k]['init_kwargs']:
            logger.warning('%s, %s: %s', k.__name__, arg, 'not in init_kwargs')
'''

with open('test_types.py', 'w') as w:
    w.write(f)
    logger.info('test_types.py has been written.')

#"""
