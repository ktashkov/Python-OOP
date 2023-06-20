class BaseService:
    def __init__(self, name: str, capacity: int):
        self._name = name
        self._capacity = capacity
        self._robots = []

        if not name.strip():
            raise ValueError("Service name cannot be empty!")
        if capacity <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")

    @staticmethod
    def details():
        raise NotImplementedError("Subclass must implement abstract method")

