#!/usr/bin/env python3
"""
Module for VerboseList that extends built-in list.
"""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Append item and print message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list and print message with count."""
        count = len(list(iterable))
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Print message and remove item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print message and pop item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
