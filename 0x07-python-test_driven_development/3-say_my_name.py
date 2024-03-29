#!/usr/bin/python3
"""Defines say_my_name function."""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: str
        last_name: str
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not (isinstance(first_name, str)):
        raise TypeError('first_name must be a string')
    if not (isinstance(last_name, str)):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
