from Item import *

class Weapon(Item):
    def __init__(self, name, weight, dmg):
        super().__init__(name, weight)
        self.eff = dmg

    #Method for showing weapon in inventory (during fight)
    def get_wpn(self):
        return ": " + self.name.title() + ", damage: " + str(self.eff)

    #Method that returns string for saving data in savefile.txt
    def save_wpn(self):
        return self.name+","+str(self.weight)+","+str(self.eff)+"/"