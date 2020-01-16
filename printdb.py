import sqlite3 as sql
import os
dbcon = sql.connect('moncafe.db')
with dbcon:
    c = dbcon.cursor()
    c.execute("""
    SELECT * FROM Coffee_stands
    """)
    print(c.fetchall())
