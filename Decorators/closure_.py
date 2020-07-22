#closures

""" def outer_function():
    messag='Hello'
    def inner_functions():
        print(messag)

    return inner_function()   ### putting () at the in of function cause the excution of it

outer_function() """

# closure: in simple defination::#  a closure is an inner_function that remember
# and has access to the variable and local scope in which created by outer function
#even after outer function has finish excuting
def outer_function(msg):
    messag=msg  # variable which inner_function has access of called free varible
    def inner_function():
        print(messag)

    return inner_function   ### putting () at the in of function cause the excution of it

func=outer_function('sara')
print(func.__name__)# this line display the name of the function

h_func=outer_function('hi there')
h2_functions=outer_function('hello_func')

h_func()
h2_functions()



#example 2

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def log(func):
    def handle(*args):
        logging.info('Running"{}" with arguments{}'.format(func.__name__, args))
        print(func(*args))
    return handle

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
add_log=log(add)
sub_log=log(sub)

add_log(3,8)
sub_log(9,3)

