#!/usr/bin/python3
"""Defines a text file-reading function."""
import json


def to_json_string(my_obj):
    """Write a string to a UTF8 text file.
    Args:
        my_obj : The name of the file to write.
    Returns:
        The number of characters written.
    """
    return json.dumps(my_obj)
