from Item import *

class Food(Item):
    def __init__(self, name, weight, heal, amount):
        super().__init__(name, weight)
        self.heal = heal
        self.amount = amount