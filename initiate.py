import atexit
import os
import sys
import sqlite3 as sql
import DTO
import DAO
import printdb
from repository import _Repository


def enter(entry, repo):
    if entry[0] == 'C':
        repo.coffeeStands.insert(DTO.CoffeeStand(entry[1], entry[2], entry[3]))
    elif entry[0] == 'E':
        repo.employees.insert(DTO.Employee(entry[1], entry[2], entry[3], entry[4]))
    elif entry[0] == 'P':
        repo.products.insert(DTO.Product(entry[1], entry[2], entry[3]))
    elif entry[0] == 'S':
        repo.suppliers.insert(DTO.Supplier(entry[1], entry[2], entry[3]))


def main(text):
    databaseexisted = os.path.isfile('moncafe.db')
    if databaseexisted:
        os.remove('moncafe.db')
    repo = _Repository()
    repo.create_tables()
    f = open(text, 'r')
    for line in f:
        entry = line.replace('\n', '')
        entry = entry.split(', ')
        enter(entry, repo)
    f.close()
    atexit.register(repo._close)


if __name__ == '__main__':
    main(str(sys.argv[1]))
