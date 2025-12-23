#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """Represents MyList class that inherits from List Class."""

    def print_sorted(self):
        """Prints list in sorted order."""
        print(sorted(self))
