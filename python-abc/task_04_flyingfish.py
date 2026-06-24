#!/usr/bin/env python3
"""
Module for multiple inheritance exploration using Fish, Bird, and FlyingFish.
This module demonstrates how Python handles multiple inheritance and
Method Resolution Order (MRO).
"""


class Fish:
    """Class representing a Fish."""

    def swim(self):
        """Prints the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird."""

    def fly(self):
        """Prints the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish that inherits from both Fish and Bird.
    Demonstrates multiple inheritance.
    """

    def swim(self):
        """Overrides the swim method for FlyingFish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Overrides the fly method for FlyingFish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Overrides the habitat method for FlyingFish."""
        print("The flying fish lives both in water and the sky!")
