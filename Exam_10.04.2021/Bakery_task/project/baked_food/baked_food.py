class BakedFood:
    def __init__(self, name: str, portion: float, price: float):
        if not name.strip():
            raise ValueError("Name cannot be empty string or white space!")
        if price <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")
        self.name = name
        self.portion = portion
        self.price = price

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
