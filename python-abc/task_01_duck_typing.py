#!/usr/bin/env python3
"""
This module demonstrates the concepts of Abstract Base Classes,
interfaces, and duck typing in Python by implementing geometric shapes.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract Base Class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a Circle, inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initializes the Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates and returns the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle, inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with a width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape_obj):
    """
    Prints the area and perimeter of a shape object using Duck Typing.
    It assumes the object implements 'area' and 'perimeter' methods.
    """
    print(f"Area: {shape_obj.area()}")
    print(f"Perimeter: {shape_obj.perimeter()}")
