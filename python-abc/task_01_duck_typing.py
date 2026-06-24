#!/usr/bin/env python3
"""
This module defines the VerboseList class which extends the built-in
Python list to provide notification messages when items are modified.
"""


class VerboseList(list):
    """
    A custom list class that prints messages upon adding or removing items.
    """

    def append(self, item):
        """
        Appends an item to the list and prints a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extends the list with an iterable and prints a notification.
        """
        # Convert to list first to safely get the count, 
        # especially if a generator or iterator is passed.
        items_list = list(iterable)
        item_count = len(items_list)
        super().extend(items_list)
        print(f"Extended the list with [{item_count}] items.")

    def remove(self, item):
        """
        Removes an item from the list and prints a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item from the list at the given index and prints a notification.
        Defaults to the last item if index is not provided.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
