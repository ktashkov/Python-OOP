from typing import List
from project.baked_food import BakedFood
from project.drink import Drink
from project.table import Table

class Bakery:
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        baked_food = None
        if food_type == "Bread":
            baked_food = Bread(name, price)
        elif food_type == "Cake":
            baked_food = Cake(name, price)
        else:
            raise ValueError(f"Invalid food type: {food_type}")
        if baked_food in self.food_menu:
            raise Exception(f"{food_type} {name} is already in the menu!")
        self.food_menu.append(baked_food)
        return f"Added {baked_food.name} ({baked_food.__class__.__name__}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        drink = None
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            drink = Water(name, portion, brand)
        else:
            raise ValueError(f"Invalid drink type: {drink_type}")
        if drink in self.drinks_menu:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        self.drinks_menu.append(drink)
        return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = None
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        else:
            raise ValueError(f"Invalid table type: {table_type}")
        if table in self.tables_repository:
            raise Exception(f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        table = self._find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"
        ordered_foods = []
        not_available_foods = []
        for food_name in food_names:
            baked_food = next((food for food in self.food_menu if food.name == food_name), None)
            if baked_food:
                ordered_foods.append(baked_food)
            else:
                not_available_foods.append(food_name)
        order_str = f"Table {table_number} ordered:\n"
        for food in ordered_foods:
            order_str += f" - {food.name}: {food.portion}g - {food.price}lv\n"
            table.orders.append(food)
        if not_available_foods:
            order_str += f"{self.name} does not have in the menu:\n"
            order_str += "\n".join(not_available_foods)
        return order
