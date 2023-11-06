# Decorators

def outer_function(msg):
    message = msg

    def inner_function() -> None:
        print(message)
    return inner_function

my_func = outer_function("my dear")
by_func = outer_function("by dear")
my_func()
by_func()