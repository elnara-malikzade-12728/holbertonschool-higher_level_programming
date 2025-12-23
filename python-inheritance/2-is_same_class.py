#!/usr/bin/python3
"""Defines a function to find an exact instance of the class."""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance
       of the specified class; otherwise False."""

    return type(obj) is a_class
