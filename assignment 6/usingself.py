class student:
    def __init__(self, name, marks):
       self.name = name
       self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

student1 = student("Abiha",92)
student1.display()