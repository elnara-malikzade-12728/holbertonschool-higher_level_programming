#!/usr/bin/env python3
"""Defines a custom Class named CustomObject."""
import pickle


class CustomObject(object):
    """Represents a custom class with attributes."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the CustomObject attributes."""
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Is Student: ", self.is_student)


    def serialize(self, filename):
        """Serialize the CustomObject instance."""
        with open(filename, "wb") as f:
            return pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the CustomObject instance."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except (pickle.UnpicklingError, EOFError):
            print(f"Error: The file '{filename}' is corrupted or empty.")
        except AttributeError:
            print(f"Error: The class structure has changed"
                  f" since this file was saved.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
