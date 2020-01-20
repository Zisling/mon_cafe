import DTO
import sqlite3 as sql


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

        return DTO.Product(*c.fetchone())


class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, act):
        self._conn.execute("""
        INSERT INTO Activities (product_id, quantity,activator_id, date) VALUES (?, ?,?,?)
        """, [act.product_id, act.quantity, act.activator_id, act.date])

# --------------------------------------------------------------------------------------
