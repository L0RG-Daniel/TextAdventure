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
        self.lost = False
        
        #Create testing items.
        self.curr_weapon = Weapon("Fists", 0, 10)
        f1 = Food("apple", 1, 30, 1)
        f2 = Food("bread", 3, 50, 3)
        w1 = Weapon("knife", 2, 25)
        self.p_inv.items.append(f1)
        self.p_inv.items.append(f2)
        self.p_inv.items.append(self.curr_weapon)
        self.p_inv.items.append(w1)
        
    #Method for clearing screen.
    def clr(self):
        os.system('cls')

    #Switch turns between player and monster.
    def switch(self):
        if self.turn =='P':
            self.turn = 'NPC'
        else:
            self.turn = 'P'

    #Loop through every item in inventory, show correct information on screen.
    def show_items(self):
        self.clr()
        print("-- Items --")
        for i in range(0,len(self.p_inv.items)):
            if self.curr_weapon == self.p_inv.items[i]:
                print(str(i+1) + ": " + self.p_inv.items[i].name.title() + ", damage: " + str(self.p_inv.items[i].eff) + ", currently equipped.")
            elif isinstance(self.p_inv.items[i], Weapon):
                print(str(i+1) + ": " + self.p_inv.items[i].name.title() + ", damage: " + str(self.p_inv.items[i].eff))
            elif isinstance(self.p_inv.items[i], Food):
                print(str(i+1) + ": " + self.p_inv.items[i].name.title() + ", heals: " + str(self.p_inv.items[i].eff) + ", amount left: " + str(self.p_inv.items[i].amount))
            else:
                print(str(i+1) + ": " + self.p_inv.items[i].name.title())

    #Print fight stats to the screen.
    def game_status(self):
        self.clr()
        print("")
        print("     You are fighting (" + self.enemy.name + ") with " + str(self.enemy.health) + "/" + str(self.ene_start_hp) + " health.")
        print("     Your current health is " + str(self.p_health) + "/100.")
        print("     Your current weapon is (" + self.curr_weapon.name + ") with damage " + str(self.curr_weapon.eff) + ".")

    #Method for starting a fight, eventually a winner will arise.
    def start(self):

        #Loop through item list
        #Select the weapon

        while not self.over:
            self.game_status()

            if self.turn == 'P':
                print("")
                res = input("     What do you want to do? (att/items): ")
                while not res in ('att', 'items'):
                    self.game_status()
                    print("")
                    print("     Incorrect input.")
                    res = input("     What do you want to do? (att/items): ")
                if res == 'att':
                    self.clr()
                    self.enemy.health -= self.curr_weapon.eff
                    print("")
                    print("     You hit (" + self.enemy.name + ") with (" + self.curr_weapon.name + ") for " + str(self.curr_weapon.eff) + " damage!")
                    print("     Enemy health is now " + str(self.enemy.health) + "/" + str(self.ene_start_hp) + ".")
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
                        item.amount -=1
                        if item.amount == 0:
                            print("You have now run out of item " + item.name + "!")
                            self.p_inv.items.pop(ind-1)
                        input("")
                    else:
                        self.clr()
                        print("Prof. Oak: Now is not the time to use that!")
                        input("")
                self.switch()

            else:
                #Enemy turn.
                self.clr()
                self.p_health -= self.enemy.dmg
                print("")
                print("     (" + self.enemy.name.title() + ") has hit you for " + str(self.enemy.dmg) + " damage!")
                self.switch()
                input("")
                
            if self.enemy.health < 1:
                self.over = True
                print("     You killed the enemy!")
                input("")

            if self.p_health < 1:
                self.over = True
                self.lost = True
                self.clr()
                print("\n\n")
                print("Oh, no!".center(80))
                print("The enemy killed you!".center(80))
                input("")

        return self.lost
