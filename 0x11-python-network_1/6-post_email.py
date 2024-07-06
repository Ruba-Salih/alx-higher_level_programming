#!/usr/bin/python3
"""A script that takes in a URL and sends a request
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    value = {"email": argv[2]}

    r = requests.post(argv[1], data=value)
    print(r.text)
