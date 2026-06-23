#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
It implements a square geometry object using evaluated size.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with validated size.

        Args:
            size (int): The side length of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
