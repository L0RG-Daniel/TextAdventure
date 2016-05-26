from NPC import *

class Person(NPC):
    def __init__(self, name, health, eff, status, bonus):
        super().__init__(name, health, eff, status)
        self.bonus = bonus