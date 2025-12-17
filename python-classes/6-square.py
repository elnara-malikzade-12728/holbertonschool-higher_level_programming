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

    @property
    def position(self):
        """Creates a property with getter."""

        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""

        error_message = "position must be a tuple of 2 positive integers"
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError(error_message)
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with private size."""

        self.size = size
        self.position = position

    def area(self):
        """Returns the current square area."""

        return self.__size ** 2

    def my_print(self):
        """Prints a square in stdout with the character #."""

        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
