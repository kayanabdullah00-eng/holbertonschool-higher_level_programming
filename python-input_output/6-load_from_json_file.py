#!/usr/bin/python3
"""
This module contains a function that deserializes a JSON file to an object.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        any: The corresponding Python object structure.
    """
    with open(filename, mode="r", encoding="utf-8") as my_file:
        return json.load(my_file)
