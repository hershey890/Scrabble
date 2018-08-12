# Module Game.py


import Display
import Board
import Defaults
import Player

class Game:

    newDefault = Defaults()

    def __init__(self, width: int, height: int = newDefault.height, players: int = newDefault.player):



        if not (isinstance(width, int) and isinstance(height, int) and isinstance(players, int)):
            raise TypeError
        elif width <=0 and height <= 0:
            raise ArithmeticError

        # Set all values in the board to default
        newBoard = Board(width, height)
        # Create default display
        newDisplay = Display(width, height)

        if players < 2 and players > 4:
            pass # newDisplay.display_prompt("asad")

    def game_init_prompt(self):
        pass