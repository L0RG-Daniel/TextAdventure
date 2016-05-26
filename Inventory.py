class Inventory:
    def __init__(self):
        self.items = []
        self.size = 25

    #Check size of space left in inventory.
    def space_left(self):
        space_left = self.size
        for item in self.items:
            space_left -= item.weight
        return space_left

    #Method for determining if a specific item fits in inventory.
    def fits(self, item):
        if item.weight <= self.space_left():
            return True
        else:
            return False