#!/usr/bin/python3
"""A script that takes in a URL and sends a request
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
