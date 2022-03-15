from pydoc import render_doc
import random
from constants import MENU
from utils import clear_terminal


class GameManager:
    current_word = ""

    def __init__(self):
        self.start_menu()

    def load_words(self):
        try:
            with open("./data/data.txt", "r", encoding="utf-8") as file:
                self.words = [word.strip() for word in file]
        except:
            print("Cant load data")

    def take_random_word(self):
        list_length = len(self.words)
        if list_length > 0:
            index = random.randint(0, list_length)

        return self.words.pop(index)

    def start_menu(self):
        try:
            option = int(input(MENU))
            clear_terminal()

            if option == 1:
                self.start_game()
                self.game_loop()
            elif option == 2:
                exit()

        except ValueError:
            print("Please input a valid option")

    def start_game(self):
        self.score = 0
        self.load_words()
        self.current_word = self.take_random_word()

    def game_loop(self):
        while True:
            self.render_game(self.score, "co_f__")
            self.input_letter()
            clear_terminal()

    def render_game(self, score, word):
        render = f"""
        Score: {score}
        {word}
        """.strip()
        print(render)

    def input_letter(self):
        letter = input("Input a letter: ")
