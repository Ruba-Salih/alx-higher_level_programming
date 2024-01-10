#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    tmpv = 0
    tmpk = ''
    for k, v in a_dictionary.items():
        if v > tmpv:
            tmpv = v
            tmpk = k
    return (tmpk)
