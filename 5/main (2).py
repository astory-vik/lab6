from Car import Car
from Plane import Plane
from ship import Ship
def Main():
    mycar = Car(123, 200, 1991)
    mycar.GiveCoordinates()
    mycar.GoX()
    mycar.GoZ()
    print(f"{mycar.X} + {mycar.Z}")
    plane = Plane(600, 500, 2013, 11)
    print(plane.passengers)
    ship = Ship(300, 35, 1999, 500, "Spain")
    print(ship.port)

if __name__ == '__main__':
    Main()