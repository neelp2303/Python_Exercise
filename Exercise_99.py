"""Define a class Person and its two child classes: Male and Female. All classes have a method called
"getGender" which can print "Male" for Male class and "Female" for the Female class.
Use Subclass(Parentclass) to define a child class."""

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self, name):
        super().__init__(name, "Male")

class Female(Person):
    def __init__(self, name):
        super().__init__(name, "Female")


male = Male("John")
female = Female("Jane")

print(male.getGender())  
print(female.getGender())  