'''
main.py
'''
from app import Resident

resident = Resident(name='Jennifer', age='28', id=23)

resident.print_name()
resident.print_age()
resident.print_id()

resident.title()
print(Resident.mro())

'''
app.py
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)
    
    def print_age(self):
        print(self.age)
    
    def title(self):
        print('In Person class')

class Student:
    def __init__(self, id):
        self.id = id

    def print_id(self):
        print(self.id)
    
    def title(self):
        print('In Student class')

class Resident(Person, Student):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)