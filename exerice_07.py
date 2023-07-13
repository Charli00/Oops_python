'''Create a base class called Person with a constructor that takes a name as a parameter.
Create a derived class called student that inherits from Person and has a constructor that takes a parameter called grades.
Write a method in Student to display the name and grade of the student.
Use super Keyword to achieve this.'''

class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,grades):
        super().__init__(name)
        self.grades=grades
    def display(self):
        print(f"The student name {self.name} and his/her graded is {self.grades}")

obj_01=Student("Ramesh","B")
obj_01.display()