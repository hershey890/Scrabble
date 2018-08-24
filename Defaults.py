# Default.py
# stores all the default values

if __name__ == "__main__":
    import os
    raise ImportError("Do not run {0}".format(os.path.basename(__file__)))
else:
    class Defaults:

        # Default board size
        width = 15
        height = 15

        # default number of letters given to each player
        letters = 7

        players = 2
