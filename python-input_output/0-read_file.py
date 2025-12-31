#!/usr/bin/python3
"""Defines a read_file function."""


def read_file(filename=""):
    """Reads a file and prints it to stdout."""

    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
