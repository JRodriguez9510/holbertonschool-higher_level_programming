#!/usr/bin/python3
""" Function to write in a file """


def write_file(filename="", text=""):
    """writes string to a file"""
    chars = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        chars += f.write(text)
        f.close()
    return chars
