from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel, consumption):
        self.fuel = fuel
        self.consumption = consumption

    @abstractmethod
    def drive(self, km): 
        pass
    @abstractmethod
    def refuel(self, amount):
        pass


class Car(Vehicle):
    def drive(self, km):
        need = km * (self.consumption + 0.9)
        if self.fuel >= need:
            self.fuel -= need

    def refuel(self, amount):
        self.fuel += amount


class Truck(Vehicle):
    def drive(self, km):
        need = km * (self.consumption + 1.6)
        if self.fuel >= need:
            self.fuel -= need

    def refuel(self, amount):
        self.fuel += amount * 0.95

car = Car(20, 5)
car.drive(3)
print(car.fuel)     
car.refuel(10)
print(car.fuel)      

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel)   
truck.refuel(50)
print(truck.fuel)    
