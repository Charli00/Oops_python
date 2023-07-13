'''Create a base class called Shape with a method area() that returns 0.
Create a derived class called Rectangle that inherits from Shape and overrides the area() method to calculate and 
return the area of a rectangle.'''

class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def area(self,length,breadth):
        self.l=length
        self.b=breadth
        print(f"The length {self.l} and breadth {self.b} and the total {self.l*self.b}")

obj_01=Rectangle()
obj_01.area(12,13)
