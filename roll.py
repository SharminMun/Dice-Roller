# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

import random

def dice_roll(numOftimes):
    playAgain = "Y"
    while playAgain == "Y":
        for dice in range(1, numOftimes+1):  
            print(random.randint(1,6))
        print("Would you like to roll the dice again?")
        playAgain = input("Please enter Y for Yes, or Type anything else to quit the game:")

dice_roll(3)