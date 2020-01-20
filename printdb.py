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
    cursor.execute("""
    SELECT a.date , description, a.quantity , e_name , s_name FROM Activities as a LEFT JOIN (
       Select table1_id, table2_id , e_name , s_name From 
    (
       Select id as table1_id, NULL as table2_id ,name as e_name, NULL as s_name FROM Employees
       UNION ALL
       Select NULL as table1_id, ID as id , NULL as e_name, name as s_name FROM Suppliers 
    )) , Products as p
    ON (table1_id = a.activator_id OR activator_id = table2_id) AND p.id = a.product_id
    ORDER BY a.date
        """)
    print('Activities')
    sup = cursor.fetchall()
    for x in sup:
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
