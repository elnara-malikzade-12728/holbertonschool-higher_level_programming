#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    @property
    def width(self):
        """Get width."""

        return self.__width

    @width.setter
    def width(self, value):
        """Set width with a value."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Set height with value."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """Initializes rectangle with optional width and height,
           and increments count each time an instance is created"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Returns the rectangle area."""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints rectangle with the character #."""

        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []
        print_symbol = str(self.print_symbol)
        for i in range(self.__height):
            lines.append(print_symbol * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """Returns string representation of the rectangle."""

        return f"Rectangle{self.__width, self.__height}"

    def __del__(self):
        """Decrements when an instance is deleted and
           Prints message when an instance is deleted."""

        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance."""

        new_rect = cls(size, size)
        return new_rect
