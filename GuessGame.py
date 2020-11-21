from Common import ask_for_numeric_input
from Game import Game
import random


class GuessGame(Game):

    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.secret_number = self.generate_number()

    def generate_number(self):
        return random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        user_input = ask_for_numeric_input("Make your guess", 1, self.difficulty)
        return user_input

    def compare_results(self, user_input):
        return user_input == self.secret_number

    def play(self):
        user_input = self.get_guess_from_user()
        return self.compare_results(user_input)
