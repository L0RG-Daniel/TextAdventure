import Invasion as adv
import random

#Start a new adventure
game = adv.Invasion()
game.start()

#Check if the player is still alive and well
while not game.finished:

    game.save_progress()

    #Only run intro chapter on new game.
    if not (game.chapter > 0):
        game.intro_chapter()
    else:
        #Choose a random new chapter out of the remaining chapters.
        if len(game.chapters) > 0:
            next_ch = random.choice(game.chapters)
        
            #Run the next random chapter.
            if next_ch == 4:
                game.woods_chapter()
            elif next_ch == 3:
                game.gas_chapter()
            elif next_ch == 2:
                game.supermarket_chapter()
            else:
                game.mall_chapter()

            #Remove played chapter from the list.
            game.chapters.remove(next_ch)
        else:
            #Run the final chapter of the game.
            game.final_chapter()

#Game is now finished.
game.clr()
print("GAME DONE MF")