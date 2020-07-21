# Decorators

def outer_function():
    message ='Hi there'

    def inner_functions():
        print(message)
    return inner_functions()
outer_function()
