class Horse:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def run(self):
        print(f"{self.name} ({self.breed}) is running!")
