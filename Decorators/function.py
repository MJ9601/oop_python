#function

def hello_func(greeting, name='you'): # the init value should be specify if you might want to don't pass argument
    return '{} {}'.format(greeting, name) 


print(hello_func('Hi', name='jack'))
"""if you pass argument, your requirment positioning argument 
have to come before your key word argument if you tried backword you getting an error"""



#example 1
#using * and ** to accept and return arbitary argument and keyword arguments
def student_info(*args, **kwargs):
    """ this function with using * and ** before the argument allows us to can pass
    in arbitary positionig argument and keyword arguments
    and it retrun them in tuple and dictionary (* and ** respectively)"""
    print(kwargs)
    print(args)

student_info('math','art','chem', name='john',age=18)

courses =['chem', 'art','phy']
info ={'name':'John','sur_name':'sue','age':18,'color_eye':'blue'}

student_info(*courses,**info) #if you pass them with * and ** their be unpack you getting an error possibly but if passing them with * and **
# they gonna be unpack automatically



#example 2
#finding the leap year and calculating the days of month you in
month_days=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """ return True for leap year and False for non-leap year"""
    return year%4==0 and (year%100!=0 or year%400==0)

def days_in_month(year,month):
    """ return number of days in that month in that year"""
    if not 1<=month<=12:
        return 'Invalid Month'
    if month==2 and is_leap(year):
        return 29
    return month_days[month]


print(days_in_month(2020, 6))
