#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a Student class."""

    def __init__(self, first_name, last_name, age):
        """Initializes the first_name, last_name and age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
