#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(argv[1], argv[2])
    
    r = requests.get(url, auth=auth)
    print(r.json().get("id"))
