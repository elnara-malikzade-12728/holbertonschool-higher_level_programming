#!/usr/bin/python3
"""Defines a function to find out whether
    the instance belongs to an object."""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
       or if the object is an instance of a class
       that inherited from the specified class;
       otherwise False."""

    if not isinstance(obj, a_class):
        return False
    else:
        return True
