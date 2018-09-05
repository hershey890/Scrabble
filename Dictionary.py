# Module Dictionary
# Opens dictionary and stores within a hashtable for rapid access
# Used to check if a word is valid ass well

# exclude words with: non-lower case alphabetical characters

if __name__ == "__main__":
    import os
    raise ImportError("Do not run {0}".format(os.path.basename(__file__)))
else:
    from collections import defaultdict
    from inspect import currentframe

    def get_linenumber():
        cf = currentframe()
        return cf.f_back.f_lineno

    def is_valid_word(line: str) -> bool:  # causing issue, I think it is always returning false
        for letter in line:
            if letter < 'a' or letter > 'z':
                return False
        return True

    def to_prime(letter: str) -> int:
        if letter < 'a' or letter > 'z':
            raise ValueError
        if letter == 'a':
            return 2
        elif letter == 'b':
            return 3
        elif letter == 'c':
            return 5
        elif letter == 'd':
            return 7
        elif letter == 'e':
            return 11
        elif letter == 'f':
            return 13
        elif letter == 'g':
            return 17
        elif letter == 'h':
            return 19
        elif letter == 'i':
            return 23
        elif letter == 'j':
            return 29
        elif letter == 'k':
            return 31
        elif letter == 'l':
            return 37
        elif letter == 'm':
            return 41
        elif letter == 'n':
            return 43
        elif letter == 'o':
            return 47
        elif letter == 'p':
            return 53
        elif letter == 'q':
            return 59
        elif letter == 'r':
            return 61
        elif letter == 's':
            return 67
        elif letter == 't':
            return 71
        elif letter == 'u':
            return 73
        elif letter == 'v':
            return 79
        elif letter == 'w':
            return 83
        elif letter == 'x':
            return 89
        elif letter == 'y':
            return 97
        elif letter == 'z':
            return 101

    def hash_func(word: str, num_words: int) -> int:
        hash_key = 1
        for letter in word:
            hash_key *= to_prime(letter)
        hash_key %= num_words
        return hash_key


    class Dictionary:

        def __init__(self, file='words.txt'):
            self.file = file
            with open(file, 'r') as dictionary:

                # Find Number of Words in the Dictionary
                self.num_words = 0
                for line in dictionary:
                    line = line.strip()
                    if is_valid_word(line):
                        self.num_words += 1
                del line

                # resets the file pointer to the start of the file
                dictionary.seek(0)
                self.dict_list = defaultdict(list)
                for line in dictionary:
                    line = line.strip()  # removes trailing whitespace
                    if is_valid_word(line):
                        key = hash_func(line, self.num_words)
                        self.dict_list[key].append(line)

        def is_real_word(self, input_word: str) -> bool:
            input_word = input_word.lower().strip()
            if is_valid_word(input_word):
                key = hash_func(input_word, self.num_words)
                for dict_word in self.dict_list[key]:
                    if dict_word == input_word:
                        return True
                return False

        # --------------------- Testing functions --------------------- #
        def get_word(self, index: int) -> str:
            with open(self.file, 'r') as dictionary:
                line = ""
                i = 0
                for line in dictionary:
                    if not is_valid_word(line.strip()):
                        continue
                    if i == index:
                        break
                    i += 1
                return line.strip()

        def get_word2(self, index: int):
            return self.dict_list[index]
