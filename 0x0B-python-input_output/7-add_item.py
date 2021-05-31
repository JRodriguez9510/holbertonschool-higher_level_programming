#!/usr/bin/python3
""" function to add args written into a JSON file """
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def my_function():
    """ adds the args to a file """
    try:
        my_file = load_from_json_file("add_item.json")
    except:
        my_file = []

    for i in range(1, len(argv)):
        my_file.append(argv[i])
    save_to_json_file(my_file, "add_item.json")


if __name__ == "__main__":
    my_function()
