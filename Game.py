# Module Game.py


import Display
import Board
import Defaults
import Player
import sys


if __name__ == "__main__":
    import os
    raise ImportError("Do not run {0}".format(os.path.basename(__file__)))
else:
    class Game:

        newDefault = Defaults()

        def __init__(self, width: int, height: int = newDefault.height, players: int = newDefault.player):

            # if not (isinstance(width, int) and isinstance(height, int)):
                # raise TypeError("Error: Not a integer")
            # elif width <= 0 or height <= 0:
                # raise ValueError("Error: Not a positive number")

            try:
                # Set all values in the board to default
                newBoard = Board(width, height)
                # Create default display
                newDisplay = Display(width, height)
            except TypeError as error:
                print(error)
                # make the user enter a valid value
                pass
            except ValueError as error:
                print(error)
                # make the user enter a valid value
                pass

            while(1):
                num_players = int(input())
                if num_players >= 1 and num_players <= 4:
                    nonlocal num_players
                    break
                else:
                    pass # replace with something that deletes the user input and asks for a new input

            if num_players > 1:
                # how would the scoping work here?
                player_list = []
                for counter in range(num_players):
                    player_list.append(Player())
                # newPlayer = Player()