from project.robots.base_robot import BaseRobot
from project.services.base_services import BaseServices
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService

class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in ("MainService", "SecondaryService"):
            raise Exception("Invalid service type!")
        for service in self.services:
            if service.name == name:
                return f"{service_type} is already added."
        service = MainService(name) if service_type == "MainService" else SecondaryService(name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in ("MaleRobot", "FemaleRobot"):
            raise Exception("Invalid robot type!")
        for robot in self.robots:
            if robot.name == name:
                return f"{robot_type} is already added."
        robot = MaleRobot(name, kind, price) if robot_type == "MaleRobot" else FemaleRobot(name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next((robot for robot in self.robots if robot.name == robot_name), None)
        service = next((service for service in self.services if service.name == service_name), None)
        if robot.kind == "Female" and type(service).__name__ != "SecondaryService":
            return "Unsuitable service."
        elif robot.kind == "Male" and type(service).__name__ != "MainService":
            return "Unsuitable service."
        if not service.can_add_robot():
            raise Exception("Not enough capacity for this robot!")
        service.add_robot(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        robot = next((robot for robot in self.services[self.services.index(service_name)].robots if robot.name == robot_name), None)
        if robot is None:
            raise Exception("No such robot in this service!")
        self.services[self.services.index(service_name)].remove_robot(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next((service for service in self.services if service.name == service_name), None)
        if service is None:
            raise Exception("No such service!")
        count = 0
        for robot in service.robots:
            if robot.eating():
                count += 1
        return f"Robots fed: {count}."

    def service_price(self, service_name: str):
        service = next((service for service in self.services if service.name == service_name), None)
        if service is None:
            raise Exception("No such service!")
        total_price = sum(robot.price for robot in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ""
        for service in self.services:
            result += f"{service.name} {type(service).__name__}:\n"
            robots = " ".join(robot.name for robot in service.robots)
            result += f"Robots: {robots}\n"
        return result
