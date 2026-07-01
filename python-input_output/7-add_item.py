#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a JSON file named `add_item.json`.
"""
import sys

save_to_json_file = (
    __import__('5-save_to_json_file').save_to_json_file
)
load_from_json_file = (
    __import__('6-load_from_json_file').load_from_json_file
)

filename = "add_item.json"

# Try to load existing items from the file; if it doesn't exist, start a new list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Append all command line arguments (skipping the script name at index 0)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
