from project.delicacies.delicacy import Delicacy

class Stolen(Delicacy):
    portion = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, self.portion, price)

    def details(self):
        return f"Stolen {self.name}: {self.portion}g - {self.price:.2f}lv."
