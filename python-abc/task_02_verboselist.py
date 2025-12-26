#!/usr/bin/env python3
"""Defines a VerboseList class that inherits from the built-in list class."""


class VerboseList(list):
    """Represents a VerboseList class that inherits from the built-in list class."""

    def append(self, item):
        """Implements the append method."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Implements the extend method."""
        super().extend(items)
        count = 0
        for i in items:
            count += 1
        print("Extended this list with [{}] items.".format(count))

    def remove(self, item):
        """Implements the remove method."""
        if item in self:
            super().remove(item)
            print("Removed [{}] to the list.".format(item))
        #else:
         #   print("[{}] not found in list.".format(item))

    def pop(self, index=-1):
        """Removes and returns the item at the given index with a message."""
        removed_item = super().pop(index)
        print("Popped [{}] from the list.".format(removed_item))
        return removed_item

if __name__ == "__main__":

    vl = VerboseList()
   # vl = VerboseList([1,5,7])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)

