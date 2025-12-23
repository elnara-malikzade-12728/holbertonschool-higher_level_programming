#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Represents a BaseGeometry class."""

    def area(self):
        """Raises an Exception with a message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
