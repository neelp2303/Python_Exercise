"""Define a class named Shape and its subclass Square. The Square class has an init function which takes a
length as an argument. Both classes have an area function which can print the area of the shape where the
Shape's area is 0 by default.
To override a method in super class, we can define a method with the same name in the super class."""


class Shape:
    def __init__(self):
        self.area = 0

    def Area(self):
        print("Area of the shape is", self.area)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.area = length * length

    def Area(self):
        print("Area of the square is", self.area)


square = Square(5)
square.Area()
