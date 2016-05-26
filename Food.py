from Item import *

class Food(Item):
    def __init__(self, name, weight, heal, amount):
        super().__init__(name, weight)
        self.eff = heal
        self.amount = amount

    #Method for showing food item in inventory (during fight)
    def get_food(self):
        return ": " + self.name.title() + ", heals: " + str(self.eff) + ", amount left: " + str(self.amount)

    #Method that returns string for saving data in savefile.txt
    def save_food(self):
        return self.name+","+str(self.weight)+","+str(self.eff)+","+str(self.amount)+"/"