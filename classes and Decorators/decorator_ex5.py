# Decorators

def decorator_function(original_function) -> object:
    def wrapper_function() -> object:
        print(f'wrapper execyuted this before {original_function.__name__}()')
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('dispaly funcation ran')

#decorated_display = decorator_function(display)
#
#decorated_display()
display()