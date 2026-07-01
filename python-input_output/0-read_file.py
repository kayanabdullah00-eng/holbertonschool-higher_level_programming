#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints its content.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to standard output.

    Args:
        filename (str): The path to the file to be read. Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as my_file:
        print(my_file.read(), end="")
