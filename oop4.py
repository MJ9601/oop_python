# pyhton programing oop
# proprety decorator

class Employee:
    def __init__(self,first ,last):
        self.first = first
        self.last = last
        

    @property  # this decorator change the type of method to object 
    def email(self):
         return '{}.{}@mail.com'.format(self.first,self.last)

    @property
    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    @full_name.setter  # this decorator allows us to can extract the argument form the method passing
    def full_name(self,name):
        first,last = name.split(' ')
        self.first=first
        self.last=last

    @full_name.deleter  #this decorator allows us to delete the argument form the method passing
    def full_name(self):
            print('Delete employee name') 
            self.first=None  #because a argument should be initialize and had to have a something I passed them ##None
            self.last=None




empl = Employee('sara','ford')


empl.first='Adam'
empl.full_name= 'jack harper'
print(empl.full_name)
print(empl.email)
print(empl.first)
del empl.full_name
