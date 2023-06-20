from project.drink import Drink


class Tea(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, 2.50, brand)

    def get_temperature(self):
        return "hot"
