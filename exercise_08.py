"""Create a base class called vehicle with a method start() that print “Vechice started” 
create a derived class called Car that inherits from Vechicle and overrides the start start() method to print “Car Started”."""


class vehicle:
    def start(self):
        print("Vehicle started")
class Car(vehicle):
    def start(self):
        print("car started")

obj_01=Car()
obj_01.start()
