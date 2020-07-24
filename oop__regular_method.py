#python programming oop
#regular method 


class Employee:

    employee_counter=0
    amount_of_raises =1.04 #this varible called as class varible which share between all method regarding the method
    def __init__(self,first,last,payment): # the init method act the same as the constructor in java
        #you have to pass all of your instance varible to init in order that can use them later
        #self do the work of this in java 
        self.first = first
        self.last = last
        self.payment = payment
        self.email =first + "."+ last+"@company.com"

        Employee.employee_counter+=1

    def full_name(self):# whatever you create method that you need to pass the varible you should pass the self to the method
        return '{} {}'.format(self.first,self.last)

    def apply_raises(self):
        self.payment=self.payment*self.amount_of_raises  #this order and following do the same things with one different 
        # in first one a specfic employee can have specific raise but in the second one they all share the same raise(the up order can change for one or all)
        #self.payment=payment*Employee.amount_of_raises





emp_1=Employee('sara','ford', 60000)
emp_2=Employee('rob', 'queen',120000)
print(emp_1.__dict__) # with this command you can see what varible the object has access of



print(emp_1.full_name())  # you should always put (), or it print only the method ditail
# this order and the following does the same things with one large different__ u cann't use the emp_1.full_name if you have 
# another class which it has the same method u should use the below order to specify the which class to use (call)
print(Employee.full_name(emp_2))

emp_1.amount_of_raises=1.05 # assgning amount of raises only for one employee
Employee.amount_of_raises=1.04 # assgning amount of raises for all employees

print(emp_1.payment)
Employee.apply_raises(emp_1) # applaying raise for employees
print(emp_1.payment)
