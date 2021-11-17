"""
functions.py
"""

import random
from trivia_pkg.questions import trivia_questions
import copy


def question_ask():
    
    # make a deep copy of the list of trivia_questions
    questions_list = copy.deepcopy(trivia_questions)
    print()

    # select random key from the copy of the trivia_questions
    player_question = random.choice(list(questions_list))

    # Print the key
    print(player_question)

    # return the value of the key
    answer = questions_list[player_question].lower()
    return answer



def check_answer(player_answer, answer):

    if player_answer == answer:
        return True

    return False



