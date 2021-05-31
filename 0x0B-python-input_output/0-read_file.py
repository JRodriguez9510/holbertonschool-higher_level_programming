#!/usr/bin/python3
""" Function to read a file """


def read_file(filename=""):
    """ Function to print file content on the stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
