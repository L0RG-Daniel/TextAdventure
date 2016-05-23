from NPC import *

class Monster(NPC):
    def __init__(self, name, health, status, dmg):
        super().__init__(name, health, status)
        self.base_dmg = dmg
