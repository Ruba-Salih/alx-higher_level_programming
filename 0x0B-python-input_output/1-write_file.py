#!/usr/bin/python3
"""Defines a text file-reading function."""


def write_file(filename="", text=""):
    """read_file function."""

    with open(filename, 'w', encoding='UTF-8') as f:
        print(f.write(text))
