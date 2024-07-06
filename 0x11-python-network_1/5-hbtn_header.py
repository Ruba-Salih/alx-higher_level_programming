#!/usr/bin/python3
"""A script that takes in a URL and sends a request
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
