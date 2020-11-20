from vehicle import Vehicle
class Ship(Vehicle):
    passangers = 0
    port = ""
    def __init__(self, price, speed, year, passengers, port):
        super().__init__(price, speed, year)
        self.passengers = passengers
        self.port = port
    def GiveCoordinates(self):
        super().GiveCoordinates()
    def GoX(self):
        self.X += self.speed
    def GoZ(self):
        self.Z += self.speed