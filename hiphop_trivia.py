"""
hiphop_trivia.py
music trivia application as python fundamentals project
utilizing defined functions, loops, data sets, modules, and
data sets
"""

import random

trivia_questions = {"What is the name of Snoop Dogs first Album?": "Doggy Style", "Where did Lauryn Hill attend college before dropping out to pursue her music career full time?":
                    "Columbia University", "What was the name of the record label founded by Suge Knight, Dr. Dre, The D.O.C., and Dick Griffey?": "Death Row Records", "Who was the first hip-hop group to get a star on the Hollywood Walk of Fame?": "Cypress Hill"}

# def ask_question():
#     question = random.choice(list(trivia_questions))
#     print(question)
#     answer = trivia_questions[question]
#     player_answer = input("Answer: ")
#     if player_answer.lower() == answer.lower():
#         return True
#     if player_answer.lower() == answer.lower():
#         return False


def main():
    user_option = input("""Welcome to Hip Hop Trivia! Would you like to play?
    Type 'yes' to continue, type 'no' to quit: """)
    num_tries = 0
    total_score = 0
    while True:
        if user_option.lower() == "yes":
            user_name = input("Please type in your name: ")
            print(f"Hi {user_name}!")
            break
        if user_option.lower() == "no":
                print("Maybe next time!")
                quit()
    input("Get ready for your first question! Press ENTER to continue.")
    while True:
        while num_tries < 3:
            print(total_score)
            question = random.choice(list(trivia_questions))
            print(question)
            answer = trivia_questions[question].lower()
            del trivia_questions[question]
            player_answer = input("Answer: ")
            if player_answer.lower() == answer:
                total_score += 5
                input("That's correct! Press ENTER to continue.")
            elif player_answer.lower() != answer:
                num_tries += 1
                print("Wrong! The answer is:", answer)
                input("Press ENTER to continue.")
            if not trivia_questions:
                print(total_score)
                print("You win!")
                quit()
        again = input("Sorry! You lose! Play Again?: ")
        if again =="yes":
            main()
        else:
            quit()

main()












            # if ask_question is True:
            #     total_score += 1
            #     print(total_score)
            #     while questions.trivia_questions:
            #         ask_question()
            #     if not questions.trivia_questions:
            #         print("No more")
            # if user_option.lower() == "no":
            #     print("Maybe next time!")
            #     quit()

    # def ask_question():
    #     question = random.choice(list(questions.trivia_questions))
    #     print(question)
    #     answer = questions.trivia_questions[question].lower()
    #     player_answer = input("Answer: ")
    #     if player_answer.lower() == answer:
    #         return True
    #     if player_answer != answer:
    #         return False

    # while num_tries < 3:
    #     if ask_question() == True and total_score <= 50:
    #         total_score += 5
    #         print("Score: ", total_score)
    #     ask_question()
    #     if total_score == 50:
    #         print("Congrats! You win!")
    #     if ask_question() == False and num_tries < 3:
    #         num_tries += 1
    #     ask_question()




