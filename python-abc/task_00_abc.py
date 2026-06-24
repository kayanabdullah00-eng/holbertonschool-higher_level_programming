#!/usr/bin/env python3
"""
This module defines an abstract base class Animal and its subclasses
Dog and Cat to demonstrate the concepts of Abstract Base Classes (ABCs)
and method overriding in Python.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Base Class representing a generic Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a Dog.
    """

    def sound(self):
        """
        Returns the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a Cat.
    """

    def sound(self):
        """
        Returns the sound made by a cat.
        """
        return "Meow"
