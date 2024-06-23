#!/usr/bin/python3

import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name \
                 FROM cities JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name LIKE BINARY %s \
                 ORDER BY cities.id ASC", (argv[4], ))

    for row in cur.fetchall():
        print(row, sep=',')
