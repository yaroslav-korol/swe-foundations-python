# SOFTWARE (Object-Oriented) DESIGN PATTERNS


# CREATIONAL PATTERNS:

# Factory Method
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
carFactory: VehicleFactory = CarFactory()
truckFactory: VehicleFactory = TruckFactory()
bikeFactory: VehicleFactory = BikeFactory()

myCar: Vehicle = carFactory.createVehicle()
myTruck: Vehicle = truckFactory.createVehicle()
myBike: Vehicle = bikeFactory.createVehicle()

print(myCar.getType())  #    "Car"
print(myTruck.getType())  #  "Truck"
print(myBike.getType())  #   "Bike"


# Builder

# Singleton


# STRUCTURAL PATTERNS:

# Facade
# Adapter
# Decorator


# BEHAVIORAL PATTERNS:
# Strategy
# Observer
