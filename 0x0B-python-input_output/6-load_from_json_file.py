#!/usr/bin/python3
"""Defines a text file-reading function."""
import json


def load_from_json_file(filename):
    """Write a string to a UTF8 text file.
    Args:
        filename : The name of the file to write.
    """
    with open(filename) as f:
        return (json.loads(f))
