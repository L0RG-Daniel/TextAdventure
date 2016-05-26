class NPC:
    def __init__(self, name, health, dmg, status):
        self.name = name
        self.health = health
        self.status = status
        self.eff = dmg

    #NPC's can be either good or evil.
    def is_good(self):
        if self.status == "good":
            return True
        else:
            return False

    def get_hp(self):
        return self.health