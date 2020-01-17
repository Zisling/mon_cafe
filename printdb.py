import sqlite3 as sql
import os


def print_table(name, cursor):
    cursor.execute("""
    SELECT * FROM {}
    """.format(name))
    listy = cursor.fetchall()
    print(name)
    if len(listy) > 0:
        for item in listy:
            print(item)


dbcon = sql.connect('moncafe.db')
with dbcon:
    c = dbcon.cursor()
    print_table('Activities', c)
    print_table('Employees', c)
    print_table('Products', c)
    print_table('Suppliers', c)
