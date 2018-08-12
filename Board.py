# Module Board.py
# stores all the values of currently in the board

import Display

class Board:

    def __init__(self, width: int, height: int):
        if not (isinstance(width, int) and isinstance(height, int)):
            return TypeError


    self.board = [['.' for x in range(width)] for y in range(height)]