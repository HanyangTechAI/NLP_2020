import functools

REGISTER = {}
def register(func):
    REGISTER[func.__name__] = func
    return func

def repeat(func_= None, *, num=1):
    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    if func_ is not None:
        return dec(func_)
    else:
        return dec

@repeat(3)
@register
def print_name(name):
    print(name)

REGISTER['print_name']('james')
