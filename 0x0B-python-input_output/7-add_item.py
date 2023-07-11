#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""

import sys
from os import path

# Importing needed functions
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

# Check if the file exists
if not path.exists(filename):
    my_list = []
else:
    # Load the existing list from the file
    my_list = load_from_json_file(filename)

# Add the arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the updated list into file
save_to_json_file(my_list, filename)
