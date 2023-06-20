class BaseRobot:
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self._name = name
        self._kind = kind
        self._price = price
        self._weight = weight

        if not name or not name.strip():
            raise ValueError("Robot name cannot be empty!")

        if not kind or not kind.strip():
            raise ValueError("Robot kind cannot be empty!")

        if price <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")

    @staticmethod
    def robot_type():
        return "Generic Robot"

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")
        self._price = value

    @property
    def weight(self):
        return self._weight

    def eating(self):
        self._weight += 1
