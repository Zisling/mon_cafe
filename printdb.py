import DTO
import DAO
import repository
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


def activities_is_not_empty(cursor):
    cursor.execute("""
    SELECT * FROM Activities
    """)
    return len(cursor.fetchall()) > 0


def employees_report(cursor):
    cursor.execute("""
    SELECT name, salary , location , COALESCE(-1*SUM(a_sum) , 0) FROM (
    SELECT e.id as id, e.name as name , e.salary as salary,c.location as location FROM Employees as e 
    JOIN Coffee_stands as c
    ON e.coffee_stand = c.id) LEFT JOIN (SELECT activator_id , SUM(a.quantity)*price as a_sum FROM Activities as a JOIN Products as p
    ON product_id = id
    GROUP BY activator_id , product_id
    )
    ON activator_id = id
    GROUP BY id
    ORDER BY name 
    """)
    print('Employees report')
    employees = cursor.fetchall()
    for x in employees:
        print(x)


def print_activities(cursor):
    print('Activities')
    cursor.execute("""
    SELECT date , description, a.quantity , e.name , NULL FROM Activities as a ,Products as p , Employees as e
    ON a.activator_id = e.id and p.id = a.product_id
    """)
    employees = cursor.fetchall()
    cursor.execute("""
        SELECT date , description, a.quantity ,NULL , s.name FROM Activities as a ,Products as p , Suppliers as s
        ON a.activator_id = s.id and p.id = a.product_id
        """)
    sup = cursor.fetchall()
    to_print = sup+employees
    to_print.sort()
    for x in to_print:
        print(x)


# dbcon = sql.connect('moncafe.db')
repo = repository._Repository()
dbcon = repo.conn
with dbcon:
    c = dbcon.cursor()
    print_table('Activities', c, 'date')
    print_table('Employees', c, 'name')
    print_table('Products', c)
    print_table('Suppliers', c)
    employees_report(c)
    if activities_is_not_empty(c):
        print_activities(c)
