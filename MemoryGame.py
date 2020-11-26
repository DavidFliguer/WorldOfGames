from Common import ask_for_numeric_input
from Game import Game
import random
import os, platform
import time

# those 2 methods can be also in common file (or, in utils file)
def is_list_equal(user_list, system_list):
    return user_list == system_list


def clear_output():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')


class MemoryGame(Game):

    def generate_sequence(self):
        system_list = []
        for x in range(self.difficulty):
            system_list.append(random.randint(1, 101))
        return system_list

    def get_list_from_user(self):
        user_list = []
        for x in range(self.difficulty):
            guess = ask_for_numeric_input("Add a number to the list", 1, 101)
            user_list.append(guess)
        return user_list

    def play(self):
        system_list = self.generate_sequence()
        print(system_list)
        time.sleep(0.7)
        clear_output()
        user_list = self.get_list_from_user()
        return is_list_equal(user_list, system_list)
    # user_input = self.get_guess_from_user()
    # return self.compare_results(user_input)
