#!/usr/bin/python3
"""Defines a function that returns the dictionary description
 with simple data structure for JSON serialization of an object."""
import json


def class_to_json(obj):
    """Returns teh dictionary description with simple
 data structure (list, dictionary, string, integer and boolean)
 for JSON serialization of an object."""
    return json.dumps(obj.__dict__)
