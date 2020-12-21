from Utils import SCORES_FILE_NAME
import os


def get_current_score():
    """
    Gets the current score (Which is the value of the Scores.txt file)

    If there is no file, returns 0
    """
    # Initialize 0
    answer = 0

    # Verify if the file exists, if it exists then read the content (That is the score)
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as f:
            answer = f.read()
    return int(answer)


def add_score(difficulty):
    """
        Updates (Or creates) the score file with the new score of the recently played game
    """
    # Calculate the points to add
    points_to_add = (difficulty * 3) + 5

    # Calculate the score that needs to be "overriden" in the file
    score_to_update = get_current_score() + points_to_add

    # Override (In case file does not exists, it creates it)
    with open(SCORES_FILE_NAME, 'w') as f:
        f.write(str(score_to_update))
