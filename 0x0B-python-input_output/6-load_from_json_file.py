#!/usr/bin/python3
""" function to get an object from a JSON  """
import json


def load_from_json_file(filename):
    """ writes an object form JSON file """
    with open(filename, encoding="utf-8") as f:
        new_obj = json.loads(f.read())
        return new_obj
