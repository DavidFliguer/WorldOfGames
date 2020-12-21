import requests
import random

from Utils import ask_for_numeric_input, EXCHANGE_API_URL
from Game import Game


class CurrencyRouletteGame(Game):

    def __init__(self, difficulty):
        super().__init__(difficulty)
        self.random_number = random.randint(1, 100)

    def get_money_interval(self):
        # I would move the url as a class const value
        rates = requests.get(EXCHANGE_API_URL).json()
        rate = rates['rates']['ILS']
        converted = int(self.random_number * rate)
        return range(converted - (5 - self.difficulty), converted + (5 - self.difficulty))

    def get_guess_from_user(self):
        return ask_for_numeric_input("Guess (approximately) how much ILS is " + str(self.random_number) + " USD (now)")

    def play(self):
        user_guess = self.get_guess_from_user()
        return user_guess in self.get_money_interval()
