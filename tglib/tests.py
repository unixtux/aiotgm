from tglib.update_manager import _func_ok

print('test for checker and func for update_manager,\nthey must take 1 argument and they cannot be generators.')

print('Testing checker\n')
print(f'{_func_ok(lambda x: ...)=}')
print(f'{_func_ok(lambda *ar, x: ...)=}')
print(f'{_func_ok(lambda *, x: ...)=}')
print(f'{_func_ok(lambda x, **kw: ...)=}')
print(f'{_func_ok(lambda x, /: ...)=}')

gen_str = '''\
def gen(x):
    yield'''

def gen(x):
    yield

print('Testing generator:', gen_str, sep='\n')
print(f'{_func_ok(gen)=}')

print('Testing async function\n')
print(f'{_func_ok(lambda x: True, must_be_coro=True)=}')

async_func_str = '''\
async def foo(x):
    ...'''

async def foo(x):
    ...

print('async func is:', async_func_str, sep='\n')
print(f'{_func_ok(foo, must_be_coro=True)=}')

async_gen_str = '''\
async def bar(x):
    yield'''

async def bar(x):
    yield

print('async gen is:', async_gen_str, sep='\n')
print(f'{_func_ok(bar, must_be_coro=True)=}')

