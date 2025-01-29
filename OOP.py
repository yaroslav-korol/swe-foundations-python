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
#     colors: list[str] = ['black', 'silver', 'white', 'red']
#     def __init__(self, brand, color, model=None):
#         if not brand:
#             raise ValueError("Missing brand")

#         if color not in self.colors:
#             raise ValueError("Invalid color option")

#         self.brand = brand
#         self.color = color
#         self.model = model


#     def __str__(self):
#         return f"Brand: {self.brand}. Color: {self.color}. Model: {self.model}"


# def main():
#     car = desirable_car()
#     print(f"I want to get {car.brand} car, model {car.model} in a {car.color} color")
#     car.color = 'black'
#     print(f"New color of {car.brand} is {car.color} now")

#     car.new_variable = "some value"
#     print(car)
#     print(car.new_variable)


# def desirable_car():
#     return Car('Tesla', 'silver', 'S')


# if __name__ == "__main__":
#     main()
#     print(Car)
#     print(Car('Tesla', 'silver'))
#     print(Car('Reno', 'red'))
#     print(desirable_car)
#     print(desirable_car())


# 3. GETters and SETters

# class Car:
#     colors: list[str] = ['black', 'silver', 'white', 'red']

#     def __init__(self, brand, color, model=None):
#         self.brand = brand
#         self.color = color
#         self.model = model

#     @property
#     def brand(self):
#         return self._brand

#     @brand.setter
#     def brand(self, brand):
#         if not brand:
#             raise ValueError("Missing brand")
#         self._brand = brand

#     @property
#     def color(self):
#         return self.____color

#     @color.setter
#     def color(self, color):
#         if color not in self.colors:
#             raise ValueError("Invalid color option")
#         self.____color = color


#     def __str__(self):
#         return f"Brand: {self.brand}. Color: {self.color}. Model: {self.model}"


# def main():
#     car = desirable_car()
#     print(f"I want to get {car.brand} car, model {car.model} in a {car.color} color")
#     car.color = 'black'
#     print(f"New color of {car.brand} is {car.color} now")

#     car.new_variable = "some value"
#     print(car)
#     print(car.new_variable)

#     print('\n')

#     car._color = 'blue HA_HA_HA!'
#     print(car)


# car_2 = Car('Opel', 'blue', 'Omega')
# print(car_2)

# car_3 = Car('', 'black', '911')
# print(car_3)


# def desirable_car():
#     return Car('Tesla', 'silver', 'S')


# if __name__ == "__main__":
#     main()

#     print('\n\n')
#     print(Car)
#     print(Car('Tesla', 'white'))
#     print(Car('Reno', 'red'))
#     print(desirable_car)
#     print(desirable_car())


# 3.1 Encapsulating all related functionality


class Car:
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
        if color not in self.colors:
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


def main():
    dream_car = Car.get()
    # print(dream_car)


# if __name__ == "__main__":
#     main()


# 4. CLASS Methods
import random

# class BigBang:
#     def __init__(self):
#         self.planets = ["Venus", "Saturn", "Mars", "Earth", "Pluto", "Mercury", "Jupiter", "Uranus", "Neptune"]

#     def create_planet(self):
#         new_planet = random.choice(self.planets)
#         return new_planet


# bang = BigBang()
# new_planet = bang.create_planet()

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

# Superclass


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


def main():
    fish: Fish = Fish.get()
    print(fish.color)

    tank_fish: AquariumFish = AquariumFish(fish.name, fish.color, 55)
    print(tank_fish)
    print(tank_fish.color, tank_fish.name)

    # Inheritance builtin test methods
    print(isinstance(fish, Fish))
    print(issubclass(AquariumFish, Fish))

    # Check if class methods inherited to subclass instance
    print(tank_fish.waterbodies)
    tank_fish.add_waterbody("wine glass")
    print(tank_fish.waterbodies)

    tank_fish.remove_waterbody("wine glass")
    print(tank_fish.waterbodies)

    tank_fish.remove_waterbody("doesn't exist")


# Operator overloading


class FishTank:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Total size is {self.size}"

    def __add__(self, other):
        return self.size + other.size

    def __sub__(self, other):
        return self.size - other.size


# def main():
#     molly_to_buy: int = 3
#     molly: AquariumFish = AquariumFish("Molly", "Black", 10 * molly_to_buy)

#     guppy_to_buy: int = 5
#     guppy: AquariumFish = AquariumFish("Guppy", "Silver", 5 * guppy_to_buy)

#     molly_tank: FishTank = FishTank(molly.min_volume_litres)
#     guppy_tank: FishTank = FishTank(guppy.min_volume_litres)

#     print(molly_tank)
#     print(guppy_tank)

#     general_tank: FishTank = molly_tank + guppy_tank
#     print(general_tank)


# Class variables, Class Methods, Static Methods


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
