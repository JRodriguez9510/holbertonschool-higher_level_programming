#!/usr/bin/python3
""" function to decode into JSON """
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file with JSON """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
        f.close()
