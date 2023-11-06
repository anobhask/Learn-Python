# Decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}()')
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('dispaly funcation ran')

@decorator_function
def display_info(name: str, age:int) -> None:
    print(f'display_info() ran with argumnets : {name, age}')
#decorated_display = decorator_function(display)
#
#decorated_display()
display()
display_info('Anoop', 39)