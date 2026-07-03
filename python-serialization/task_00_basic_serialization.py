#!/usr/bin/env python3
"""Module for basic JSON serialization and deserialization."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load data from a JSON file and deserialize it into a Python dictionary."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
