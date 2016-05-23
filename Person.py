from NPC import *

class Person(NPC):
    def __init__(self, name, health, status, bonus):
        super().__init__(name, health, status)
        self.bonus = bonus
