class Inventory():
    def __init__(self):
        self.items = []
        self.size = 25

    def space_left(self):
        space_left = self.size
        for item in self.items:
            space_left -= item['weight']
        return space_left

    def fits(self, item):
        if item.weight <= self.space_left():
            return True
        else:
            return False
