#!/usr/bin/python3
"""Defines a text file-reading function."""
import json


def save_to_json_file(my_obj, filename):
    """Write a string to a UTF8 text file.
    Args:
        my_obj : The name of the file to write.
        filename : The name of the file to write.
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(my_obj))
