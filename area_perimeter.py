#Abstract Base Class Using the abc module, define an abstract class Shape with abstract methods area() and perimeter(). Implement Rectangle and Circle subclasses. Write a program to calculate their area and perimeter.
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

rect = Rectangle(10,5)
circle = Circle(7)

print("Rectangle")
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

print("\nCircle")
print("Area:", round(circle.area(),2))
print("Perimeter:", round(circle.perimeter(),2))
