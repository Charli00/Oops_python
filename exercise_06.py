'''create Two variables a and b

Create a function called add,sub,multiplication,division all function should take 2 variables as parameter

Pass the a and b value through the object().
'''

class calculator:
    def __init__(self,a,b):
        self.first_value=a
        self.second_value=b
    def added(self):
        print(f"The value of first {self.first_value} and the second value {self.second_value} and the addition of first and second value : {self.first_value+ self.second_value}")
    def subtract(self):
        print(f"The value of first {self.first_value} and the second value {self.second_value} and the subtraction of first and second value : {self.first_value - self.second_value}")
    def multiptly(self):
        print(f"The value of first {self.first_value} and the second value {self.second_value} and the mutliplication of first and second value : {self.first_value * self.second_value}")
    def divi(self):
        print(f"The value of first {self.first_value} and the second value {self.second_value} and the division of first and second value : {self.first_value / self.second_value}")


addition=calculator(3,4)
addition.added()

subtraction=calculator(12,34)
subtraction.subtract()

multiplication=calculator(4,67)
multiplication.multiptly()

division=calculator(36,6)
division.divi()
