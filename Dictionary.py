# Module Dictionary
# Opens dictionary and stores within a hashtable for rapid access
# Used to check if a word is valid ass well

if __name__ == "__main__":
    import os
    raise ImportError("Do not run {0}".format(os.path.basename(__file__)))
else:
    class Dictionary:

        def __init__(self):
            with open('words.txt', 'r') as dictionary:
                read_data = dictionary.read()
                # add all the hashing stuff in here
                # also remove all the words with non-alphabetical characters
            dictionary.close()