#!/usr/bin/python3
"""  script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import requests

    content = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(content.text.__class__))
    print("\t- content: {}".format(content.text))
