#!/usr/bin/python3
"""
This module contains a function that appends a string to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The text content to append to the file. Defaults to "".

    Returns:
        int: The total number of characters successfully appended.
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
