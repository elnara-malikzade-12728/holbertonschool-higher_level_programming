#!/usr/bin/env python3
"""Defines a Fish, Bird and FlyingFish classes."""


class Fish:
    """Represents a Fish class."""
    def __init__(self):
        """Initializes a Fish class."""
        pass
    def swim(self):
        """Swims the fish."""
        print("The fish is swimming!")
    def habitat(self):
        """The fish lives in water."""
        print("The fish lives in water!")

class Bird:
    """Represents a Bird class."""
    def __init__(self):
        """Initializes a Bird class."""
        pass
    def fly(self):
        """Flies the bird"""
        print("The bird is flying!")
    def habitat(self):
        """The bird lives in the sky."""
        print("The bird lives in the sky!")

class FlyingFish:
    """Represents a FlyingFish class."""
    def __init__(self):
        """Initializes a FlyingFish class."""
        pass

    def fly(self):
        """Flies the FlyingFish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Swims the FlyingFish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """The flying fish lives both in water and the sky."""
        print("The flying fish lives both in water and the sky!")

if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mro())