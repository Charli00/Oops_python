'''5)create a class called teacher

Create a variable = name and registry number using constructor.

Create a function called display which should display the name and registry number of the teacher

Create t1 and t2 object and pass the name and reg no value through object.
'''

class teacher:
    def __init__(self,name,registry): #arguments or variables
        self.real_name=name              #class instance
        self.register_number=registry
    def display(self):
        print(f"The Teacher name is {self.real_name} and his/her registered number is {self.register_number}")


#created a object pass the arguments
t1=teacher("LALLY","9523")
t1.display()
print("\n")
t2=teacher("swathi","9056")
t2.display()
