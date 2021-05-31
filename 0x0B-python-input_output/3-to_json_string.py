#!/usr/bin/python3
""" function to get the JSON representation of an object """
import json


def to_json_string(my_obj):
    """ return the JSON representation of an object """
    return json.dumps(my_obj)
