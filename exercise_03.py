'''.create a clss called student

Create a variable =name and register number using constructor

Create a function called display which should display thee name and registry number of the student.

'''

class student:
    def __int__(self):
        self.name=""
        self.register=""
    def display(details):
        print(f"NAME OF THE STUDENT IS: {details.name} and his/her registry number is: {details.register}")

department=student()

department.name="RAMESH"
department.register="1003920"
department.display()

department.name="RAME"
department.register="1003"
department.display()
