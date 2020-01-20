# REPO
import sqlite3 as sql
import DTO
import DAO


class _Repository:
    def __init__(self):
        self._conn = sql.connect('moncafe.db')
        self.employees = DAO._Employees(self._conn)
        self.suppliers = DAO._Suppliers(self._conn)
        self.coffeeStands = DAO._CoffeeStands(self._conn)
        self.products = DAO._Products(self._conn)
        self.activities = DAO._Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE Products(
         id INTEGER PRIMARY KEY ,
         description TEXT NOT NULL, 
         price REAL NOT NULL,
         quantity INTEGER NOT NULL
         );

        CREATE TABLE Coffee_stands(
        id INTEGER PRIMARY KEY, 
        location TEXT NOT NULL, 
        number_of_employees INTEGER
        );

        CREATE TABLE Activities(
         product_id INTEGER INTEGER REFERENCES Product(id),
         quantity INTEGER NOT NULL, 
         activator_id INTEGER NOT NULL,
         date DATE NOT NULL
         );

         CREATE TABLE Suppliers(
         id INTEGER primary key,
         name TEXT NOT NULL ,
         contact_information TEXT 
         );

        CREATE TABLE Employees(
        id INTEGER primary key,
        name TEXT NOT NULL ,
        salary REAL NOT NULL ,
        coffee_stand INTEGER REFERENCES Coffee_stand(id)
        );
        """)
