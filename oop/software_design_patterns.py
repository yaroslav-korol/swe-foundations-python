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
        self._main_course = None
        self._dessert = None
        self._drink = None

    @property
    def starter(self) -> Starter:
        return self._starter

    @property
    def main_course(self) -> MainCourse:
        return self._main_course

    @property
    def dessert(self) -> Dessert:
        return self._dessert

    @property
    def drink(self) -> Drink:
        return self._drink

    @starter.setter
    def starter(self, starter: Starter) -> None:
        self._starter = starter

    @main_course.setter
    def main_course(self, main_course: MainCourse) -> None:
        self._main_course = main_course

    @dessert.setter
    def dessert(self, dessert: Dessert) -> None:
        self._dessert = dessert

    @drink.setter
    def drink(self, drink: str) -> None:
        self._drink = drink


# Builder Interface
class BuilderInterface(ABC):
    @abstractmethod
    def add_starter(self, starter: Starter) -> None:
        pass

    @abstractmethod
    def add_main_course(self, main_course: MainCourse) -> None:
        pass

    @abstractmethod
    def add_dessert(self, dessert: Dessert) -> None:
        pass

    @abstractmethod
    def add_drink(self, drink: Drink) -> None:
        pass


# Concrete Builder
class DinnerBuilder(BuilderInterface):
    def __init__(self):
        self._meal: Meal = Meal()

    def add_starter(self, starter: Starter) -> None:
        self._meal.starter = starter

    def add_main_course(self, main_course: MainCourse) -> None:
        self._meal.main_course = main_course

    def add_dessert(self, dessert: Dessert) -> None:
        self._meal.dessert = dessert

    def add_drink(self, drink: Drink) -> None:
        self._meal.drink = drink

    def build(self) -> Meal:
        return self._meal


# Director
class Director:
    def construct_healthy_dinner(self, builder: BuilderInterface) -> None:
        builder.add_starter(Starter.SALAD)
        builder.add_main_course(MainCourse.FISH)
        builder.add_dessert(Dessert.FRUIT_SALAD)
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
# print(f"dessert: {my_healthy_meal.dessert}")
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
# my_home: SmartHome = SmartHome()
# print(my_home.set_movie_mode())


# BEHAVIORAL PATTERNS:

# STRATEGY
#   The Strategy is a behavioral design pattern that enables selecting an algorithm's runtime behavior.
#   It defines a family of algorithms, encapsulates each one, and makes them interchangeable.


# Strategy Interfaces
class Lockable(ABC):
    @abstractmethod
    def lock(self):
        pass

    @abstractmethod
    def unlock(self):
        pass


class Openable(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


# Context (Navigator Class)
class Door(ABC):
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self._lock_behavior = None
        self._open_behavior = None

    def set_lock_behavior(self, lock_behavior: Lockable):
        self._lock_behavior = lock_behavior

    def set_open_behavior(self, open_behavior: Openable):
        self._open_behavior = open_behavior

    def perform_lock(self):
        self._lock_behavior.lock()

    def perform_unlock(self):
        self._lock_behavior.unlock()

    def perform_open(self):
        self._open_behavior.open()

    def perform_close(self):
        self._open_behavior.close()

    def get_dimensions(self):
        return self.dimensions


# Concrete Strategies
class PasswordLock(Lockable):
    def lock(self):
        print("Door locked with password")

    def unlock(self):
        print("Door unlocked with password")


class KeyLock(Lockable):
    def lock(self):
        print("Door locked with a key")

    def unlock(self):
        print("Door unlocked with a key")


class SlidingOpening(Openable):
    def open(self):
        print("The door opened with a sliding mechanism")

    def close(self):
        print("The door closed with a sliding mechanism")


class StandardOpening(Openable):
    def open(self):
        print("The door opened with a standard mechanism")

    def close(self):
        print("The door closed with a standard mechanism")


class StandardDoorWithKeyLock(Door):
    pass


class SlidingDoor(Door):
    pass


# Client simulation

# Test 1

# # Initialize door
# external_door: StandardDoorWithKeyLock = StandardDoorWithKeyLock(dimensions=12)

# # Set behaviors
# external_door.set_lock_behavior(KeyLock())
# external_door.set_open_behavior(StandardOpening())

# # Invoke behaviors
# external_door.perform_lock()
# external_door.perform_unlock()
# external_door.perform_open()
# external_door.perform_close()

# # Change lock mechanism
# external_door.set_lock_behavior(PasswordLock())
# external_door.perform_lock()
# external_door.perform_unlock()


print("\n")


# Test 2

# sliding_door: SlidingDoor = SlidingDoor(dimensions=24)

# sliding_door.set_lock_behavior(PasswordLock())
# sliding_door.set_open_behavior(SlidingOpening())

# sliding_door.perform_lock()
# sliding_door.perform_unlock()

# sliding_door.perform_open()
# sliding_door.perform_close()


# OBSERVER
#   The Observer is a behavioral design pattern that allows objects to be notified about changes in another object's state.

#   There are technically two implementations of the observer pattern we can implement: push model and a pull model.
#       - The push model directly updates all the observers after a change in value of the subjects.
#       - In the pull model, the publisher only informs the subscribers that there has been a change and the subscribers
#         are responsible for fetching the books themselves if they are interested.

#   In my example below, I use the push model.


# Observer (Subscriber) Interface
class Customer(ABC):
    @abstractmethod
    def update(self, stock_quantity: int):
        pass


# Subject (Publisher) Interface
class Store(ABC):
    @abstractmethod
    def add_customer(self, customer: Customer):
        pass

    @abstractmethod
    def remove_customer(self, customer: Customer):
        pass

    @abstractmethod
    def notify_customers(self):
        pass

    @abstractmethod
    def update_quantity(self, quantity: int):
        pass


# Concrete Observer (Subscriber)
class BookStoreCustomer(Customer):
    def __init__(self, store: Store):
        self._store = store
        self._store.add_customer(self)
        self._stock_quantity: int | None = None

    def update(self, stock_quantity: int) -> None:
        self._stock_quantity = stock_quantity
        if self._stock_quantity > 0:
            print(f"Subscribed book stock updated to: {self._stock_quantity}")


# Concrete Subjects
class BookStore(Store):
    def __init__(self, quantity: int):
        self._customers: list[Customer] = []
        self._stock_quantity = quantity

    def add_customer(self, customer: Customer) -> None:
        self._customers.append(customer)

    def remove_customer(self, customer: Customer) -> None:
        self._customers.remove(customer)

    def notify_customers(self) -> None:
        for customer in self._customers:
            customer.update(self._stock_quantity)

    def update_quantity(self, quantity: int) -> None:
        self._stock_quantity = quantity
        self.notify_customers()


# Client simulation

# # Test 1
# book_store: BookStore = BookStore(5)
# customer_1: BookStoreCustomer = BookStoreCustomer(store=book_store)
# customer_2: BookStoreCustomer = BookStoreCustomer(store=book_store)


# # Initially, the book is out of stock
# print("Setting stock to 0.")
# book_store.update_quantity(0)

# # The book comes back in stock
# print("Setting stock to 5.")
# book_store.update_quantity(5)

# # Remove customer_1 from the notification list
# book_store.remove_customer(customer_1)

# # Simulate the situation where the stock changes again
# print("\nSetting stock to 2.")
# book_store.update_quantity(2)


# STATE
#   The State is a behavioral design pattern that allows an object to alter its behavior when its internal state changes.
#   This pattern is often used to encapsulate the state-related behavior within state-specific classes,
#   avoiding large conditional statements in the object's methods.


# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def change_state(self, traffic_light) -> None:
        pass


# Context
class TrafficLight:
    def __init__(self):
        self._prev_state: TrafficLightState = None
        self._current_state: TrafficLightState = RedState()

    def get_prev_state(self) -> TrafficLightState:
        return self._prev_state

    def set_state(self, state: TrafficLightState) -> None:
        self._prev_state = self._current_state
        self._current_state = state

    def change(self) -> None:
        self._current_state.change_state(self)


# Concrete State Classes
class GreenState(TrafficLightState):
    def change_state(self, traffic_light: TrafficLight) -> None:
        print("Green - go!")
        traffic_light.set_state(YellowState())


class YellowState(TrafficLightState):
    def change_state(self, traffic_light: TrafficLight) -> None:
        if isinstance(traffic_light.get_prev_state(), GreenState):
            print("Yellow (from Green to Red) - caution!")
            traffic_light.set_state(RedState())
        else:
            print("Yellow (from Red to Green) - caution!")
            traffic_light.set_state(GreenState())


class RedState(TrafficLightState):
    def change_state(self, traffic_light: TrafficLight) -> None:
        print("Red - Stop!")
        traffic_light.set_state(YellowState())


# Client
light_system: TrafficLight = TrafficLight()

light_system.change()  # Green - Go!
light_system.change()  # Yellow - Prepare to Stop!
light_system.change()  # Red - Stop!
light_system.change()  # Yellow - Prepare to Go!
