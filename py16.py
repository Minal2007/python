import math

# Base class
class Shape:
    def area(self):
        return 0

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create a list of different shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(2, 9)
]

# Demonstrate polymorphism
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")
