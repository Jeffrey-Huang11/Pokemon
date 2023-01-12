# Simulation for game
from pip import main

import game_logic.battle


def play(p1, p2):
    move = input("Choose your move:")
    atk(move, p1, p2)





# main function 
def main():
    print("Choose your pokemon!")

    p1 = input()
    print("Choose your rival!")

    p2 = input()
    play()

  


