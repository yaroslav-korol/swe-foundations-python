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
#   The Singleton is a creational design pattern which ensures that at most one instance of a class may exist.


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
# first_instance: Singleton = Singleton()
# print(f"Default 'First instance' value is: {first_instance.getValue()}")
# first_instance.setValue(value="modified first instance value")
# print(f"New 'First instance' value is: {first_instance.getValue()}")

# second_instance: Singleton = Singleton()
# print(f"Second instance value is: {second_instance.getValue()}")

# print(first_instance is second_instance)  # True


# BUILDER


# PROTOTYPE
#   The Prototype is a creational design pattern that allows an object to copy itself.
#   It is particularly useful when the creation of an object is more convenient through
#   copying an existing object than through creation from scratch.


class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass


class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> Shape:
        return Square(self.length)


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> Shape:
        return Rectangle(self.width, self.height)


class Test:
    def clone_shapes(self, shapes: list[Shape]) -> list[Shape]:
        return [shape.clone() for shape in shapes]


# TEST CASES
square = Square(10)  # 10 is the length
another_square = square.clone()  # Clone with length 10
print(square == another_square)  # False

rectangle = Rectangle(10, 20)  # 10 is width, 20 is height
another_rectangle = rectangle.clone()  # Clone with width 10 and height 20
print(rectangle == another_rectangle)  # False

test = Test()
shapes = [square, rectangle, another_square, another_rectangle]
cloned_shapes = test.clone_shapes(shapes)

print(shapes == cloned_shapes)  # False
print(len(shapes) == len(cloned_shapes))  # True
print(shapes[0] == cloned_shapes[0])  # False
print(shapes[0].get_length() == cloned_shapes[0].get_length())  # True


# STRUCTURAL PATTERNS:

# FACADE
# ADAPTER
# DECORATOR


# BEHAVIORAL PATTERNS:

# STRATEGY
# OBSERVER
