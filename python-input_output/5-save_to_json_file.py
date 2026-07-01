#!/usr/bin/python3
"""
This module contains a function that serializes an object to a file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The Python object data structure to serialize.
        filename (str): The name of the text file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
