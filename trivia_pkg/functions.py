"""
functions.py
"""

import random
from trivia_pkg.questions import trivia_questions


def ask_question():
    print()
    question = random.choice(list(trivia_questions))
    print(question)
    player_answer = input("Answer: ")
    answer = trivia_questions[question].lower()
    del trivia_questions[question]
    if player_answer == answer:
        return True
    if not trivia_questions:
        print("You win")
    return False, answer