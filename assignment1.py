# Base class
class Superhero:
    def __init__(self, name, power, alias):
        self.__alias = alias  # Encapsulated attribute
        self.name = name
        self.power = power

    def reveal_identity(self):
        return f"The real name of {self.name} is {self.__alias}."

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass inheriting from Superhero
class FlyingHero(Superhero):
    def __init__(self, name, power, alias, flying_speed):
        super().__init__(name, power, alias)
        self.flying_speed = flying_speed

    def fly(self):
        return f"{self.name} is flying at {self.flying_speed} km/h!"

# Instantiate objects
superman = FlyingHero("Superman", "Super Strength", "Clark Kent", 300)
batman = Superhero("Batman", "Martial Arts", "Bruce Wayne")

# Use the methods
print(superman.reveal_identity())  # Output: The real name of Superman is Clark Kent.
print(superman.fly())              # Output: Superman is flying at 300 km/h!
print(batman.use_power())          # Output: Batman uses Martial Arts!
