#!/usr/bin/env python3
"""Defines an Animal class."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Represents an animal class."""

    @abstractmethod
    def sound(self):
        """Represents an animal sound."""
        pass

class Dog(Animal):
    """Represents an animal dog."""
    def sound(self):
        """Implements dog sound."""
        return "Bark"

class Cat(Animal):
    """Represents an animal cat."""
    def sound(self):
        """Implements cat sound."""
        return "Meow"
