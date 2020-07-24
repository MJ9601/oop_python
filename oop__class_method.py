#python programming oop-class method

class Employee:
    raise_amt=1.04
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email =last+"."+first+"@mail.com"
    def apply_raiser(self):
        self.salary=self.salary*self.raise_amt
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    @classmethod #this command make the program to excute the class method first
    def set_raise(cls, amount):
        cls.raise_amt=amount
    @classmethod
    def from_String(cls,emp_str):# this class method split the string which passing in to and return it as first, last, and salary instance variable
        #cls like self is specific and should pass as first argument of class method
        first,last,salary=emp_str.split('-')# split part
        return cls(first,last,salary)# return part as instance variable
    



Employee.set_raise(1.05)
emp1=Employee('sara','ford',68900)
emp2=Employee('alex','queen',56999)
print(Employee.raise_amt)
print(emp1.raise_amt)


#alternative constracture: use the class methad in order to provide multiway to create object

emp_1='john-doe-7000'
emp_2='steve-smith-7000'
emp_3='jane-doe-90000'
new_emp_1=Employee.from_String(emp_1)
new_emp_2=Employee.from_String(emp_2)
new_emp_3=Employee.from_String(emp_3)


print(new_emp_1.email)
print(new_emp_2.salary)


