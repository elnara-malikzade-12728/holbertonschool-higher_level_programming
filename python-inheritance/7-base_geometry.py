#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Represents a BaseGeometry class."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer."""
        if type(value) is int:
            pass
        elif type(value) is float:
            raise TypeError("age must be an integer")
        else:
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
