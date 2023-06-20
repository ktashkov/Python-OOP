from abc import ABC, abstractmethod


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        if capacity <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def reserve(self, number_of_people: int):
        if number_of_people > self.capacity:
            raise ValueError("Cannot reserve table for more people than its capacity!")
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total = 0
        for food in self.food_orders:
            total += food.price
        for drink in self.drink_orders:
            total += drink.price
        return round(total, 2)

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @abstractmethod
    def free_table_info(self):
        pass
