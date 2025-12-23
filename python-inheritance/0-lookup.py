#!/usr/bin/python3
"""Returns the list of available attributes and methods of an object."""


def lookup(obj):
    """Return a list of attributes and methods of an object."""
    return dir(obj)
