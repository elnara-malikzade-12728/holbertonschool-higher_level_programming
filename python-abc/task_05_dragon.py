#!/usr/bin/env python3
"""Defines two mixin classes."""


class SwimMixin(object):
    """Swims the dragon."""

    def swim(self):
        """The creature swims!"""
        print("The creature swims!")

class FlyMixin(object):
    """Flies the dragon."""

    def fly(self):
        """The creature flies!"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Represents a Dragon."""

    def fly(self):
        """The creature flies!"""
        super().fly()

    def swim(self):
        """The creature swims!"""
        super().swim()

    def roar(self):
        """The dragon roars!"""
        print("The dragon roars!")

if __name__ == "__main__":
    draco = Dragon()
    draco.swim()  # Outputs: The creature swims!
    draco.fly()  # Outputs: The creature flies!
    draco.roar()  # Outputs: The dragon roars!