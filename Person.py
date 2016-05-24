from NPC import *

class Person(NPC):
    def __init__(self, name, health, dmg, status, bonus):
        super().__init__(name, health, dmg, status)
        self.bonus = bonus
