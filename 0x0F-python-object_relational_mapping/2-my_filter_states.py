#!/usr/bin/python3
""" Script that lists all states with a name starting with N (upper N) from the database """

import MySQLdb
from sys import argv

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]
    sql  = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cur = db.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        if row[1] == name:
            print(row)
    cur.close()
    db.close()
