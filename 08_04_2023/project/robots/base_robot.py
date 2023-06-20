class BaseRobot:
    def __init__(self, name: str, kind: str, price: float, weight: int):
        if not name or not name.strip():
            raise ValueError("Robot name cannot be empty!")
        if not kind or not kind.strip():
            raise ValueError("Robot kind cannot be empty!")
        if price <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")
        self._name = name
        self._kind = kind
        self._price = price
        self._weight = weight

    @property
    def name(self) -> str:
        return self._name

    @property
    def kind(self) -> str:
        return self._kind

    @property
    def price(self) -> float:
        return self._price

    @property
    def weight(self) -> int:
        return self._weight

    @staticmethod
    def eating():
        raise NotImplementedError("eating() method is not implemented in the base class")
