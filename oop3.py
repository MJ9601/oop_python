# oop Special class (Magic and Dunder) Method
# the method which surrounded by two underscores called Dunder

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
        """ in first one a specfic employee can have specific raise 
        but in the second one they all share the 
        same raise(the up order can change for one or all)"""
        #self.payment=payment*Employee.amount_of_raises

    #it is good to have one things of following around specailly __repr__
    def __repr__(self):# should be used for debugging and logging and things like that
        return "Employee('{}','{}',{})".format(self.first, self.last, self.payment)    # recreating the object from

    def __str__(self):# readable representation of object and it should be used for display to the inuser
        return '{} - {}'.format(self.full_name(), self.email)
    def __add__(self, other):
        # this method take to object the first one is the main and the other is right side of addition ** in this case it add payment of two employee
        return self.payment+other.payment

    def __len__(self):# this method return the length of the object which passing in to in this case "full_name ()"
        return len(self.full_name())


emp_1=Employee('sara','ford', 60000)
emp_2=Employee('rob', 'queen',120000)

print(emp_1)

print(emp_1.__repr__())
print(emp_1.__str__())  ## the next two lines do the same as above
#print(repr(emp_1))
#print(str(emp_1))

print(emp_1+emp_2)# this command line add two employee payment to eachother
print(len(emp_1))# this command line print the length of full_name employee for inuser




""" the following code lines show how the add method actually works 
they work the same as no, they are #add method for adding int and string"""
#print(int.__add__(1,2))
#print(str.__add__('a','b'))
""" the following code lines show how the add method actually works""" 
#print(len('test'))
#print('test'.__len__)



## return NotImplemented
""" what does the above code is basically when they return #NotImplemented they don't want to  throw an error because
might the other object knows how to handle the operation
So returning #NotImplemented in a way to fall back on the other object to
see if it knows how to handle the operation
and if none of them know how to handle the operation
then it will eventually throw an error (exception more likely)""" 

