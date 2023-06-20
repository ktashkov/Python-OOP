class Race:
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Name cannot be an empty string!")
        self.name = name
        self.drivers = []
