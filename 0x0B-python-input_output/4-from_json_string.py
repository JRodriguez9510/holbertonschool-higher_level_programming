#!/usr/bin/python3
""" function to get the decode of a JSON  """
import json


def from_json_string(my_str):
    """ decodes a JSON str """
    x = json.loads(my_str)
    return x
