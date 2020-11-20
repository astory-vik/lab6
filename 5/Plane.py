from vehicle import Vehicle
class Plane(Vehicle):
    hight = 0
    passengers = 0
    def __init__(self, price, speed, year, passengers):
        super().__init__(price, speed, year)
        self.passengers = passengers
    def GiveCoordinates(self):
        super().GiveCoordinates()
    def GoX(self):
        self.X += self.speed
    def GoZ(self):
        self.Z += self.speed
    def GoUP(self):
        self.hight += self.speed
    def GoDown(self):
        self.hight -= self.speed