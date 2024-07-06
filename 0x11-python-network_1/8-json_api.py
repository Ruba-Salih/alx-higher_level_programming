#!/usr/bin/python3
"""A script that takes in a URL and sends a request
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    payload = {"q": argv[1][0] if len(argv) > 1 else ""}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
