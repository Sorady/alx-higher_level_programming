#!/usr/bin/python3
"""7-add_item"""


if __name__ == "__main__":
    import sys
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    finally:
        for i in range(1, len(sys.argv)):
            items.append(sys.argv[i])
        save_to_json_file(items, "add_item.json")
