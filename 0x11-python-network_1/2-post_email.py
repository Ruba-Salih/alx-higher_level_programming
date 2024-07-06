#!/usr/bin/python3
""" script that takes in a URL and an email """


if __name__ == "__main__":
    from sys import argv
    import urllib.parse
    import urllib.request

    url = argv[1]
    variable = {"email": argv[2]}
    data = urllib.parse.urlencode(variable).encode("utf-8")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
