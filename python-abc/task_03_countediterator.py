#!/usr/bin/env python3
"""
Module for CountedIterator.
This module defines a custom iterator class that wraps an iterable
and keeps track of the number of items successfully iterated.
"""


class CountedIterator:
    """
    An iterator wrapper that counts how many items have been fetched.
    """

    def __init__(self, some_iterable):
        """
        Initializes the CountedIterator with an iterable object
        and sets the counter to 0.
        """
        self.__iterator = iter(some_iterable)
        self.__counter = 0

    def get_count(self):
        """
        Returns the current count of items iterated so far.
        """
        return self.__counter

    def __next__(self):
        """
        Fetches the next item from the iterator, increments the counter,
        and returns the item. Raises StopIteration when empty.
        """
        try:
            item = next(self.__iterator)
            self.__counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself.
        Required to fully support the iterator protocol in Python.
        """
        return self
