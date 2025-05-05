
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"



class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  
    def add_employee(self, employee):
        self.employees.append(employee)  

    def show_department_details(self):
        print(f"Department: {self.dept_name}")
        for emp in self.employees:
            print(emp.get_details())



emp1 = Employee("Abiha", 101)
emp2 = Employee("Hassan", 102)


sales_dept = Department("Sales")


sales_dept.add_employee(emp1)
sales_dept.add_employee(emp2)


sales_dept.show_department_details()
