#!/usr/bin/python3
"""Defines a Rectangle class based on BaseGeometry class."""


class Rectangle(BaseGeometry):
    """Represents Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes private width and height."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
