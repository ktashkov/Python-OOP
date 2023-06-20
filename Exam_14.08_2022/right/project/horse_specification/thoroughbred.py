from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > 140:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        if self.speed + 3 > 140:
            self.speed = 140
        else:
            self.speed += 3