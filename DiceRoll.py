import random
import sys

#player = input("""Press Y to roll the dices or
    #Press N to exit: """)
player = "y".lower()
while player.lower() == "y":
    player = input("""Press Y to roll the dices or
        Press N to exit: """)
    if player.lower() == "y":

        dice_1 = random.choice(range(1,7))
        dice_2 = random.choice(range(1,7))


        print(dice_1,dice_2)


    elif player.lower() == "n":

        print("Have a good day")
        sys.exit()
