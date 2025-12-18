#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0

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
        for i in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """Returns string representation of the rectangle."""

        return f"Rectangle{self.__width, self.__height}"

    def __del__(self):
        """Decrements when an instance is deleted and
           Prints message when an instance is deleted."""

        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
