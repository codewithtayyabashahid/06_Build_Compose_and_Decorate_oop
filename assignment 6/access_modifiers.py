class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           
        self._salary = salary      
        self.__ssn = ssn          

# Creating an object of the Employee class
emp = Employee("Abiha", 50000, "123-45-6789")

# Accessing public variable
print("Public: Name =", emp.name) 


print("Protected: Salary =", emp._salary)

try:
    print("Private: SSN =", emp.__ssn) 
except AttributeError as e:
    print("Private: SSN = Access denied due to error:", e)

print("Private (with name mangling): SSN =", emp._Employee__ssn)  
