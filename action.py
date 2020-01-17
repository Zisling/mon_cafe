import sqlite3 as sql
import os


def insert_update(entry, cursor):
    cursor.execute("""
                    INSERT INTO Activities (product_id, quantity,activator_id, date) VALUES (?, ?,?,?)
            """, [entry[0], entry[1], entry[2], entry[3]])
    cursor.execute("""
            UPDATE Products SET quantity=quantity+(?) WHERE id = (?)
            """, [entry[1], entry[0]])


def update(entry, cursor):
    if int(entry[1]) > 0:
        insert_update(entry, cursor)
    elif int(entry[1]) < 0:
        cursor.execute("""
        SELECT quantity FROM Products WHERE id = (?)
        """, [entry[0]])
        product_quantity = int(cursor.fetchone()[0])
        if product_quantity + int(entry[1]) >= 0:
            insert_update(entry, cursor)


dbcon = sql.connect('moncafe.db')
with dbcon:
    c = dbcon.cursor()
    f = open('action.txt', 'r')
    for line in f:
        entry = line.replace('\n', '')
        entry = entry.split(', ')
        update(entry, c)
