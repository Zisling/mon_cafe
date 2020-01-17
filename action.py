import sqlite3 as sql
import os


def update(entry, cursor):
    if int(entry[1]) > 0:
        cursor.execute("""
                INSERT INTO Activities (product_id, quantity,activator_id, date) VALUES (?, ?,?,?)
        """, [entry[0], entry[1], entry[2], entry[3]])


dbcon = sql.connect('moncafe.db')
with dbcon:
    c = dbcon.cursor()
    f = open('action.txt', 'r')
    for line in f:
        entry = line.replace('\n', '')
        entry = entry.split(', ')
        update(entry, c)
