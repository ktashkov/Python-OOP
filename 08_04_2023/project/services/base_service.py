class BaseService:
    def __init__(self, name: str, capacity: int):
        if not name.strip():
            raise ValueError("Service name cannot be empty!")
        self._name = name

        if capacity <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self._capacity = capacity

        self._robots = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def robots(self) -> list:
        return self._robots

    def details(self) -> str:
        raise NotImplementedError("details method not implemented in BaseService")

