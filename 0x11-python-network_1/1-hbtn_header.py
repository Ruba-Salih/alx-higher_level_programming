#!/usr/bin/python3
"""
    A script that takes in a URL and sends a request,
    displays the X-Request-Id value.
"""


if __name__ == "__main__":
    import sys
    import urllib.request as request

    url = sys.argv[1]
    request = request.Request(url)
    with request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
