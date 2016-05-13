import os
import time

debug = False

class Invasion():
    def __init__(self):
        
        #Print starting screen
        print("\n\n")
        print("    !@#$%  &    !      V     A       S      I        O     N                   ")
        print("      *    $#   @                                                              ")
        print("      %    % $  #                                                              ")
        print("      #    ^  ( $                                                              ")
        print("    ^*(%#  *   +$                                                              ")
        print("                                                                               ")
        print("\n\n")
        input("                        Press Enter to start the game                        \n                                                                             \n                                     ")
        
        #Set game variables
        self.alive = True
        self.health = 100
        self.name = ""
        self.chapter = ""
        
        #Prepare screen for game
        os.system('cls')
    
    #Method for delay/clearing
    def wait(self, t):
        if not debug:
            time.sleep(t)

    def clr(self):
        os.system('cls')
    
    #Getter for player status
    def is_alive(self):
        return self.alive

    #Move flashing dash on screen
    def clr_dash(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

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
        self.clr_dash()
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
        print("\n\n\n")
        print(line1.center(80))
        print(line2.center(80))
        print(line3.center(80))

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
            return True
        elif opt == "run":
            self.story_2((self.name.title() + ": Guys, let's get out of here ASAP."), "Tyler: Smart words, this seems unsafe!")
            return True
        else:
            return False

    #Method for chapter 1
    def chapter_a(self):
        print("\n\n")
        print("-- Chapter 1 --".center(80))
        print("\n")
        self.wait(5)
        print("This story is set in the United States of America.\n".center(80))
        self.wait(3)
        print("You and Tyler are best friends.\n".center(80))
        self.wait(3)
        print("Together with Tyler and your brother Evan,".center(80), end="") 
        print("you are going to see a movie in the cinema.\n".center(80))
        print("\n\n\n\n\n\n\n\n")
        input("")
        self.clr()

        #Subchapter a_1
        self.chapter = "a_1"
        q_string = self.option_1("You are sitting in the cinema. The movie hasn't started yet.", "talk/walk/wait")
        while not(self.a_1(q_string)):
            q_string = self.option_1("You are sitting in the cinema. The movie hasn't started yet.", "talk/walk/wait")
        self.clr_dash()
        input("")

        #Subchapter a_1
        self.chapter = "a_2"
        q_string = self.option_2("Suddenly, the lights go out and the ground starts shaking!", "Evan: Help, what is going on?!", "talk/run")
        while not(self.a_2(q_string)):
            q_string = self.option_2("Suddenly, the lights go out and the ground starts shaking!", "Evan: Help, what is going on?!", "talk/run")
        self.clr_dash()
        input("")


    
    #Main method for running the game    
    def start(self):
        #Check for savefiles.
        if not (self.show_loadscreen()):
            if not debug:
                self.show_infoscreen()
            else:
                self.name = "Daniel"

        #Continue.
        self.chapter_a()