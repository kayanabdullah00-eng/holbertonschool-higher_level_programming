#!/usr/bin/python3
"""
This module contains a function that converts a JSON string to an object.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string representation to decode.

    Returns:
        any: The corresponding Python object data structure.
    """
    return json.loads(my_str)
