class Vehicle:
    lecenseCode = ""
    serialCode = ""
    wheelQuantity = 0
    doorQuantity = 0
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    def turboBoost(self):
        print("Turn On nitrous")
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    def television(self):
        print("Turn On TV")
class EstateCar(Vehicle):
    luxuryMaterial = ""

car1 = Car()
car1.turnOnAirConditioner()
car1.turboBoost()
pickup1 = Pickup()
pickup1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()
estateCar1 = EstateCar()
estateCar1.turnOnAirConditioner()