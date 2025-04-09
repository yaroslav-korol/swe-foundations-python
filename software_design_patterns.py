# SOFTWARE (Object-Oriented) DESIGN PATTERNS


# CREATIONAL PATTERNS:

# FACTORY METHOD
#   The Factory Method is a creational design pattern that provides an interface for creating objects
#   in a superclass but allows subclasses to alter the type of objects that will be created.
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass


class Car(Vehicle):
    def getType(self) -> str:
        return "Car"


class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"


class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"


class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass


class CarFactory(VehicleFactory):
    def createVehicle(self):
        return Car()


class BikeFactory(VehicleFactory):
    def createVehicle(self):
        return Bike()


class TruckFactory(VehicleFactory):
    def createVehicle(self):
        return Truck()


# TEST CASE
# carFactory: VehicleFactory = CarFactory()
# truckFactory: VehicleFactory = TruckFactory()
# bikeFactory: VehicleFactory = BikeFactory()

# myCar: Vehicle = carFactory.createVehicle()
# myTruck: Vehicle = truckFactory.createVehicle()
# myBike: Vehicle = bikeFactory.createVehicle()

# print(myCar.getType())  #    "Car"
# print(myTruck.getType())  #  "Truck"
# print(myBike.getType())  #   "Bike"


# SINGLETON
class Singleton:
    _is_instance = None

    # Re-writing built-in __new__ method
    def __new__(cls):
        if not cls._is_instance:
            cls._is_instance = super(Singleton, cls).__new__(cls)
            cls._is_instance._init_value()

        return cls._is_instance

    def _init_value(self):
        self.value = "default"

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value


# TEST CASES
first_instance: Singleton = Singleton()
print(f"Default 'First instance' value is: {first_instance.getValue()}")
first_instance.setValue(value="modified first instance value")
print(f"New 'First instance' value is: {first_instance.getValue()}")

second_instance: Singleton = Singleton()
print(f"Second instance value is: {second_instance.getValue()}")

print(first_instance is second_instance)  # True


# BUILDER


# STRUCTURAL PATTERNS:

# FACADE
# ADAPTER
# DECORATOR


# BEHAVIORAL PATTERNS:

# STRATEGY
# OBSERVER
