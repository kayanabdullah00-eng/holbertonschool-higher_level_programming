#!/usr/bin/env python3
"""
Module for Shape, Circle, Rectangle and duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a shape."""

    @abstractmethod
    def area(self):
        """Method to compute area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to compute perimeter."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Return area of circle using absolute value of radius."""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Return perimeter of circle using absolute value of radius."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle using absolute values."""
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """Return perimeter of rectangle using absolute values."""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
