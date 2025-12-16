#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    @property
    def size(self):
        """Creates a property with getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Creates a property setter."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        """Initializes a square with private size."""

        self.__size = size

    def area(self):
        """Returns the current square area."""

        return self.__size ** 2
