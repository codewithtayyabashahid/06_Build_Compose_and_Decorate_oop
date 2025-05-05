#class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) 
        self.subject = subject

t = Teacher("M. Hassan", "Maths")

# Output 
print("Name:", t.name)
print("Subject:", t.subject)
