# Base class
class Vehicle:
    def move(self):
        pass  # Method to be overridden

# Subclasses with specific implementations
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Instantiate objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrate polymorphism
vehicles = [car, plane, boat]
for vehicle in vehicles:
    print(vehicle.move())  # Output: Driving 🚗, Flying ✈️, Sailing 🚤
