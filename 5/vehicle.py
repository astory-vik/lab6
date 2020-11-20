from abc import ABC, abstractmethod


class Vehicle(ABC):
    X = 0
    Y = 0
    Z = 0
    price = 0
    speed = 0
    year = 0
    def __init__(self, price, speed, year):
        self.price = price
        self.speed = speed
        self.year = year
    @abstractmethod
    def GiveCoordinates(self):
        print(str(self.X) + " ; " + str(self.Y) + " ; " + str(self.Z))

