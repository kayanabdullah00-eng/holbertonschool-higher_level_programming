#!/usr/bin/env python3
"""
Module for mixins exploration using SwimMixin, FlyMixin, and Dragon.
This module demonstrates how mixins are used to add specific behaviors
to classes without creating a complex inheritance hierarchy.
"""


class SwimMixin:
    """Mixin class that provides swimming functionality."""

    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying functionality."""

    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a Dragon that composes capabilities
    from both SwimMixin and FlyMixin, and has its own roar method.
    """

    def roar(self):
        """Prints the dragon's unique roaring behavior."""
        print("The dragon roars!")
