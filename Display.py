# Module Display.py
# Displays the scrabble board
# Eventually integrate tinkerpy or whatever to build a gui


import os

if __name__ == "__main__":

    print("Do not run {0}".format(os.path.basename(__file__)))
    raise ImportError
else:
    class Display:

        letters = ['_', '_', '_', '_', '_', '_', '_']

        def __init__(self, width: int, height: int):
            if not (isinstance(width, int) and isinstance(height, int)):
                raise TypeError("Error: Not a integer")
            elif width <= 0 or height <= 0:
                raise ValueError("Error: Not a positive number")
            self.width = width
            self.height = height
            self.board = [['.' for x in range(width)] for y in range(height)]

            # print("     _______.  ______ .______          ___      .______   .______    __       _______ \n" \
            #       .center(os.get_terminal_size().columns))
            # print("    /       | /      ||   _  \        /   \     |   _  \  |   _  \  |  |     |   ____|\n" \
            #       .center(os.get_terminal_size().columns))
            # print("   |   (----`|  ,----'|  |_)  |      /  ^  \    |  |_)  | |  |_)  | |  |     |  |__   \n" \
            #       .center(os.get_terminal_size().columns))
            # print("    \   \    |  |     |      /      /  /_\  \   |   _  <  |   _  <  |  |     |   __|  \n" \
            #       .center(os.get_terminal_size().columns))
            # print(".----)   |   |  `----.|  |\  \----./  _____  \  |  |_)  | |  |_)  | |  `----.|  |____ \n" \
            #       .center(os.get_terminal_size().columns))
            # print("|_______/     \______|| _| `._____/__/     \__\ |______/  |______/  |_______||_______|\n" \
            #       .center(os.get_terminal_size().columns))

            print("""\
                 _______.  ______ .______          ___      .______   .______    __       _______
                /       | /      ||   _  \        /   \     |   _  \  |   _  \  |  |     |   ____|
               |   (----`|  ,----'|  |_)  |      /  ^  \    |  |_)  | |  |_)  | |  |     |  |__   
                \   \    |  |     |      /      /  /_\  \   |   _  <  |   _  <  |  |     |   __|  
            .----)   |   |  `----.|  |\  \----./  _____  \  |  |_)  | |  |_)  | |  `----.|  |____ 
            |_______/     \______|| _| `._____/__/     \__\ |______/  |______/  |_______||_______|
            """.center(os.get_terminal_size().columns))
            print("\n\n\nPress Enter the number of players to begin (must be 1-3)".center(os.get_terminal_size().columns))


        def dislay_init(self, width: int, height: int):
            pass

        def display_board(self): # -> bool:
            """Displays the board"""
            if not (isinstance(self.width, int) and isinstance(self.height, int)):
                raise TypeError
                # should I put a return false here?
            for y in range(self.height):
                for x in range(self.width):
                    print(". ")
                print(" ")

        def set_board(self, x_coord: int, y_coord: int):
            if not (isinstance(x_coord, int) and isinstance(y_coord, int)):
                raise TypeError
            elif x_coord < 0 or y_coord < 0:
                raise ArithmeticError


        def display_letters(self, letters) -> int:
            pass # implement later

        def display_prompt(self, prompt: str):
            if not isinstance(prompt, str):
                raise TypeError
