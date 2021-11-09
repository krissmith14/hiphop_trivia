"""
functions.py
"""

import random
from trivia_pkg.questions import trivia_questions
import copy


def ask_question():
    print()
    question_2= list(trivia_questions)
    question = random.choice(list(trivia_questions))
    print(question)
    player_answer = input("Answer: ")
    answer = trivia_questions[question].lower()
    del trivia_questions[question]
    if player_answer == answer:
        return True, answer
    if not trivia_questions:
        print("You win")
    return False, answer


# put question in a separate fx
# take question bank and 