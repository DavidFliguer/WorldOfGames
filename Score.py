from Utils import SCORES_FILE_NAME
import os


def get_current_score():
    answer = 0
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as f:
            answer = f.read()
    return int(answer)


def add_score(difficulty):
    points_to_add = (difficulty * 3) + 5
    score_to_update = get_current_score() + points_to_add

    with open(SCORES_FILE_NAME, 'w') as f:
        f.write(str(score_to_update))
