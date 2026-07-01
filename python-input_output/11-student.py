#!/usr/bin/python3
"""
This module defines a Student class with serialization and deserialization.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes contained
        in this list are retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list, optional): A list of strings specifying which
                attributes to include in the returned dictionary.

        Returns:
            dict: A filtered dictionary of the student's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary where keys match public attribute names
                and values correspond to their replacement values.
        """
        for key, value in json.items():
            setattr(self, key, value)
