#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a Student class."""

    def __init__(self, first_name, last_name, age):
        """Initializes the first_name, last_name and age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""

        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res

        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        return self.__dict__.update(json)
