"""Define a class named Circle which can be constructed by a radius. The Circle class has a method which can
compute the area.
Use def methodName(self) to define a method."""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 22 / 7 * self.radius**2


value = Circle(7)
calculate_radius = value.area()

print("The area of the circle is: ", calculate_radius)
