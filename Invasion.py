import os
import time
import re
from Person import *
from Food import *
from Inventory import *
from Fight import *
from NPC import *

class Invasion:
    def __init__(self):
        
        #Print starting screen
        print("\n\n")
        print("       !@#$%  &    !  $       /     ^       {+%#   !#}{?    =+>   &    !     ")
        print("         *    $#   @   %     }     & @     @         ^     `   -  $#   @     ")
        print("         %    % $  #    (   ?     ; - +     >&^#     %     ~   }  % $  #     ")
        print("         #    ^  ( $     = `     -     $        ~    #     *   |  ^  ( $     ")
        print("       ^*(%#  *   +$      #     *       #   )+!?   !??<+    $<[   *   +$     ")
        print("                                                                             ")
        print("\n\n\n\n\n\n")
        input("                        Press Enter to start the game                        \n                                                                             \n                                     ")
        
        #Set game variables
        self.health = 100
        self.name = ""
        self.chapter = 0
        self.finished = False
        self.chapters = [1, 2, 3, 4]
        self.companions = []
        self.inv = Inventory()

        #Give the player a small boost in the beginning
        i1 = Food("apple", 1, 15, 3)
        i2 = Food("sandwich", 3, 30, 1)
        i3 = Weapon("shotgun", 10, 25)
        self.inv.items.append(i1)
        self.inv.items.append(i2)
        self.inv.items.append(i3)
        
        #Prepare screen for game
        os.system('cls')
    
    #Method for clearing
    def clr(self):
        os.system('cls')
    
    #Getter for player status
    def is_alive(self):
        return self.alive

    #Method for displaying loading screen
    def show_loadscreen(self):
        if (os.path.isfile("savefile.txt") and not self.finished):
            print("\n\n")
            print("A savefile was found. Load this file? (yes/no)".center(80))
            result = input("                                                                             \n                                     ")
            
            #If the player wants to load a savefile:
            if result in ('y','yes'):
                #Retrieve all info from savefile.txt
                with open("savefile.txt", "r") as save_file:
                    game_state = []
                    for line in save_file:
                        values = line.split("=")
                        game_state.append({'var': values[0], 'value': values[1].rstrip()})
                    
                    #Create temporary Inventory, fill this inv with items from savefile.
                    tmp_inv = Inventory()

                    #Create temporary Companion list, fill this list with companions from savefile.
                    tmp_comps = []

                    #Load values into game
                    for entry in game_state:
                        if entry['var'] == 'name':
                            self.name = entry['value']
                        elif entry['var'] == 'health':
                            self.health = int(entry['value'])
                        elif entry['var'] == 'chapter':
                            self.chapter = int(entry['value'])
                        elif entry['var'] == 'finished':
                            if entry['value'] == 'True':
                                self.finished = True
                            else:
                                self.finished = False

                        #Loop through chapters and split where necessary
                        elif entry['var'] == 'chapters':
                            temp_arr = re.split(",", entry['value'])
                            self.chapters[:] = []
                            for item in temp_arr:
                                try:
                                    self.chapters.append(int(item))
                                except ValueError:
                                    pass
                        elif entry['var'] == 'invsize':
                            tmp_inv.size = int(entry['value'])

                        #Loop through all items in inventory and split where necessary
                        elif entry['var'] == 'items':
                            temp_items = re.split("/", entry['value'])

                            #An item can be of 3 types (Regular, food, weapon)
                            #Each one needs to be loaded differently, check for this.
                            for item in temp_items:
                                itm = re.split(",", item)
                                if itm[0] == 'w':
                                    temp_wpn = Weapon(itm[1],int(itm[2]),int(itm[3]))
                                    tmp_inv.items.append(temp_wpn)
                                elif itm[0] == 'f':
                                    temp_food = Food(itm[1], int(itm[2]), int(itm[3]), int(itm[4]))
                                    tmp_inv.items.append(temp_food)
                                elif itm[0] == 'i':
                                    temp_itm = Item(itm[1], int(itm[2]))
                                    tmp_inv.items.append(temp_itm)
                                else:
                                    pass
                            self.inv = tmp_inv

                        #Loop through all companions in list and split where necessary
                        elif entry['var'] == 'companions':
                            temp_comps = re.split("/", entry['value'])
                            for comp in temp_comps:
                                cmp = re.split(",", comp)
                                temp_cmp = Person(cmp[0],int(cmp[1]),int(cmp[2]),cmp[3],cmp[4])
                                tmp_comps.append(temp_cmp)
                            self.companions = tmp_comps
                        else:
                            pass

                    #Notify user that savefile has been loaded.
                    self.clr()
                    print("\n\n")
                    print("Your savefile was loaded.".center(80))
                    input("")
                    self.clr()
                return True

            #If the player chooses to play new game or input is incorrect:
            elif result in ('n', 'no'):
                self.clr()
                print("\n\n")
                print("No savefile was loaded.".center(80))
                input("")
                self.clr()
                return False
            else:
                self.clr()
                self.show_loadscreen()
                return True

        #Savefile doesn't exist, skip to introduction directly.
        else:
            return False

    #Method for displaying infoscreen
    def show_infoscreen(self):
        print("\n\n\n")
        tmp_name = input("What is your name?\n    ".center(80))
        while not tmp_name:
            self.clr()
            print("\n\n\n")
            tmp_name = input("What is your name?\n    ".center(80))
        self.name = tmp_name
        self.clr()

        print("\n\n\n")
        print(("Okay, " + self.name + ", welcome to this game!").center(80))
        print("")
        print(("You can always continue by pressing the Enter key. Try it!").center(80))
        input("")
        print("")
        print(("Good job, let's get started!").center(80))
        input("")
        self.clr()

    #Method for saving progress after each chapter
    def save_progress(self):
        self.clr()
        print("\n\n")
        print("Do you want to save the game at this point? (yes/no)".center(80))
        print("Note: Game can only be saved after finishing a chapter.".center(80))
        res = input("                                                                          \n                                    ")

        if res in ('y', 'yes'):
            #Clear savefile.
            open("savefile.txt", 'w').close()

            #Write new data to file.
            with open("savefile.txt", 'w') as save_file:
                save_file.write("name=" + self.name + "\n")
                save_file.write("health=" + str(self.health) + "\n")
                save_file.write("chapter=" + str(self.chapter) + "\n")
                
                #Write finished
                if self.finished == True:
                    save_file.write("finished=True\n")
                else:
                    save_file.write("finished=False\n")
                
                #Write chapters (list format)
                ch_string = ""
                try:
                    ch_string = str(self.chapters[0])
                except IndexError:
                    pass
                for i in range(1, len(self.chapters)):
                    ch_string += ("," + str(self.chapters[i]))
                save_file.write("chapters=" + ch_string + "\n")

                #Write inventory
                save_file.write("invsize=" + str(self.inv.size) + "\n")
                inv_string = ""
                item_string = ""
                for i in range(0, len(self.inv.items)):
                    item = self.inv.items[i]
                    if isinstance(item, Weapon):
                        item_string = ("w,"+item.save_wpn())
                    elif isinstance(item, Food):
                        item_string = ("f,"+item.save_food())
                    else:
                        item_string = ("i,"+item.name+","+str(item.weight)+"/")
                    inv_string += item_string
                inv_string = inv_string[:-1]
                save_file.write("items=" + inv_string + "\n")

                #Write companions
                list_string = ""
                comp_string = ""
                for i in range(0, len(self.companions)):
                    comp = self.companions[i]
                    comp_string = (comp.name+","+str(comp.health)+","+str(comp.eff)+","+comp.status+","+comp.bonus+"/")   
                    list_string += comp_string
                comp_string = comp_string[:-1]
                save_file.write("companions=" + comp_string + "\n")

        #Don't save, notify user.
        elif res in ('n', 'no'):
            self.clr()
            print("\n\n")
            print("Progress was not saved.".center(80))
            input("")
        else:
            self.clr()
            self.save_progress()

    #Method for printing option screen with 1 line of description
    def option_1(self, desc, opt):
        self.clr()
        print("\n\n\n")
        print(desc.center(80))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        result = input("     Enter command (" + opt + "): ")
        return result

    #Method for printing option screen with 2 lines of description
    def option_2(self, desc1, desc2, opt):
        self.clr()
        print("\n\n\n")
        print(desc1.center(80))
        print(desc2.center(80))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        result = input("     Enter command (" + opt + "): ")
        return result

    #Method for printing story information with 2 lines
    def story_2(self, line1, line2):
        self.clr()
        print("\n\n\n")
        print(line1.center(80))
        print(line2.center(80))

    #Method for printing story information with 3 lines
    def story_3(self, line1, line2, line3):
        self.clr()
        print("\n\n\n\n")
        print(line1.center(80))
        print(line2.center(80))
        print(line3.center(80))
        
    #Check if input is correct.
    def is_valid(self, x):
        if x in ('y', 'yes', 'n', 'no'):
            return True
        else:
            return False

    #Method for apologizing :)
    def sorry_Peter_LG(self):
        print("\n")
        print("     Unfortunately, this section has not been fully developed.")
        print("     The programmer, Daniel, had to do all of the project on his own.")
        print("")
        print("     All of the functionality and technical aspects are there,")
        print("     but the game lacks in content.")
        print("")
        print("     He sincerely apologises for this fact.")
        print("     He is going to finish this game back home (NL), when he has a lot of time.")
        print("     If the player is interested in playing the full game,")
        print("     send the programmer an email.")
        print("\n")
        input("")
        self.clr()

    #Method for introduction chapter
    def intro_chapter(self):
        print("\n\n")
        print("----- Introduction -----".center(80))
        input("")
        print("This story is set in the United States of America.".center(80))
        input("")
        print("You and Tyler are best friends.".center(80))
        input("")
        print("Together with Tyler and your brother Evan,".center(80), end="") 
        print("you are going to see a movie in the cinema.".center(80))
        print("\n\n\n\n")
        input("")
        self.clr()

        #Subchapter 0.1
        q_string = self.option_1("You are sitting in the cinema. The movie hasn't started yet.", "talk/walk/wait")
        while not(self.a_1(q_string)):
            q_string = self.option_1("You are sitting in the cinema. The movie hasn't started yet.", "talk/walk/wait")
        input("")
        self.clr()

        #Subchapter 0.2
        q_string = self.option_2("Suddenly, the lights go out and the ground starts shaking!", "Evan: Help, what is going on?!", "talk/run")
        while not(self.a_2(q_string)):
            q_string = self.option_2("Suddenly, the lights go out and the ground starts shaking!", "Evan: Help, what is going on?!", "talk/run")
        self.health -= 90
        input("")
        self.clr()

        self.chapter = 1

    #Methods for choices in intro chapter
    def a_1(self, opt):
        if opt == "talk":
            self.story_2((self.name.title() + ": Damn, this is taking long. I wish this movie would start already!"), "Tyler: Dude, be patient. It will probably start in 5 minutes.")
            return True
        elif opt == "walk":
            self.story_3((self.name.title() + ": I'm going around for a walk now, I'll be right back."), "You find a box of popcorn. After that, you walk over to the door.", "Huh? The doors are locked!")
            f1 = Food("popcorn", 2, 25, 1)
            if self.inv.fits(f1):
                self.inv.items.append(f1)
                print("\n\n")
                print("     Item ("+f1.name+") has been added to inventory.")
            else:
                print("\n\n")
                print("     Item ("+f1.name+") doesn't fit in inventory.")
            return True
        elif opt == "wait":
            self.story_2("You decide to be patient, good choice.", "After all, you are not in a rush, right?")
            return True
        else:
            return False
    def a_2(self, opt):
        if opt == "talk":
            self.story_3((self.name.title() + ": What the hell is going on?!"), "And what is that guy on the front row even doing?", "Tyler: I didn't even notice him until now. Sir. SIR! EXCUSE ME!")
            self.story_3("Alex: Hi! Do you kids have any idea what's going on?", (self.name.title() + ": No, but let's find that out later!"), "Alex: Smart idea. I'll join you guys!")
            p1 = Person("Alex", 80, 10, "good", "dmg")
            self.companions.append(p1)
            return True
        elif opt == "run":
            self.story_2((self.name.title() + ": Guys, let's get out of here ASAP."), "Tyler: Smart words, this seems unsafe!")
            return True
        else:
            return False

    #Method for mall chapter
    def mall_chapter(self):
        self.clr()
        print("\n\n")
        print("----- The Shopping Mall -----".center(80))
        input("")
        print("After a long walk, you arrive at a shopping mall.".center(80))
        input("")
        print("The mall looks abandoned.".center(80))
        input("")
        print("Tyler: We can probably find some clothing and weapons in there!".center(80)) 
        input("")
        print("However, something seems off..".center(80))
        print("\n\n\n")
        input("")
        self.clr()

        #Subchapter 2.1
        q_string = self.option_1("You enter the mall. Where do you want to go? (Left for more gameplay)", "left/right")
        while not(self.b_1(q_string)):
            q_string = self.option_1("You enter the mall. Where do you want to go? (Left for more gameplay)", "left/right")
        self.clr()

        self.chapter = 2

    #Methods for choices in mall_chapter
    def b_1(self, opt):
        if opt in ('l', 'left'):
            self.story_2("You go to the left.", "Suddenly, a mysterious figure shows up!")
            input("")
            self.clr()
            p2 = Person("Alison", 50, 10, "good", "healing")
            
            def b_1_1(opt2):
                if opt2 in ('y', 'yes'):
                    self.story_2("You slowly approach the mysterious figure.", (self.name.title() + ": Ahem. Excuse me?"))
                    input("")
                    self.story_3("The figure slowly walks towards your group.", "As the figure comes closer, you see that it is a crying woman!", "She seems very sad.")
                    input("")
                    self.story_3("Alison: C-Can you guys h-help me?", (self.name.title() + ": Yes, of course! What's going on?"), "Alison: I was j-just buying some clothes!")
                    input("")
                    self.story_3("Alison: When I went into a changing booth, everyone suddenly disappeared!", "Alison: While I was changing, I heard some loud monster-like noises.", "Evan: And did you notice the earthquake?")
                    input("")
                    self.story_3("Alison: Earthquake? No?!", "Alex: ..Something bad happened for sure.", "Tyler: Let's figure this stuff out soon.")
                    input("")
                    self.story_3("Alison: I will join your group, if that's ok.", "Alison: I used to be a nurse, maybe I can be helpful.", (self.name.title() + ": Sure, you can join us!"))
                    self.companions.append(p2)
                    return True
                elif opt2 in ('n','no'):
                    self.story_2("As your group slowly tries to walk away, Evan steps on broken glass.", "The mysterious figure turns around and charges you!")
                    input("")

                    self.clr()
                    p2.status = "evil"
                    fight = Fight(self.name, self.health, self.inv, self.companions, p2)
                    if (fight.start() == True):
                        self.finished = True
                    else:
                        self.story_2((self.name.title() + ": Wow, that was crazy!"), (self.name.title() + ": Is everyone OK?"))
                        input("")
                        alex = False
                        for ally in self.companions:
                            if ally.name == 'Alex':
                                alex = True
                                ally.health -= 80
                                if ally.health < 1:
                                    self.story_2("Evan: Oh no.. Alex.. ALEX!", "Tyler: Sorry guys, Alex is gone.")
                                    for i in range(0, len(self.companions)):
                                        if self.companions[i].name == "Alex":
                                            self.companions.pop(i)
                                else:
                                    self.story_2("Evan: Alex, are you allright?", "Alex: Well, I'm alive, but I took some serious damage.")
                                break
                        if not alex:
                            self.story_2("Evan: Yeah, I'm good.", "Tyler: I'm fine as well!")

                    return True
                else:
                    return False

            #Trigger next event.
            q_string = self.option_1("Do you approach the figure?", "yes/no")
            while not(b_1_1(q_string)):
                q_string = self.option_1("Do you approach the figure?", "yes/no")
            input("")
            self.clr()

            return True
        elif opt in ('r', 'right'):
            self.story_2("Evan: It's so dark here, I can't see anything!", "Tyler: Guys, let's check out that box over there!")
            input("")
            self.story_2((self.name.title() + ": Is that what I think it is?"), "Evan: Oh yes! A loot crate!")
            input("")
            self.clr()
            print("\n\n")
            print("     Congratulations, you found a loot crate!")
            print("     The crate contains the following items: ")
            print("     1. M16, damage: 35", end="")
            input("")
            print("     2. Knife, damage: 20", end="")
            input("")
            print("     3. Healing kit, heals: 50", end="")
            input("")
            print("")
            print("     The items that fit have been added to your inventory!")
            input("")

            i1 = Weapon("M16", 3, 35)
            i2 = Weapon("Knife", 2, 20)
            i3 = Food("Healing kit", 0, 50, 1)

            if self.inv.fits(i1):
                self.inv.items.append(i1)
            if self.inv.fits(i2):
                self.inv.items.append(i2)
            if self.inv.fits(i3):
                self.inv.items.append(i3)
            return True
        else:
            return False


    #Method for supermarket chapter
    def supermarket_chapter(self):
        self.clr()
        print("\n\n")
        print("----- The Supermarket -----".center(80))
        self.sorry_Peter_LG()

    #Method for gas station chapter
    def gas_chapter(self):
        self.clr()
        print("\n\n")
        print("----- The Gas Station -----".center(80))
        self.sorry_Peter_LG()

    #Method for chapter in the woods
    def woods_chapter(self):
        self.clr()
        print("\n\n")
        print("----- The Woods -----".center(80))
        self.sorry_Peter_LG()

    #Method for final chapter of the story
    def final_chapter(self):
        self.clr()
        print("\n\n")
        print("----- The Final Chapter -----".center(80))
        print("")
        input("")
        print("After a long journey, you finally make it to the research centre.".center(80))
        input("")
        print((self.name.title()+": Well guys, this is it. I'm going in alone.").center(80))
        input("")
        print("Evan: No, don't leave us!".center(80))
        input("")
        print((self.name.title()+": I have to, it's just too dangerous!").center(80))
        input("")

        self.story_2("As you walk through the door, the noise increases in volume.", "You slowly walk towards the sound.")
        input("")

        self.story_3("In the distance, you see a large item on the ground.", "It looks like a powerful weapon!", (self.name.title()+": Better pick it up!"))
        input("")
        print("Plasma Rifle (125) has been added to your inventory.".center(80))
        input("")
        rifle = Weapon("Plasma Rifle", 2, 125)
        if self.inv.fits(rifle):
            self.inv.items.append(rifle)
        self.story_3("You slowly open the door..", (self.name.title()+": ......."), (self.name.title()+": Oh. Shit."))
        input("")
        self.save_progress()

        self.story_2("A huge alien monster stands in the middle of the room.", "Get ready to fight!")
        input("")

        final_boss = NPC("Budalt",250,35,"evil")
        fight = Fight(self.name, self.health, self.inv, self.companions, final_boss)
        if (fight.start() == True):
            self.clr()
            print("\n\n")
            print((self.name.title()+": Ouch..! I guess this was it..").center(80))
            input("")
            self.clr()
            print("\n\n")
            print(("Too bad "+self.name.title()+", Budalt proved to be too strong for you.").center(80))
            input("")
            print("I still hope you enjoyed the game 'Invasion' by Daniel Hartgers.".center(80))
            input("")
            self.finished = True
        else:
            self.clr()
            print("\n\n")
            print((self.name.title()+": Holy shit..! I did it?!").center(80))
            input("")
            self.clr()
            print("\n\n")
            print(("Congratulations, "+self.name.title()+", you did it!").center(80))
            input("")
            print("I hope you enjoyed the game 'Invasion' by Daniel Hartgers.".center(80))
            input("")
            self.finished = True

    #Method for end screen
    def end_screen(self):
        self.clr()
        print("\n\n")
        print("       !@#$%  &    !  $       /     ^       {+%#   !#}{?    =+>   &    !     ")
        print("         *    $#   @   %     }     & @     @         ^     `   -  $#   @     ")
        print("         %    % $  #    (   ?     ; - +     >&^#     %     ~   }  % $  #     ")
        print("         #    ^  ( $     = `     -     $        ~    #     *   |  ^  ( $     ")
        print("       ^*(%#  *   +$      #     *       #   )+!?   !??<+    $<[   *   +$     ")
        print("                                                                             ")
        print("\n\n")
        print(("Dear "+self.name.title()+",").center(80))
        print("\n")
        print("Thank you for playing this game!".center(80))
        print("You can replay this game if you want to,".center(80))
        print("there is probably a lot more to explore!".center(80))    
        input("")
    
    #Main method for running the game    
    def start(self):
        #Check for savefiles.
        if not (self.show_loadscreen()):
            self.show_infoscreen()