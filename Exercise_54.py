"""Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a
method which can compute the area.
Use def methodName(self) to define a method."""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

dimensions = Rectangle(50,20)

print(dimensions.area()) 