from Item import *

class Weapon(Item):
    def __init__(self, name, weight, dmg):
        super().__init__(name, weight)
        self.base_dmg = dmg
