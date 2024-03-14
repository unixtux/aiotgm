#!/bin/env python3

if __name__ != '__main__':
    import os
    raise OSError(f'{os.path.basename(__file__)} must be launched from __main__')

import sys
sys.path.append('../')
from aiotgm.update_manager import _func_ok

print('\n- Testing checker and function of the update_managers, they must take 1 argument and they cannot be generators.\n')

print("~" * 55)
print('\n- Testing checker:\n')
print(f'{_func_ok(lambda x: ...) = }')
print(f'{_func_ok(lambda x, /: ...) = }')
print(f'{_func_ok(lambda *ar, x: ...) = }')
print(f'{_func_ok(lambda *, x: ...) = }')
print(f'{_func_ok(lambda x, **kw: ...) = }\n')

gen_str = '''\
def gen(x):
    yield'''

def gen(x):
    yield

print("~" * 55)
print('\n- Checking for a normal function using a generator:', gen_str, sep='\n\n')
print(f'\n{_func_ok(gen) = }\n')

print("~" * 55)
print('\n- Checking for an async function using a lambda function:\n')
print(f'{_func_ok(lambda x: True, must_be_coro = True) = }\n')

async_func_str = '''\
async def foo(x):
    ...'''

async def foo(x):
    ...

print("~" * 55)
print('\n- Checking for an async function using an async function:', async_func_str, sep='\n\n')
print(f'\n{_func_ok(foo, must_be_coro = True) = }\n')
print("~" * 55)

async_gen_str = '''\
async def bar(x):
    yield'''

async def bar(x):
    yield

print('\nChecking for an async function using an async generator:', async_gen_str, sep='\n\n')
print(f'\n{_func_ok(bar, must_be_coro = True) = }\n')

print("~" * 55)
