class Vehicle:
    def __init__(self):
        print('vehicle')

class Car(Vehicle):
    def __init__(self):
        print("car")

class RaceCar(Car):
    def __init__(self):
        print("RaceCar")

class Plane(Vehicle):
    def __init__(self):
        print("Plane")
class Boat(Vehicle):
    def __init__(self):
        print("Boat")


a = Boat()