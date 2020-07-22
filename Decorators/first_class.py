 #first class function

def square(x):
    return x**2

f=square  # you can remove the '()' from the function in order to set f as function
# leaving the () cause the function to be executed
print(square)
print(f)
print(f(1)) # this line act as the function

# if a function accepts other functions as argument or return them as results, it called higher order functions
#higher function

#example 1:
def cube(x):
    return x**3

def my_value(func, args):
    # this function takes a function and array as arguments
    result=[]
    for i in args:
        result.append(func(i))
    return result# lack of () cause the function to doesn't executed and get set for the passing as argument

cub=my_value(cube,[1, 2, 3, 4, 5])
print(cub)




#example 2:
def logger(msg):
    def log_msg():
        print('log:' + msg)
    return log_msg

log_hi=logger('hello_func')
log_hi()


#example 3
def tag_html(tag_):
    def text_(msg):
        print('<{0}>{1}</{0}>'.format(tag_, msg))

    return text_
# when we pass function as argument what does happen is that 
# argument actually will be equal to the return function
print_tag=tag_html('div')
print_tag('this is simple test')
print_tag('test 2')
print_h4=tag_html('h4')
print_h4('test 4 ')