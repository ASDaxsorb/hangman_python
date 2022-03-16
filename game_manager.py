import time
import random
from constants import MENU, HANGMANFRAMES
from utils import clear_terminal


class GameManager:
    def __init__(self):
        self.score = 0
        self.load_words()
        self.start_menu()
        self.set_values()

    def load_words(self):
        try:
            with open("./data/data.txt", "r", encoding="utf-8") as file:
                self.words = list(map(lambda w: w.strip(), file))

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
        self.set_values()

    def game_loop(self):
        while self.missed < len(HANGMANFRAMES) - 1:
            self.render_game(self.score, "".join(self.hidden_word).upper())
            self.input_letter()
            clear_terminal()
        else:
            self.game_over()

    def render_game(self, score, word):
        print(f"Score:{score}\n\n")
        print(HANGMANFRAMES[self.missed])
        print(f"\n\nWord: {word}\n")

    def input_letter(self):
        letter = input("Input a letter: ").lower().strip()
        for i, (key, value) in enumerate(self.letters.items()):
            was_found = letter == value
            if was_found:
                self.hidden_word[key] = letter
                self.letters.pop(key)
                break

        if not was_found:
            self.add_missed()
        elif self.is_correct_answer():
            self.won()

    def hide_word(self):

        hidden_word = []
        letters = {}
        for index, letter in enumerate(self.current_word):
            number = random.randint(0, 2)
            if number == 2:
                hidden_word.append("_")
                letters[index] = letter
            elif number == 1:
                hidden_word.append("_")
                letters[index] = letter
            else:
                hidden_word.append(letter)

        return hidden_word, letters

    def set_values(self):
        self.current_word = self.take_random_word()
        self.hidden_word = ""
        self.letters = {}
        self.missed = 0
        while self.hidden_word.count("_") == 0:
            self.hidden_word, self.letters = self.hide_word()

    def is_correct_answer(self):
        return "".join(self.hidden_word).lower() == self.current_word.lower()

    def won(self):
        clear_terminal()
        self.score += 100
        print(f"score {self.score}\n\n")
        print("Correct!")
        print(self.current_word.capitalize())
        self.set_values()
        time.sleep(2)

    def game_over(self):
        clear_terminal()
        print("Game Over :(\n")
        print(HANGMANFRAMES[len(HANGMANFRAMES) - 1])
        print(f"Youre score: {self.score}")
        time.sleep(2)
        self.start_menu()

    def add_missed(self):
        self.missed += 1
