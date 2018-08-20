# Module Player.py
# Receives player input

if __name__ == "__main__":
    import os
    print("Do not run {0}".format(os.path.basename(__file__)))
    raise ImportError
else:
    class Player:

        def get_init_input(self, prompt: str = "") -> str:
            user_input = input(prompt)
            return user_input

        def get_user_word(self) -> str:
            pass

