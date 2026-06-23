#!/usr/bin/python3
"""
This module provides a function to look up object attributes and methods.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing attributes and methods.
    """
    return dir(obj)
