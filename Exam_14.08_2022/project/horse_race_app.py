from project.horse import Horse
from project.appaloosa import Appaloosa
from project.thoroughbred import Thoroughbred

from project.jockey import Jockey

horses = [
    Appaloosa("Appy"),
    Thoroughbred("Thunder"),
    Thoroughbred("Lightning"),
    Appaloosa("Spotty")
]

jockey = Jockey("John", 25)

race = HorseRace(horses)
race.start_race()

jockey.ride(horses[0])
jockey.ride(horses[2])
