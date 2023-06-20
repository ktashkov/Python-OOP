from project.services.main_service import MainService
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.secondary_service import SecondaryService

class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type == "MainService":
            service = MainService(name)
            self.services.append(service)
            return f"{service_type} is successfully added."
        elif service_type == "SecondaryService":
            service = SecondaryService(name)
            self.services.append(service)
            return f"{service_type} is successfully added."
        else:
            raise Exception("Invalid service type!")
    def add_service(self, service_type: str, name: str):
        if service_type not in ["MainService", "SecondaryService"]:
            raise Exception("Invalid service type!")
        for service in self.services:
            if service.name == name:
                return f"{name} already exists."
        service = MainService(name) if service_type == "MainService" else SecondaryService(name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in ["MaleRobot", "FemaleRobot"]:
            raise Exception("Invalid robot type!")
        for robot in self.robots:
            if robot.name == name:
                return f"{name} already exists."
        robot = MaleRobot(name, kind, price) if robot_type == "MaleRobot" else FemaleRobot(name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = None
        for r in self.robots:
            if r.name == robot_name:
                robot = r
                break
        if robot is None:
            raise Exception("No such robot exists!")
        service = None
        for s in self.services:
            if s.name == service_name:
                service = s
                break
        if service is None:
            raise Exception("No such service exists!")
        if type(robot) == MaleRobot and not isinstance(service, MainService):
            return "Unsuitable service."
        if type(robot) == FemaleRobot and not isinstance(service, SecondaryService):
            return "Unsuitable service."
        if not service.add_robot(robot):
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = None
        for s in self.services:
            if s.name == service_name:
                service = s
                break
        if service is None:
            raise Exception("No such service exists!")
        robot = service.remove_robot(robot_name)
        if robot is None:
            raise Exception("No such robot in this service!")
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = None
        for s in self.services:
            if s.name == service_name:
                service = s
                break
        if not service:
            raise Exception("No such service!")
        number_of_robots_fed = service.feed_all_robots()
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = None
        for s in self.services:
            if s.name == service_name:
                service = s
                break
        if not service:
            raise Exception("No such service!")
        total_price = service.calculate_price()
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ""
        for service in self.services:
            result += f"{service.details()}\n"
        return result.strip()