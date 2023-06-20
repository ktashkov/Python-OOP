class HorseRace:
    def __init__(self, horses):
        self.horses = horses

    def start_race(self):
        for horse in self.horses:
            horse.run()

class Horse:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def run(self):
        print(f"{self.name} ({self.breed}) is running!")
