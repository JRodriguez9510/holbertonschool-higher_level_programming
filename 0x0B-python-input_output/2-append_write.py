#!/usr/bin/python3
""" Function to read a file """


def append_write(filename="", text=""):
    """ writes at the end of a file """
    chars = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        chars += f.write(text)
        f.close()
        return chars
