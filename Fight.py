import os
from Weapon import *
from Food import *

class Fight():
    def __init__(self, p_name, p_health, p_inv, p_comp, NPC):
        self.p_name = p_name
        self.p_health = p_health
        self.p_inv = p_inv
        self.p_comp = p_comp
        self.enemy = NPC
        self.over = False
        self.turn = 'P'
        self.ene_start_hp = self.enemy.health
        
        #Testing items 
        self.curr_weapon = Weapon("Fists", 0, 10)
        f1 = Food("apple", 1, 30, 5)
        f2 = Food("bread", 3, 50, 1)
        w1 = Weapon("knife", 2, 25)
        self.p_inv.items.append(f1)
        self.p_inv.items.append(f2)
        self.p_inv.items.append(self.curr_weapon)
        self.p_inv.items.append(w1)
        
    def clr(self):
        os.system('cls')

    def switch(self):
        if self.turn =='P':
            self.turn = 'NPC'
        else:
            self.turn = 'P'

    def show_items(self):
        self.clr()
        print("-- Items --")
        for i in range(0,len(self.p_inv.items)):
            print(str(i+1) + ": " + self.p_inv.items[i].name.title() + ", " + str(self.p_inv.items[i].eff))

    def start(self):

        #Loop through item list
        #Select the weapon

        while not self.over:
            if self.enemy.health < 1:
                print("FIGHT OVER - P WON")
                self.over = True
            elif self.p_health < 1:
                print("FIGHT OVER - E WON")
                self.over = True
            else:
                self.clr()
                if self.turn == 'P':
                    res = input("What do you want to do? (att/items): ")
                    while not res in ('att', 'items'):
                        self.clr()
                        res = input("What do you want to do? (att/items): ")
                    if res == 'att':
                        self.enemy.health -= self.curr_weapon.eff
                        print("You hit (" + self.enemy.name + ") with (" + self.curr_weapon.name + ") for " + str(self.curr_weapon.eff) + " damage!")
                        print("Enemy health is now " + str(self.enemy.health) + "/" + str(self.ene_start_hp) + ".")
                        input("")
                    else:
                        self.show_items()
                        
                        q = input("Select item: ")
                        corr = False
                        ind = 0
                        while not corr:
                            try:
                                ind = int(q)
                                if ind > len(self.p_inv.items):
                                    self.show_items()
                                    q = input("Select item: ")
                                else:
                                    corr = True
                            except ValueError:
                                self.show_items()
                                q = input("Select item: ")                    
                        item = self.p_inv.items[ind-1]
                        if isinstance(item, Weapon):
                            if item == self.curr_weapon:
                                print("This item is already equipped!")
                                input("")
                            else:
                                self.curr_weapon = item
                                print(item.name.title() + " with damage " + str(item.eff) + " is now equipped!")
                                input("")
                        elif isinstance(item, Food):
                            self.p_health += item.eff
                            print(item.name.title() + " has healed " + str(item.eff) + " health!")
                            input("")
                        else:
                            self.clr()
                            print("Prof. Oak: Now is not the time to use that!")
                            input("")
                
                if self.enemy.health < 1:
                    self.over = True
