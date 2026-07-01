#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The text content to write into the file. Defaults to "".

    Returns:
        int: The total number of characters successfully written.
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
