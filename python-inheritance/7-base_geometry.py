#!/usr/bin/python3
"""
This module defines a class BaseGeometry based on 6-base_geometry.py.
It provides methods for input validation and area calculations.
"""


class BaseGeometry:
    """
    A class representing base geometry with validation capabilities.
    """

    def area(self):
        """
        Public instance method to calculate area.

        Raises:
            Exception: Always, because it is not implemented yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name associated with the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
