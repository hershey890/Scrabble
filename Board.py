# Module Board.py
# stores all the values of currently in the board

import Display

if __name__ == "__main__":
    import os
    print("Do not run {0}".format(os.path.basename(__file__)))
    raise ImportError
else:
    class Board:

        def __init__(self, width: int, height: int):
            if not (isinstance(width, int) and isinstance(height, int)):
                raise TypeError("Error: Not a integer")
            elif width <= 0 or height <= 0:
                raise ValueError("Error: Not a positive number")


        # self.board = [['.' for x in range(width)] for y in range(height)]