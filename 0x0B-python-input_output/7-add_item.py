#!/usr/bin/python3
"""
Module 7-add_item.py that adds all arguments to a Python list, and
then save them to a file.
"""
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    add_file = "add_item.json"

    try:
        new_list = load_from_json_file(add_file)
    except FileNotFoundError:
        new_list = []
    new_list.extend(argv[1:])
    save_to_json_file(new_list, add_file)
