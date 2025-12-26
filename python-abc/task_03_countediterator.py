#!/usr/bin/env python3
"""Defines a CountedIterator class
that extends the built-in iterator from the iter function."""
from collections.abc import Iterator


class CountedIterator(Iterator):
    """Represents a CountedIterator class."""

    def __init__(self, iterable):
        """Initializes a CountedIterator object."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the number of items in the iterator."""
        return self.count

    def __next__(self):
        """Returns the next item from the iterator."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            # Re-raise StopIteration when the internal iterator is exhausted
            raise StopIteration
    def __iter__(self):
        """Returns a CountedIterator object."""
        return self

