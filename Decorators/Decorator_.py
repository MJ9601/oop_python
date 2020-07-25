# DEcorator


# first class function allows us to tread function as object
# closure allows us to take advantage of first class function and return inner_function
# that remeber and has access to the arguments and local varible which create by outer function

# decorator pass a function as argument and excute it and return a function
# why Decorators

# decoratoring our function allows us to easily add functionality to our existing function
# by adding that functionality inside out wrapper function
# for example in example 1 without modify display function we can inside our wrapper function
# add anythings you want

# example 1
# simplest decorator that can be found
from functools import wraps
print('-------------example 1--------------------')


def decorator_function(orig_function):
    def wrapper_function():
        return orig_function()
    return wrapper_function  # the wrapper_function is waited to be executed


@decorator_function
def display():
    print('display function ran')


#display = decorator_function(display)
""" above line (is) does the same as @decorater_function"""
display()


# example 2
print('-------------example 2--------------------')


def decorator_function(orig_function):
    # adding *args and **kwargs allows to the decorator to be able to accepts multiple arbitrary arguments
    def wrapper_function(*args, **kwargs):
        print('wrapper has been excuted before {}'.format(orig_function.__name__))
        return orig_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('display function ran')


#display = decorator_function(display)
""" above line (is) does the same as @decorater_function"""
# display()


@decorator_function
def display_info(name, age):
    print('display_info ran with argument ({},{})'.format(name, age))


display_info('joe', 19)


# example 3
# decorator class

print('-------------example 3--------------------')
# this decorator class does the same as the previous decorator function


class MyDecorator(object):
    def __init__(self, orig_function):  # for outer function we should used the __init__ method
        self.orig_function = orig_function

    # for wrapper function we should use the __call__ method just remember to don't forget the ##self
    def __call__(self, *args, **kwargs):
        print('call method has been excuted before {}'.format(
            self.orig_function.__name__))
        return self.orig_function(*args, **kwargs)


@MyDecorator
def display():
    print('display function ran')


#display = decorator_function(display)
""" above line (is) does the same as @decorater_function"""
# display()


@MyDecorator
def display_info(name, age):
    print('display_info ran with argument ({},{})'.format(name, age))


display_info('joe', 19)


# example 4
# logger
# timer_decorator

print('-------------example 4--------------------')


def logger(orig_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {} and keyargument:{}'.format(args, kwargs))
        return orig_function(*args, **kwargs)

    return wrapper


def timer_function(orig_function):
    import time

    def wrapper(*args, **kwargs):
        t_ = time.time()
        result = orig_function(*args, **kwargs)
        t__ = time.time()-t_
        print('{} has been executed and {} second was duration of excution'.format(
            orig_function.__name__, t__))
        return result
    return wrapper


@timer_function
def display_info(name, age):

    import time
    time.sleep(2)
    print('display_info ran with argument ({},{})'.format(name, age))


display_info('joe', 19)


@logger
def display_info(name, age):

    import time
    time.sleep(2)
    print('display_info ran with argument ({},{})'.format(name, age))


display_info('joe', 19)


# example 5
# logger
# timer_decorator
# using both on a function using wraps
"""if you try to pass to decorator to a function the below line actually will happen
display=logger(timer_function(display))
which it cause that the inner function of timer_function (wrapper) get passed to the logger (try it to see what happens) which we don't want to happen
we want to that original function get passed to the both logger and timer function
so we use the wraps decorator to make that happen
"""

print('-------------example 5--------------------')


def logger(orig_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_function.__name__), level=logging.INFO)

    # if you add wraps decorator to the wrapper function in every decorator function it pass the original function to the next decorator
    @wraps(orig_function)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {} and keyargument:{}'.format(args, kwargs))
        return orig_function(*args, **kwargs)

    return wrapper


def timer_function(orig_function):
    import time

    # if you add wraps decorator to the wrapper function in every decorator function it pass the original function to the next decorator
    @wraps(orig_function)
    def wrapper(*args, **kwargs):
        t_ = time.time()
        result = orig_function(*args, **kwargs)
        t__ = time.time()-t_
        print('{} has been executed and {} second was duration of excution'.format(
            orig_function.__name__, t__))
        return result
    return wrapper


@logger
@timer_function
def display_info(name, age):

    import time
    time.sleep(2)
    print('display_info ran with argument ({},{})'.format(name, age))


display_info('sue', 35)

# example 6
# creating decorator which take arguments as
"""if you try to pass to decorator to a function the below line actually will happen
display=logger(timer_function(display))
which it cause that the inner function of timer_function (wrapper) get passed to the logger (try it to see what happens) which we don't want to happen
we want to that original function get passed to the both logger and timer function
so we use the wraps decorator to make that happen
"""

print('-------------example 6--------------------')


def prefixed_Decorator(arg):
    def decorator_function(org_function):
        def wrapper(*args, **kwargs):
            print(arg, 'Executing Before', org_function.__name__)
            result = org_function(*args, **kwargs)
            print(arg, 'Executing After', org_function.__name__)
            return result
        return wrapper
    return decorator_function


@prefixed_Decorator('logging:')
def display_info(name, age):
    print('display_info ran with argument ({},{})'.format(name, age))


display_info('sue', 35)
display_info('john', 23)
