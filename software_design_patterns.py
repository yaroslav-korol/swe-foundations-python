# SOFTWARE (Object-Oriented) DESIGN PATTERNS

from abc import ABC, abstractmethod
from enum import Enum

# CREATIONAL PATTERNS:

# FACTORY METHOD
#   The Factory Method is a creational design pattern that provides an interface for creating objects
#   in a superclass but allows subclasses to alter the type of objects that will be created.


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
#   The Builder is a creational design pattern that allows the construction of complex objects step by step.
#   It is useful when an object has several components and it's desirable to construct the object with various configurations.


class Starter(Enum):
    SALAD = 1
    SOUP = 2
    BRUSCHETTA = 3
    VEGGIE_STICKS = 4
    CHICKEN_WINGS = 5


class MainCourse(Enum):
    GRILLED_CHICKEN = 1
    PASTA = 2
    VEGGIE_STIR_FRY = 3
    FISH = 4
    PIZZA = 5


class Dessert(Enum):
    FRUIT_SALAD = 1
    ICE_CREAM = 2
    CHOCOLATE_CAKE = 3
    VEGAN_PUDDING = 4
    CHEESECAKE = 5


class Drink(Enum):
    WATER = 1
    VEGAN_SHAKE = 2
    SODA = 3
    FRUIT_JUICE = 4


# Product type
class Meal:
    def __init__(self):
        self._starter = None
        self._main = None
        self._dessert = None
        self._drink = None

    @property
    def starter(self) -> str:
        return self._starter

    @property
    def main_course(self) -> str:
        return self._main_course

    @property
    def desert(self) -> str:
        return self._desert

    @property
    def drink(self) -> str:
        return self._drink

    @starter.setter
    def starter(self, starter: str) -> None:
        self._starter = starter

    @main_course.setter
    def main_course(self, main_course: str) -> None:
        self._main_course = main_course

    @desert.setter
    def desert(self, desert: str) -> None:
        self._desert = desert

    @drink.setter
    def drink(self, drink: str) -> None:
        self._drink = drink


# Builder Interface
class BuilderInterface(ABC):
    @abstractmethod
    def add_starter():
        pass

    @abstractmethod
    def add_main_course():
        pass

    @abstractmethod
    def add_desert():
        pass

    @abstractmethod
    def add_drink():
        pass


# Concrete Builder
class DinnerBuilder(BuilderInterface):
    def __init__(self):
        self._meal: Meal = Meal()

    def add_starter(self, starter: str) -> None:
        self._meal.starter = starter

    def add_main_course(self, main_course: str) -> None:
        self._meal.main_course = main_course

    def add_desert(self, desert: str) -> None:
        self._meal.desert = desert

    def add_drink(self, drink: str) -> None:
        self._meal.drink = drink

    def build(self) -> Meal:
        return self._meal


# Director
class Director:
    def construct_healthy_dinner(self, builder: BuilderInterface) -> None:
        builder.add_starter(Starter.SALAD)
        builder.add_main_course(MainCourse.FISH)
        builder.add_desert(Dessert.FRUIT_SALAD)
        builder.add_drink(Drink.WATER)

    def construct_other_meal(self, builder: BuilderInterface) -> None:
        pass


# TEST CASES
# test_builder: BuilderInterface = DinnerBuilder()
# test_director: Director = Director()

# test_director.construct_healthy_dinner(test_builder)
# my_healthy_meal: Meal = test_builder.build()

# print("Meal constructed")
# print(f"Starter: {my_healthy_meal.starter}")
# print(f"Main: {my_healthy_meal.main_course}")
# print(f"Desert: {my_healthy_meal.desert}")
# print(f"Drink: {my_healthy_meal.drink}")


# PROTOTYPE
#   The Prototype is a creational design pattern that allows an object to copy itself.
#   iIt is particularly useful when the creation of an object is more convenient through
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
# square = Square(10)  # 10 is the length
# another_square = square.clone()  # Clone with length 10
# print(square == another_square)  # False

# rectangle = Rectangle(10, 20)  # 10 is width, 20 is height
# another_rectangle = rectangle.clone()  # Clone with width 10 and height 20
# print(rectangle == another_rectangle)  # False

# test = Test()
# shapes = [square, rectangle, another_square, another_rectangle]
# cloned_shapes = test.clone_shapes(shapes)

# print(shapes == cloned_shapes)  # False
# print(len(shapes) == len(cloned_shapes))  # True
# print(shapes[0] == cloned_shapes[0])  # False
# print(shapes[0].get_length() == cloned_shapes[0].get_length())  # True


# STRUCTURAL PATTERNS:

# ADAPTER
#   The Adapter is a structural design pattern that allows incompatible interfaces to work together.
#   It wraps an existing class with a new interface so that it becomes compatible with the client's interface.


# Adaptee - Existing (legacy) class
class XmlLogger:
    def log(self, message: str) -> str:
        # Do some work - construct xml log message ...
        xml_message: str = f"Converted xml message: {message}"
        return xml_message


# Target Interface v.1
class JsonLogger(ABC):
    @abstractmethod
    def log_message(self, message: str) -> str:
        pass


# Target Interface v.2 using Protocol (for decoupling)
# from typing import Protocol
# class JsonLogger(Protocol):
#     def log_message(self, message: str) -> str:
#         ...


# Adapter
class LoggerAdapter(JsonLogger):
    def __init__(self, xml_logger: XmlLogger) -> None:
        self._xml_logger = xml_logger

    def log_message(self, message: str) -> str:
        return self._xml_logger.log(message)


# TEST CASES

# Client
# legacy_logger: XmlLogger = XmlLogger()
# new_logger = LoggerAdapter(legacy_logger)

# default_message: str = "Some test message"
# print(new_logger.log_message(default_message))


# DECORATOR
#   The Decorator is a structural design pattern that allows behavior to be added to individual objects,
#   either statically or dynamically, without affecting the behavior of other objects from the same class.


# Component Interface
class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


# Concrete Component
class BaseCoffee(Beverage):
    def __init__(self, base_price: float) -> None:
        self._base_price = base_price

    def get_description(self) -> str:
        return "It's a base coffee"

    def get_cost(self) -> float:
        return self._base_price


# Abstract Decorator
class BeverageDecorator(Beverage, ABC):
    def __init__(self, base_coffee: BaseCoffee):
        self._base_coffee = base_coffee

    def get_description(self) -> str:
        return self._base_coffee.get_description()

    def get_cost(self) -> float:
        return self._base_coffee.get_cost()


# Concrete Decorators
class AddMilkDecorator(BeverageDecorator):
    def __init__(self, base_coffee: BaseCoffee) -> None:
        super().__init__(base_coffee)

    def get_description(self) -> str:
        return super().get_description() + " with Milk"

    def get_cost(self) -> float:
        return super().get_cost() + 0.5


class AddEspressoDecorator(BeverageDecorator):
    def __init__(self, base_coffee: BaseCoffee):
        super().__init__(base_coffee)

    def get_description(self) -> str:
        return super().get_description() + " with additional Espresso"

    def get_cost(self) -> float:
        return super().get_cost() + 0.7


# TEST CASES

# Option 1
# base_coffee: Beverage = BaseCoffee(base_price=1.1)
# coffee_with_milk: Beverage = AddMilkDecorator(base_coffee=base_coffee)
# double_espresso_with_milk: Beverage = AddEspressoDecorator(coffee_with_milk)
# print(f"Final Beverage: {double_espresso_with_milk.get_description()}")
# print(f"Final price: {double_espresso_with_milk.get_cost(): .2f}")

# Option 2
# final_drink: Beverage = AddMilkDecorator(AddEspressoDecorator(BaseCoffee(base_price=1.1)))
# print(f"Final Beverage: {final_drink.get_description()}")
# print(f"Final price: {final_drink.get_cost(): .2f}")


# FACADE
#   The Facade is a structural design pattern that provides a simplified interface to a complex system of classes,
#   library, or framework. It wraps the complexities of the system and provides a simple interface to clients.


class Brightness(Enum):
    UNKNOWN = "UNKNOWN"
    BRIGHT = "BRIGHT"
    DIM = "DIM"


class Service(Enum):
    UNKNOWN = "UNKNOWN"
    HULU = "HULU"
    NETFLIX = "NETFLIX"
    HBO = "HBO"


# Subsystem classes
class SmartLight:
    def __init__(self) -> None:
        self._brightness: Brightness = Brightness.UNKNOWN

    def get_brightness(self) -> Brightness:
        return self._brightness

    def set_brightness(self, brightness: Brightness) -> None:
        self._brightness = brightness


class SmartThermostat:
    def __init__(self) -> None:
        self._temperature: int = 19

    def get_temperature(self) -> int:
        return self._temperature

    def set_temperature(self, temperature: int) -> None:
        self._temperature = temperature


class SmartTV:
    def __init__(self) -> None:
        self._stream_service: Service = Service.UNKNOWN

    def get_stream_service(self) -> Service:
        return self._stream_service

    def set_stream_service(self, stream_service: Service) -> None:
        self._stream_service = stream_service


# Facade Class
class SmartHome:
    def __init__(self):
        self.__lights: SmartLight = SmartLight()
        self.__thermostat: SmartThermostat = SmartThermostat()
        self.__tv = SmartTV()

    def set_movie_mode(self) -> str:
        self.__lights.set_brightness(Brightness.DIM)
        self.__thermostat.set_temperature(21)
        self.__tv.set_stream_service(Service.NETFLIX)
        return "Movie mode is on"

    def set_another_mode(self):
        pass


# Client simulation
my_home: SmartHome = SmartHome()
print(my_home.set_movie_mode())


# BEHAVIORAL PATTERNS:

# STRATEGY
# OBSERVER
