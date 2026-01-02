#!/usr/bin/env python3
"""Defines a function to serialize and deserialize Python objects"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as file:
        return json.dump(data, file)

def load_and_deserialize(filename):
    with open(filename, 'r') as file:
        return json.load(file)