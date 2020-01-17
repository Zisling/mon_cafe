import atexit
import os
import sqlite3 as sql


# DTO
class Employee:
    def __init__(self, e_id, name, salary, coffee_stand):
        self.id = e_id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class Supplier:
    def __init__(self, s_id, name, contact_information):
        self.id = s_id
        self.name = name
        self.contact_information = contact_information


class Product:
    def __init__(self, p_id, description, price, quantity=0):
        self.id = p_id
        self.description = description
        self.price = price
        self.quantity = quantity


class CoffeeStand:
    def __init__(self, c_id, location, number_of_employees):
        self.id = c_id
        self.location = location
        self.number_of_employees = number_of_employees


class Activities:
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date


# --------------------------------------------------------------------------------------
# DAO
class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
        INSERT INTO Employees (id, name,salary,coffee_stand) VALUES (?, ?,?,?)
        """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
        SELECT * FROM Employees WHERE id = ?
        """, [employee_id])

        return c.fetchone()


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
        INSERT INTO Suppliers (id, name,contact_information) VALUES (?, ?,?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
        SELECT id, name FROM Suppliers WHERE id = ?
        """, [supplier_id])

        return c.fetchone()


class _CoffeeStands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, stand):
        self._conn.execute("""
        INSERT INTO Coffee_stands (id, location,number_of_employees) VALUES (?, ?,?)
        """, [stand.id, stand.location, stand.number_of_employees])

    def find(self, stand_id):
        c = self._conn.cursor()
        c.execute("""
        SELECT * FROM Coffee_stands WHERE id = ?
        """, [stand_id])

        return c.fetchone()


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
        INSERT INTO Products (id, description,price, quantity) VALUES (?, ?,?,?)
        """, [product.id, product.description, product.price, product.quantity])

    def find(self, product_id):
        c = self._conn.cursor()
        c.execute("""
        SELECT id, name FROM Products WHERE id = ?
        """, [product_id])

        return Product(*c.fetchone())


class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, act):
        self._conn.execute("""
        INSERT INTO Activities (product_id, quantity,activator_id, date) VALUES (?, ?,?,?)
        """, [act.product_id, act.quantity, act.activator_id, act.date])


# --------------------------------------------------------------------------------------
# REPO
class _Repository:
    def __init__(self):
        self._conn = sql.connect('moncafe.db')
        self.employees = _Employees(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.coffeeStands = _CoffeeStands(self._conn)
        self.products = _Products(self._conn)
        self.activities = _Activities(self._conn)

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


def enter(entry, repo):
    if entry[0] == 'C':
        repo.coffeeStands.insert(CoffeeStand(entry[1], entry[2], entry[3]))
    elif entry[0] == 'E':
        repo.employees.insert(Employee(entry[1], entry[2], entry[3], entry[4]))
    elif entry[0] == 'P':
        repo.products.insert(Product(entry[1], entry[2], entry[3]))
    elif entry[0] == 'S':
        repo.suppliers.insert(Supplier(entry[1], entry[2], entry[3]))


def main():
    databaseexisted = os.path.isfile('moncafe.db')
    if databaseexisted:
        os.remove('moncafe.db')
    repo = _Repository()
    repo.create_tables()
    f = open('config.txt', 'r')
    for line in f:
        entry = line.replace('\n', '')
        entry = entry.split(', ')
        enter(entry, repo)
    f.close()
    atexit.register(repo._close)


if __name__ == '__main__':
    main()
