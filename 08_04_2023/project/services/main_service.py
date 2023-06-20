from project.services.base_service import BaseService

class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self) -> str:
        robots_str = " ".join([robot.name for robot in self._robots]) if self._robots else "none"
        return f"{self._name} Main Service:\nRobots: {robots_str}"
