'''7)Create a class called Animal with method Sound() that prints “Animals makes sound” .
Create a derived class called Dog that inherits from animal and overrides the the sound() method to print “ Dog barks”.
Create another derived class called Bird that inherits from animal and overrides the sound() method to print “Bird sing”'''

class Animal:
    def sound(self):
        print("Animal makes sound ")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Bird(Animal):
    def sound(self):
        print("Bird sing")


Dog_01=Dog()
Dog_01.sound()

print("\n")

Bird_01=Bird()
Bird_01.sound()
