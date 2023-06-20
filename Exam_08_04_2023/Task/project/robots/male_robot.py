from project.robots.base_robot import BaseRobot

class MaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 9)

    @staticmethod
    def robot_type():
        return "Male Robot"

    def eating(self):
        self._weight += 3
