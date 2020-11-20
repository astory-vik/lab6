from abc import ABC, abstractmethod
from vehicle import Vehicle


class Car(Vehicle):
    def GiveCoordinates(self):
        super().GiveCoordinates()

    def GoX(self):
        self.X += self.speed

    def GoZ(self):
        self.Z += self.speed
