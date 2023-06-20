from project.services.base_service import BaseService

class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=15)

    def __str__(self):
        robots = ' '.join(robot.name for robot in self._robots) or 'none'
        return f"{self._name} Secondary Service:\nRobots: {robots}"

    @staticmethod
    def details():
        return "This is a secondary service."

