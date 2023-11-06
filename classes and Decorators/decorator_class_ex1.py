# Decorators

from typing import Any


def decorator_class(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}()')
        return original_function(*args, **kwargs)
    return wrapper_function

class decorator_class(object):

    def __init__(self, original_function) -> None:
        self.original_function = original_function
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f'call method executed this before {self.original_function.__name__}()')
        return self.original_function(*args, **kwds)


@decorator_class
def display():
    print('dispaly funcation ran')

@decorator_class
def display_info(name: str, age:int) -> None:
    print(f'display_info() ran with argumnets : {name, age}')
#decorated_display = decorator_class(display)
#
#decorated_display()
display()
display_info('Anoop', 39)