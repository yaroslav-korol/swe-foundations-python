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
    colors: list[str] = ["black", "white", "silver", "red", ]

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
    planets = ["Venus", "Saturn", "Mars", "Earth", "Pluto", "Mercury", "Jupiter", "Uranus", "Neptune"]
    
    @classmethod
    def create_planet(cls):
        new_planet = random.choice(cls.planets)
        return new_planet
    

new_planet = BigBang.create_planet()

# print(new_planet)





# INHERITANCE

# Superclass

class Fish:
    waterbodies: list[str] = ["river", "lake", "pond", "canal", "tank"]

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
        name: str = input("Name: ")
        color: str = input("Color: ")
        # name: str = "Molly"
        # color: str = "Black"
        return cls(name, color)

    

class AquariumFish(Fish):
    def __init__(self, name, color, min_tank_size, size=None):
        super().__init__(name, color, size)
        self.min_tank_size = min_tank_size
    

    @property
    def min_tank_size(self):
        return self._min_tank_size
        
    @min_tank_size.setter
    def min_tank_size(self, min_tank_size):
        if not min_tank_size:
            raise ValueError("Missing minimum tank size")
        if min_tank_size < 1:
            raise ValueError("Minimum size should be positive integer")
        self._min_tank_size = min_tank_size


    # @classmethod
    # def get(cls):
    #     """Override get method for AquariumFish-specific attributes."""
    #     fish = super().get()  # Get common Fish attributes (name, color)
    #     min_tank_size = float(input("Minimum tank size: "))
    #     # Return an instance of AquariumFish with all attributes
    #     return cls(fish.name, fish.color, min_tank_size, fish.size)
    

class WildNatureFish(Fish):
    def __init__(self, name, color, waterbody, size=None):
        super().__init__(name, color, size)
        self.waterbody = waterbody

    @property
    def waterbody(self):
        return self._waterbody
    
    @waterbody.setter
    def waterbody(self, cls, waterbody):
        if not waterbody in cls.waterbodies:
            raise ValueError("Missing waterbody")
        self._waterbody = waterbody


def main():
    fish: Fish = Fish.get()
    print(fish.color)

    tank_fish: AquariumFish = AquariumFish(fish.name, fish.color, 55)
    print(tank_fish)
    print(tank_fish.color, tank_fish.name)


if __name__ == "__main__":
    main()