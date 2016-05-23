import os
import time
from Person import *

class Invasion():
    def __init__(self):

        #Variable for easy debugging.
        self.debug = True
        
        #Print starting screen
        print("\n\n")
        print("       !@#$%  &    !  $       /     ^       {+%#   AAAAA    AAA   &    !     ")
        print("         *    $#   @   %     }     & @     @         A     A   A  $#   @     ")
        print("         %    % $  #    (   ?     ; - +     >&^#     A     A   A  % $  #     ")
        print("         #    ^  ( $     = `     -     $        ~    A     A   A  ^  ( $     ")
        print("       ^*(%#  *   +$      #     *       #   )+!?   AAAAA    AAA   *   +$     ")
        print("                                                                             ")
        print("\n\n\n\n\n\n")
        input("                        Press Enter to start the game                        \n                                                                             \n                                     ")
        
        #Set game variables
        self.health = 100
        self.name = ""
        self.chapter = ""
        self.finished = False
        self.chapters = [1, 2, 3, 4]
        self.companions = []
        
        #Prepare screen for game
        os.system('cls')
    
    #Method for delay/clearing
    def wait(self, t):
        if not self.debug:
            time.sleep(t)

    def clr(self):
        os.system('cls')
    
    #Getter for player status
    def is_alive(self):
        return self.alive

    #Method for displaying loading screen
    def show_loadscreen(self):
        if (os.path.isfile("savefile.txt")):
            result = input("A savefile was found. Load this file? (y/n)")
            if result == 'y':
                print("yes!")
            elif result == 'n':
                print("no!")
            else:
                print("incorrect input")
            return True
        else:
            return False

    #Method for displaying infoscreen
    def show_infoscreen(self):
        print("\n\n\n")
        self.name = input("What is your name?\n    ".center(80))
        self.clr()

        print("\n\n\n")
        print(("Okay, " + self.name + ", welcome to this game!").center(80))
        self.wait(2)
        self.clr()

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

    #Method for introduction chapter
    def intro_chapter(self):
        print("\n\n")
        print("----- Introduction -----".center(80))
        print("\n")
        self.wait(5)
        print("This story is set in the United States of America.".center(80))
        print("\n")
        self.wait(3)
        print("You and Tyler are best friends.".center(80))
        print("\n")
        self.wait(3)
        print("Together with Tyler and your brother Evan,".center(80), end="") 
        print("you are going to see a movie in the cinema.".center(80))
        print("\n\n\n\n\n")
        input("")
        self.clr()

        #Subchapter a_1
        self.chapter = "a_1"
        q_string = self.option_1("You are sitting in the cinema. The movie hasn't started yet.", "talk/walk/wait")
        while not(self.a_1(q_string)):
            q_string = self.option_1("You are sitting in the cinema. The movie hasn't started yet.", "talk/walk/wait")
        input("")
        self.clr()

        #Subchapter a_1
        self.chapter = "a_2"
        q_string = self.option_2("Suddenly, the lights go out and the ground starts shaking!", "Evan: Help, what is going on?!", "talk/run")
        while not(self.a_2(q_string)):
            q_string = self.option_2("Suddenly, the lights go out and the ground starts shaking!", "Evan: Help, what is going on?!", "talk/run")
        self.health -= 90
        input("")
        self.clr()

    #Method for mall chapter
    def mall_chapter(self):
        print("\n\n")
        print("----- The Shopping Mall -----".center(80))
        print("\n")
        self.wait(5)
        print("After a long walk, you arrive at a shopping mall.".center(80))
        print("\n")
        self.wait(3)
        print("The mall looks abandoned.".center(80))
        print("\n")
        self.wait(3)
        print("Tyler: We can probably find some clothing and weapons in there!".center(80)) 
        print("\n")
        self.wait(3)
        print("However, something seems off..".center(80))
        print("\n\n\n")
        input("")
        self.clr()

    #Method for supermarket chapter
    def supermarket_chapter(self):
        print("\n\n")
        print("----- The Supermarket -----".center(80))
        print("\n")
        self.wait(5)
        print("".center(80))
        print("\n")
        self.wait(3)
        print("".center(80))
        print("\n")
        self.wait(3)
        print("".center(80)) 
        print("\n")
        self.wait(3)
        print("".center(80))
        print("\n\n\n")
        input("")
        self.clr()

    #Method for gas station chapter
    def gas_chapter(self):
        print("\n\n")
        print("----- The Gas Station -----".center(80))
        print("\n")
        self.wait(5)
        print("".center(80))
        print("\n")
        self.wait(3)
        print("".center(80))
        print("\n")
        self.wait(3)
        print("".center(80)) 
        print("\n")
        self.wait(3)
        print("".center(80))
        print("\n\n\n")
        input("")
        self.clr()

    #Method for chapter in the woods
    def woods_chapter(self):
        print("\n\n")
        print("----- The Woods -----".center(80))
        print("\n")
        self.wait(5)
        print("".center(80))
        print("\n")
        self.wait(3)
        print("".center(80))
        print("\n")
        self.wait(3)
        print("".center(80)) 
        print("\n")
        self.wait(3)
        print("".center(80))
        print("\n\n\n")
        input("")
        self.clr()

    #Method for final chapter of the story
    def final_chapter(self):
        self.finished = True

    #Methods for each choice in storyline
    def a_1(self, opt):
        if opt == "talk":
            self.story_2((self.name.title() + ": Damn, this is taking long. I wish this movie would start already!"), "Tyler: Dude, be patient. It will probably start in 5 minutes.")
            return True
        elif opt == "walk":
            self.story_3((self.name.title() + ": I'm going around for a walk now, I'll be right back."), "You walk over to the double doors of the cinema.", "Huh? The doors are locked!")
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
            p1 = Person("Alex", 80, "good", "dmg")
            self.companions.append(p1)
            return True
        elif opt == "run":
            self.story_2((self.name.title() + ": Guys, let's get out of here ASAP."), "Tyler: Smart words, this seems unsafe!")
            return True
        else:
            return False
    
    
    #Main method for running the game    
    def start(self):
        #Check for savefiles.
        if not (self.show_loadscreen()):
            if not self.debug:
                self.show_infoscreen()
            else:
                self.name = "Daniel"