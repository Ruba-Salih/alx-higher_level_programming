#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """read_file function."""


    with open(filename, encoding='UTF-8') as f:
        print(f.readlines(), end= '')
