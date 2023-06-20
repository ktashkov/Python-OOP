class Jockey:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ride(self, horse):
        print(f"{self.name} is riding {horse.name} ({horse.breed})!")
        horse.run()
