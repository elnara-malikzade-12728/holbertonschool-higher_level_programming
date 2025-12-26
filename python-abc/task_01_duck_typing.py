#!/usr/bin/env python3
"""Defines an abstract class Shape."""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Represents an abstract class Shape."""
    @abstractmethod
    def area(self):
        """Defines an abstract  area method."""
        pass

    @abstractmethod
    def perimeter(self):
        """Defines an abstract  perimeter method."""
        pass

class Circle(Shape):
    """Represents an abstract class Shape."""

    def __init__(self, radius):
        """Initializes Circle."""
        self.radius = radius

    def area(self):
        """Implements the area method."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Implements the perimeter method."""
        return 2 * (pi * self.radius)

class Rectangle(Shape):
    """Represents an abstract class Shape."""

    def __init__(self, width, height):
        """Initializes Rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Implements the area method."""
        return self.width * self.height

    def perimeter(self):
        """Implements the perimeter method."""
        return 2 * (self.width + self.height)

def shape_info(self):
    """Implements the shape_info method."""
    print(f"Area: {self.area()}")
    print(f"Perimeter: {self.perimeter()}")

if __name__ == "__main__":
    circle = Circle(3)
    rectangle = Rectangle(4, 5)

    shape_info(circle)
    shape_info(rectangle)



