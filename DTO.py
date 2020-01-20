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