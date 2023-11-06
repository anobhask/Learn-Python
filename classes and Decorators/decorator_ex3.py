# Decorators

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('dispaly funcation ran')

decorated_display = decorator_function(display)

decorated_display()