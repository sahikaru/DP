#!/usr/env python

class Beverage():
    def __init__(self):
        self.description = "Unknow"

    def cost(self):
        pass

class CondimentDecorator(Beverage):
    def getDescription(self):
        return self.beverage.description
        

class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "HouseBlend"

    def cost(self):
        return 0.89
class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast"
    
    def cost(self):
        return 1.20

class Mocha(CondimentDecorator):
    def __init__(self,beverage):
        self.beverage = beverage 

    def getDescription(self):
        return self.beverage.getDescription + " , Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20

class Whip(Beverage):
    def __init__(self,beverage):
        self.beverage = beverage 

    def getDescription(self):
        return self.beverage.getDescription + " , Whip"

    def cost(self):
        return self.beverage.cost() + 0.30
        

if __name__ == "__main__":
    coffee = DarkRoast()
    coffee = Mocha(coffee)
    coffee = Mocha(coffee)
    coffee = Whip(coffee)
    print coffee.cost()

