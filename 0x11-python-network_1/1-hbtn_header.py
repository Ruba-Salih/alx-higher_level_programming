#!/usr/bin/python3
"""
    A script that takes in a URL and sends a request,
    displays the X-Request-Id variable value
"""


if __name__ == "__main__":
    from sys import argv
    import urllib.request
    url = argv[1]

    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
