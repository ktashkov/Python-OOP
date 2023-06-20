from project.delicacies.delicacy import Delicacy

class Gingerbread(Delicacy):
    portion = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.portion, price)

    def details(self):
        return f"Gingerbread {self.name}: {self.portion}g - {self.price:.2f}lv."
