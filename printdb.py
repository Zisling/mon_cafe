import sqlite3 as sql
import os


def print_table(name, cursor, key_to_order='id'):
    cursor.execute("""
    SELECT * FROM {}
    ORDER BY {}""".format(name, key_to_order))
    listy = cursor.fetchall()
    print(name)
    if len(listy) > 0:
        for item in listy:
            print(item)


dbcon = sql.connect('moncafe.db')
with dbcon:
    c = dbcon.cursor()
    print_table('Activities', c,'date')
    print_table('Employees', c,'name')
    print_table('Products', c)
    print_table('Suppliers', c)
