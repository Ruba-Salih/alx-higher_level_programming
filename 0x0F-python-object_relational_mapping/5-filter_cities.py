#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name \
                 FROM cities JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC", (argv[4], ))

    for row in cur.fetchall():
        print(row, sep=',')
