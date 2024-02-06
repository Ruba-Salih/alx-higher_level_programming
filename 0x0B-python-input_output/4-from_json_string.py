#!/usr/bin/python3
"""Defines a text file-reading function."""
import json


def from_json_string(my_str):
    """Write a string to a UTF8 text file.
    Args:
        my_str (str): The name of the file to write.
    Returns:
        The number of characters written.
    """
    return json.loads(my_str)
