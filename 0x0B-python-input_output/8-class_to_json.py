#!/usr/bin/python3
""" Function to convert objects into dicts """


def class_to_json(obj):
    """ return a dictionary of the object """
    return obj.__dict__
