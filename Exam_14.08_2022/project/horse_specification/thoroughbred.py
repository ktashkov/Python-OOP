from project.horse import Horse

class Thoroughbred(Horse):
    def __init__(self, name):
        super().__init__(name, "Thoroughbred")
