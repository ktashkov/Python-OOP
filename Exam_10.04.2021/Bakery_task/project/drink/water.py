from project.drink import Drink


class Water(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, 1.50, brand)

    def get_temperature(self):
        return "cold"
