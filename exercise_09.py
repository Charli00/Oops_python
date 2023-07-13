'''Create a base class called EMPLOYEE with properties name and salary.
Create a derived class called Manager that inherits from Employee and adds a property department.
Write a method in Manager to display the name,salary and department of the manager.'''

class EMPLOYEE:
    def __init__(self,name,salary):
        self.good_name=name
        self.payslip=salary
class Manager(EMPLOYEE):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print(f"The manager name is {self.good_name} and salary {self.payslip} working in {self.department} department ")

obj_01=Manager("charles",5000000000000,"IT")
obj_01.display()
