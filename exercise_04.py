'''4) create a class called fruit

Create a variable called color using __init__ method

Create a object called apple “pass the color variable as a parameter through object”.'''


class fruit:
    def __init__(self,color):
        self.color=color
    def fruit_Color(self):
        print(f"Fruit clor is: {self.color}")

apple=fruit("red")
apple.fruit_Color()

orange=fruit("orange")
orange.fruit_Color()

