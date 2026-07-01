#!/usr/bin/python3
"""
Adds all command-line arguments to a Python list and saves to a JSON file.
"""
import sys

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_file(items, filename)
