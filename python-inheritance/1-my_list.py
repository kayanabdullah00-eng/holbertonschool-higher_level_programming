#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
It includes methods to manage and display list elements in a sorted order.
"""


class MyList(list):
    """
    A custom list class that extends the functionality of the built-in list.
    Provides an additional method to print elements in an ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list sorted in ascending order.
        Assumes all elements within the list are of integer type.
        """
        print(sorted(self))
