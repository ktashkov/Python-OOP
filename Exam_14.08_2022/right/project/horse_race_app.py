from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        if [x for x in self.horses if x.name == horse_name]:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type in ("Appaloosa", "Thoroughbred"):
            if horse_type == "Appaloosa":
                horse = Appaloosa(horse_name, horse_speed)
            elif horse_type == "Thoroughbred":
                horse = Thoroughbred(horse_name, horse_speed)

            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        if [x for x in self.jockeys if x.name == jockey_name]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        if [x for x in self.horse_races if x.race_type == race_type]:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for horse in self.horses:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                if jockey.horse:
                    return f"Jockey {jockey_name} already has a horse."
                horse.is_taken = True
                jockey.horse = horse
                return f"Jockey {jockey_name} will ride the horse {horse.name}."

        raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        if not [x for x in self.horse_races if x.race_type == race_type]:
            raise Exception(f"Race {race_type} could not be found!")

        race = [x for x in self.horse_races if x.race_type == race_type][0]

        if not [j for j in self.jockeys if j.name == jockey_name]:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        if not [x for x in self.horse_races if x.race_type == race_type]:
            raise Exception(f"Race {race_type} could not be found!")

        race = [x for x in self.horse_races if x.race_type == race_type][0]

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = race.jockeys[0]

        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed.horse.speed:
                highest_speed = jockey

        return f"The winner of the {race_type} race, with a speed of {highest_speed.horse.speed}km/h is " \
               f"{highest_speed.name}! Winner's horse: {highest_speed.horse.name}."


