#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
