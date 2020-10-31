import Common


def welcome(name):
    """
    This function has a person name as an input and returns a string in the following layout:

    :param name: The person name
    :return: A formatted string
    """

    return """Hello {} and welcome to the World of Games (WoG).
        Here you can find many cool games to play.""".format(name)


def load_game():
    """
        This function asks the user for input for the game and difficulty
        NOTE: According to assignment it does not return anything but seems to me that should return the user selection to use it in the main (See TODO)
    """

    choose_game_text = """Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS"""
    choose_game_difficulty_text = """Please choose game difficulty from 1 to 5:"""

    chosen_game = Common.ask_for_numeric_input(choose_game_text, 1, 3)
    chosen_difficulty = Common.ask_for_numeric_input(choose_game_difficulty_text, 1, 5)
    #TODO: Shouldn't this return the selection ?