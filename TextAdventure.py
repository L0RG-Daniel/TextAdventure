import Invasion as adv

#Start a new adventure
game = adv.Invasion()
game.start()

#Check if the player is still alive and well
while (game.health > 0 and game.finished == False):
    if game.intro_chapter() == True:
        game.mall_chapter()
        #Randomly decide one of the four chapters
    game.final_chapter()

game.clr()
print("GAME DONE MF")