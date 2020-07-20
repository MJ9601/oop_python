#oop
# inheritance (subclass and parent class)

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


class Developer(Employee):
    amount_of_raises=1.10 ## this line of code rewrite the value of this varible in parent class
    def __init__(self,first, last, payment, prog_lang):
        super().__init__(first, last, payment) ## this command and the following line of code does the same things
       # Employee.__init__(self,first,last,payment)
       ## the two up lines make the parent class to initialize the passing argument
        self.prog_lang= prog_lang

class Manager(Employee):
    def __init__(self,first, last, payment, employees=None):
        super().__init__(first, last, payment) ## this command and the following line of code does the same things
        if employees==None:# you can not pass empty list for init so pass the None value then use an if condition to pass the empty list
            self.employees =[]
        else:
            self.employees = employees
    
    def add_employee(self,emp):# give the manager ability of adding employees
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):# give the manager ability of removing employees
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):# it print the list of employees which the manager superwise them
        for e in self.employees:
            print("-----------"+ e.full_name()+"-----------")



emp_1=Developer('sara','ford', 60000,'python')
emp_2=Developer('rob', 'queen',120000,'java')

mag_1=Manager('joe','sue',120000,[emp_1])
print(mag_1.email)

Manager.add_employee(mag_1,emp_2)
mag_1.remove_emp(emp_1)
mag_1.print_employees()

print(emp_1.email)
#print(help(Developer))  ## this line of code gives you the info about the developer class and inheritance

# the following two lines of code are the method define inside the python ## they both return False and True value
print(isinstance(mag_1,Manager)) ## this line of code gives you info which is the object is the instance argument of class or not
print(issubclass(Developer,Manager)) ## this line of code gives info that whatever first class is the subclass of the second class

