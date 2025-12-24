#!/usr/bin/python3
"""Defines a Rectangle class based on BaseGeometry class."""
import importlib
"""Dynamically import the module using its string name."""

bg_module = importlib.import_module("7-base_geometry")

class Rectangle(bg_module.BaseGeometry):
    """Represents Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes private width and height."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
