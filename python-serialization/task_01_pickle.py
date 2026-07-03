#!/usr/bin/env python3
"""Module for pickling custom objects."""

import pickle


class CustomObject:
    """Custom class for serialization."""

    def __init__(self, name, age, is_student):
        """Initialize attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize object to file."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError,
                pickle.PickleError,
                EOFError,
                AttributeError):
            return None
