# different between __repr__ and __str__


# the goal of __repr__ is to be unambiguous
# the goal of __str__ is to be readable


import datetime
import pytz
a=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b=str(a)
print('str(a): {}'.format(str(a)))
print('str(b): {}'.format(str(b)))
print('------------------')
print('repr(a): {}'.format(repr(a)))
print('repr(b): {}'.format(repr(b)))

'''
the __repr__ is used for developer specially can be used
for ##debugging purposes to see what kind of variable an object return or stored
## but __str__ is simply ment for clean and nice printing 
does not give us any futher info on object and variable that was stored in object.
'''

