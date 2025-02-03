import random
from abc import ABC, abstractmethod
from datetime import datetime as dt

# 1. Version 1

# class Car:
#     pass


# def main():
#     car = desirable_car()
#     print(f"I want to get {car.brand} car, model {car.model} in a {car.color} color")
#     car.color = 'black'
#     print(f"New color of {car.brand} is {car.color} now")


# def desirable_car():
#     car = Car()
#     car.brand = 'Tesla'
#     car.model = 'S'
#     car.color = 'silver'

#     return car


# if __name__ == "__main__":
#     main()
#     print(Car)
#     print(Car())
#     print(desirable_car)
#     print(desirable_car())


# # 2. Version 2


# class Car:
#     colors: list[str] = ["black", "silver", "white", "red"]

#     def __init__(self, brand, color, model=None):
#         if not brand:
#             raise ValueError("Missing brand")

#         if color not in Car.colors:
#             raise ValueError("Invalid color option")

#         self.brand = brand
#         self.color = color
#         self.model = model

#     def __str__(self):
#         return f"Brand: {self.brand}. Color: {self.color}. Model: {self.model}"


# def main():
#     car = desirable_car()
#     print(f"I want to get {car.brand} car, model {car.model} in a {car.color} color")
#     car.color = "black"
#     print(f"New color of {car.brand} is {car.color} now")

#     car.new_variable = "some value"
#     print(car)
#     print(car.new_variable)


# def desirable_car():
#     return Car("Tesla", "silver", "S")


# if __name__ == "__main__":
#     main()
#     print(Car)
#     print(Car("Tesla", "silver"))
#     print(Car("Reno", "red"))
#     print(desirable_car)
#     print(desirable_car())


# 3. GETters. SETters and DELETErs


class Car:
    colors: list[str] = ["black", "silver", "white", "red"]

    def __init__(self, car_brand, car_color, model=None):
        self.brand = car_brand
        self.color = car_color
        self.model = model

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, car_brand):
        # if not car_brand:
        #     raise ValueError("Missing brand")
        self._brand = car_brand

    @brand.deleter
    def brand(self):
        print(f"Delete {self.brand}")
        self._brand = None

    @property
    def color(self):
        return self.____color

    @color.setter
    def color(self, car_color):
        if car_color not in Car.colors:
            raise ValueError("Invalid color option")
        self.____color = car_color

    def __str__(self):
        return f"Brand: {self.brand}. Color: {self.color}. Model: {self.model}"


# def main():
#     car = desirable_car()
#     print(f"I want to get {car.brand} car, model {car.model} in a {car.color} color")
#     car.color = "black"
#     print(f"New color of {car.brand} is {car.color} now")
#     print()

#     # Use custom deleter function to unset color value
#     test_deleter_car = Car("BMW", "black", "700")
#     print(test_deleter_car)
#     del test_deleter_car.brand
#     print(test_deleter_car)
#     print()

#     # We can add any new instance variable even if it is not declared in __init__
#     car.new_variable = "some value"
#     print(car)
#     print(car.new_variable)
#     print()

#     # # How python trust concept (conventions) works
#     car._color = "blue HA_HA_HA!"
#     print(car)


# Test setters Error raise
# car_2 = Car("Opel", "blue", "Omega")
# print(car_2)

# car_3 = Car("", "black", "911")
# print(car_3)


def desirable_car():
    return Car("Tesla", "silver", "S")


# if __name__ == "__main__":
#     main()
#     print("\n\n")
#     print(Car)
#     print(Car("Tesla", "white"))
#     print(Car("Reno", "red"))
#     print(desirable_car)
#     print(desirable_car())


# 3.1 Encapsulating all related functionality


class CarFull:
    colors: list[str] = [
        "black",
        "white",
        "silver",
        "red",
    ]

    def __init__(self, brand, color, model=None):
        self.brand = brand
        self.color = color
        self.model = model

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if not brand:
            raise ValueError("Missing Brand")
        self._brand = brand

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if color not in CarFull.colors:
            raise ValueError("This color is not available")
        self._color = color

    def __str__(self):
        return f"I want to buy {self.brand} {self.model} in {self.color} color."

    @classmethod
    def get(cls):
        # brand: str = 'Porsche'
        # color: str = 'silver'
        # model: str = '911 Carrera GT'
        brand: str = input("Brand: ")
        color: str = input("Color: ")
        model: str = input("Model: ")
        return cls(brand, color, model)


# def main():
#     dream_car = CarFull.get()
#     print(dream_car)


# 4. CLASS Methods
class BigBang:
    def __init__(self):
        self.planets = [
            "Venus",
            "Saturn",
            "Mars",
            "Earth",
            "Pluto",
            "Mercury",
            "Jupiter",
            "Uranus",
            "Neptune",
        ]

    def create_planet(self):
        new_planet = random.choice(self.planets)
        return new_planet


bang = BigBang()
new_planet = bang.create_planet()

# print(new_planet)


# 4.1 SINGLETON


class BigBang:
    planets = [
        "Venus",
        "Saturn",
        "Mars",
        "Earth",
        "Pluto",
        "Mercury",
        "Jupiter",
        "Uranus",
        "Neptune",
    ]

    @classmethod
    def create_planet(cls):
        new_planet = random.choice(cls.planets)
        return new_planet


new_planet = BigBang.create_planet()

# print(new_planet)


# INHERITANCE


# Superclass (Parent)
class Fish:
    waterbodies: list[str] = ["river", "lake", "pond", "canal", "aquarium"]

    def __init__(self, name: str, color: str, size: float = None) -> None:
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return f"Name: {self._name}. Color: {self.color}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @classmethod
    def get(cls):
        # name: str = input("Name: ")
        # color: str = input("Color: ")
        name: str = "Molly"
        color: str = "Black"
        return cls(name, color)

    @classmethod
    def add_waterbody(cls, waterbody):
        if waterbody not in cls.waterbodies:
            cls.waterbodies.append(waterbody)
            print(f"{waterbody} added to waterbodies list successfully")
        else:
            print(f"{waterbody} already present")

    @classmethod
    def remove_waterbody(cls, waterbody):
        if waterbody in cls.waterbodies:
            cls.waterbodies.remove(waterbody)
            print(f"{waterbody} removed from waterbodies list successfully")
        else:
            print(f"There is no {waterbody} in the list")


# Sub class (child)
class AquariumFish(Fish):
    def __init__(self, name, color, min_volume_litres, size=None):
        super().__init__(name, color, size)
        self.min_volume_litres = min_volume_litres

    @property
    def min_volume_litres(self):
        return self._min_volume_litres

    @min_volume_litres.setter
    def min_volume_litres(self, min_volume_litres):
        if not min_volume_litres:
            raise ValueError("Missing minimum tank size")
        if min_volume_litres < 1:
            raise ValueError("Minimum volume should be positive integer")
        self._min_volume_litres = min_volume_litres


class WildNatureFish(Fish):
    def __init__(self, name, color, waterbody, size=None):
        super().__init__(name, color, size)
        self.waterbody = waterbody

    @property
    def waterbody(self):
        return self._waterbody

    @waterbody.setter
    def waterbody(self, cls, waterbody):
        if waterbody not in cls.waterbodies:
            raise ValueError("Missing waterbody")
        self._waterbody = waterbody


# def main():
#     fish: Fish = Fish.get()
#     print(fish.color)

#     tank_fish: AquariumFish = AquariumFish(fish.name, fish.color, 55)
#     print(tank_fish)
#     print(tank_fish.color, tank_fish.name)

#     # Inheritance builtin test methods
#     print(isinstance(fish, Fish))
#     print(issubclass(AquariumFish, Fish))

#     # Check if class methods inherited to subclass instance
#     print(tank_fish.waterbodies)
#     tank_fish.add_waterbody("wine glass")
#     print(tank_fish.waterbodies)

#     tank_fish.remove_waterbody("wine glass")
#     print(tank_fish.waterbodies)

#     tank_fish.remove_waterbody("doesn't exist")


# MULTIPLE INHERITANCE
class Swimmer:
    def swim(self):
        print("Swimming")


class Runner:
    def run(self):
        print("Running")


class Whale(Swimmer):
    pass


class Tiger(Runner):
    pass


class Beaver(Runner, Swimmer):
    pass


# def main():
#     beaver = Beaver()
#     beaver.run()
#     beaver.swim()


# MULTI LEVEL INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def run(self):
        print(f"{self.name} is running away")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Lion(Predator):
    pass


# def main():
#     lion_king = Lion("Simba")
#     print(lion_king.is_alive)
#     lion_king.hunt()


# ABSTRACT CLASSES


class Clock(ABC):
    @abstractmethod
    def show_time():
        pass

    @abstractmethod
    def set_time():
        pass

    @abstractmethod
    def turn_on():
        pass

    @abstractmethod
    def turn_off():
        pass


class WallClock(Clock):
    def show_time(self):
        print(f"Current time is: {dt.now().strftime('%H:%M')}")

    def set_time(self):
        print("Move the gear wheel")

    def turn_on(self):
        print("Move switcher button up")

    def turn_off(self):
        print("Move switcher button down")


class SmartWatch(Clock):
    def show_time(self):
        print(f"Current time is: {dt.now().strftime('%H:%M')}")

    def set_time(self):
        print("Entering menu -> settings -> change time")

    def turn_on(self):
        print("Hold the menu button for 5 seconds")

    def turn_off(self):
        print("Hold the menu button - > navigate to 'switch off' -> press 'start' button")


# def main():
#     wall_clock = WallClock()
#     wall_clock.show_time()

#     apple_watch = SmartWatch()
#     apple_watch.turn_on()
#     apple_watch.show_time()


# POLYMORPHISM (Many forms)


# Polymorphism by inheritance
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class ElectricCar(Vehicle):
    def go(self):
        return "Electric car moves"

    def stop(self):
        return "Electric car stops"


class DieselCar(Vehicle):
    def go(self):
        return "Diesel car moves"

    def stop(self):
        return "Diesel car stops"


class Tractor(DieselCar):
    def go(self):
        return "Tractor moves"

    def stop(self):
        return "Tractor stops"


class Tesla(ElectricCar):
    def go(self):
        return "Tesla car moves"

    def stop(self):
        return "Tesla car stops"


# Polymorphism by 'Duck typing' rule - Object must have the minimum necessary attributes / methods
# 'If it looks like a duck and quacks like a duck - IT MUST BE A DUCK!'
class Snail:
    def go(self):
        return "Snail moves"

    def stop(self):
        return "Snail stops"


# def main():
#     # vehicles = [ElectricCar(), Tesla(), DieselCar(), Tractor()]

#     # Assume Snail is a vehicle according to 'Duck typing' rule
#     vehicles = [ElectricCar(), Tesla(), DieselCar(), Tractor(), Snail()]
#     for vehicle in vehicles:
#         print(vehicle.go())


# AGGREGATION
#   Aggregation - Represents a relationship where one object (the whole) contains references to one or more INDEPENDENT objects (the parts)


class ItCompany:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return f"{self.name} has {len(self.employees)} employees"


class ItSpecialist:
    def __init__(self, first_name, last_name, position):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    def __str__(self):
        return f"{self.first_name}{self.last_name} is a {self.position}"


# def main():
#     company: ItCompany = ItCompany("Google")
#     print(company)

#     engineer_1: ItSpecialist = ItSpecialist(
#         first_name="Neet", last_name="Code", position="Software Engineer"
#     )
#     engineer_2: ItSpecialist = ItSpecialist(
#         first_name="Y", last_name="King", position="Senior Software Engineer"
#     )

#     company.add_employee(engineer_1)
#     company.add_employee(engineer_2)
#     print(company)

#     for employee in company.employees:
#         print(employee)


# COMPOSITION
#   The composed objects directly ! OWNS ! its components, which cannot exist independently
#   THis is "Owns-a" relationship, while ABSTRACTION has "has-a" relationship between objects


class Cheese:
    def __init__(self, cheese_type):
        self.cheese_type = cheese_type

    def __str__(self):
        return f"It's a {self.cheese_type} cheese"


class Patty:
    def __init__(self, meat_type):
        self.meat_type = meat_type

    def __str__(self):
        return f"This patty is cooked from {self.meat_type} meat"


class Bread:
    def __init__(self, bread_type):
        self.bread_type = bread_type

    def __str__(self):
        return f"It's a {self.bread_type}"


class Burger:
    def __init__(self, burger_type, bread_type, meat_type, cheese_type):
        self.burger_type = burger_type
        self.bread = [Bread(bread_type) for _ in range(2)]
        self.cheese = Cheese(cheese_type)
        self.patty = Patty(meat_type)

    def __str__(self):
        return (
            f"This {self.burger_type} consists of {len(self.bread)} {self.bread[0].bread_type}, "
            f"with a {self.patty.meat_type} patty and {self.cheese.cheese_type} cheese inside"
        )


def main():
    cheeseburger: Burger = Burger(
        burger_type="cheeseburger", bread_type="bun", meat_type="beef", cheese_type="cheddar"
    )
    print(cheeseburger.bread[0])
    print(cheeseburger.cheese)
    print(cheeseburger.patty)
    print(cheeseburger)


# SUPER() METHOD. METHODS OVERWRITING


class Shape:
    def __init__(self, color, color_filled):
        self.color = color
        self.color_filled = color_filled

    def __str__(self):
        return f"It's {self.color} and {'filled' if self.color_filled else 'not filled'}"


class Circle(Shape):
    def __init__(self, color, color_filled, radius):
        super().__init__(color, color_filled)
        self.radius = radius

    # Parent (Super) class method overwriting
    def __str__(self):
        print(super().__str__())
        return f"It's area is {self.radius**2 * 3.14} cm"


class Square(Shape):
    def __init__(self, color, color_filled, width):
        super().__init__(color, color_filled)
        self.width = width

    # Parent (Super) class method overwriting
    def __str__(self):
        print(super().__str__())
        return f"It's area is {self.width**2} cm"


class Triangle(Shape):
    def __init__(self, color, color_filled, width, height):
        super().__init__(color, color_filled)
        self.width = width
        self.height = height

    # Parent (Super) class method overwriting
    def __str__(self):
        print(super().__str__())
        return f"It's area is {self.width * self.height / 2} cm"


# def main():
#     circle = Circle(radius=5, color="Green", color_filled=True)
#     print(circle)

#     square = Square(width=6, color="Red", color_filled=True)
#     print(square)

#     triangle = Triangle(width=6, height=5, color="Yellow", color_filled=False)
#     print(triangle)


# MAGIC (dUnder) METHODS. OPERATOR OVERLOADING.


class FishTank:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Total size is {self.size}"

    def __repr__(self):
        return f"FishTank(size={self.size})"

    def __add__(self, other):
        if isinstance(other, FishTank):
            return self.size + other.size
        raise TypeError("Invalid type")

    def __sub__(self, other):
        if isinstance(other, FishTank):
            return self.size - other.size
        raise TypeError("Invalid type")


# def main():
#     molly_to_buy: int = 3
#     molly: AquariumFish = AquariumFish("Molly", "Black", 10 * molly_to_buy)

#     guppy_to_buy: int = 5
#     guppy: AquariumFish = AquariumFish("Guppy", "Silver", 5 * guppy_to_buy)

#     molly_tank: FishTank = FishTank(molly.min_volume_litres)
#     guppy_tank: FishTank = FishTank(guppy.min_volume_litres)

#     print(molly_tank)
#     print(guppy_tank)
#     print()

#     general_tank: FishTank = molly_tank + guppy_tank
#     print(general_tank)
#     print()

#     # __str__ VS __repr__
#     print(molly_tank)
#     print(str(molly_tank))
#     print(molly_tank.__str__())

#     print(repr(molly_tank))
#     print(molly_tank.__repr__())
#     print()

#     # Magic methods in built-in classes
#     print(int.__add__(2, 1))
#     print("hello".__add__(" world"))
#     print(str.__len__("some test string"))


# EXAMPLES OF CREATING CUSTOM CONTEXT MANAGERS AND ITERATORS by using related magic methods


# CUSTOM RANGE Class Implementation
class MyRange:
    def __init__(self, start_value):
        self.start_value = start_value

    @property
    def start_value(self):
        return self._start_value

    @start_value.setter
    def start_value(self, start_value):
        if isinstance(start_value, int):
            self._start_value = start_value
        else:
            raise TypeError("Invalid Type")

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_value > 0:
            current = self.start_value
            self.start_value -= 1
            return current
        raise StopIteration


# CUSTOM CONTEXT MANAGER Implementation
class MyDbConnectionManager:
    "Simulate a DataBase Connection with custom context manager"

    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        self.connected = True
        print(f"Connected to {self.db_name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connected = False
        print(f"Disconnected from {self.db_name}")
        # Handle exceptions
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppresses exceptions if they occur


# def main():
#     for i in MyRange(6):
#         print(i)

#     with MyDbConnectionManager("My_DB_Engine") as db:
#         print(f"Connected to Database: {db.connected}")


# Class variables, Class Methods, Static Methods

# Class variables:
#   - shared among all instances of a class
#   - Defined outside the constructor
#   - Allow to share among all objects created from that class


class StoreSoldItems:
    sold_items: int = 0
    uah_to_usd_rate: float = 42.00

    def __init__(self, item_type: str, item_brand: str, item_price_usd: float):
        self.item_type = item_type
        self.item_brand = item_brand
        self.item_price_usd = item_price_usd
        StoreSoldItems.sold_items += 1

    def get_price_uah(self):
        return self.item_price_usd * self.uah_to_usd_rate
        # return self.item_price_usd * StoreSoldItems.uah_to_usd_rate

    @classmethod
    def update_rate(cls, new_rate_uah: float):
        cls.uah_to_usd_rate = new_rate_uah

    @classmethod
    def from_string(cls, item_string):
        parsed_type, parsed_brand, parsed_price = item_string.split("-")
        return cls(parsed_type, parsed_brand, int(parsed_price))

    @staticmethod
    def get_uah_rate():
        # url_endpoint = 'some_url_api'
        # response = requests.get(url_endpoint)
        # response.raise_for_status()
        # return response.json().get("UAH")
        return 43.0

    def __str__(self):
        return f"{self.item_brand} {self.item_type} current price is {self.get_price_uah()} UAH"


# def main():
#     laptop: StoreSoldItems = StoreSoldItems("laptop", "Apple", 2500)
#     phone: StoreSoldItems = StoreSoldItems("phone", "Samsung", 1500)
#     print(f"Total items sold: {StoreSoldItems.sold_items}")

#     # Use cases when better to modify class variables by instance not class call
#     print(laptop)
#     laptop.uah_to_usd_rate = 42.5
#     print(laptop)

#     # We can call instance method from class by passing instance instead of self
#     print(phone.get_price_uah())
#     print(StoreSoldItems.get_price_uah(phone))

#     # Use classmethod to update class variable
#     print(phone)
#     StoreSoldItems.update_rate(45.00)
#     print(phone)

#     # Classmethod as alternative constructor
#     item_string: str = "toaster-gorenje-50"
#     toaster: StoreSoldItems = StoreSoldItems.from_string(item_string)
#     print(toaster)

#     # Use staticmethod to get current rate
#     new_rate = StoreSoldItems.get_uah_rate()
#     StoreSoldItems.update_rate(new_rate)
#     print(phone)


if __name__ == "__main__":
    main()
