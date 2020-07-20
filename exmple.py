#static method in oop
# the class method pass the class as first argument
# the static method does not pass nor the class or intance argument
import datetime
class Employee:
    @staticmethod
    def is_workday(day):# static method does not get instance or class argument as first argument
        # we can pass the argument with wanted
        if day.weekday() ==5 or day.weekday() ==6:# monday=0 and sunday=6
            return False #if is sunday or satureday return False
        return True# if not return True

my_date = datetime.date(2020,7,20)
print(Employee.is_workday(my_date))

# if you not using self inside of regular method or cls inside of class method you should consider using static method
#the static method is used if you don't access anywhere inside the function

