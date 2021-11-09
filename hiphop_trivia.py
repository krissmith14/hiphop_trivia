"""
hiphop_trivia.py
music trivia application as python fundamentals project
utilizing defined functions, loops, data sets, modules, and
data sets
"""

from trivia_pkg.functions import ask_question


def main():
    user_option = input("""Welcome to Hip Hop Trivia! Would you like to play?
    Type 'yes' to continue, type 'no' to quit: """)

    while True:
        if user_option.lower() == "yes":
            user_name = input("Please type in your name: ")
            print(f"Hi {user_name}!")
            break
        if user_option.lower() == "no":
            print("Maybe next time!")
            quit()
    input("Get ready for your first question! Press ENTER to continue.")

    total_score = 0
    num_tries = 0

    while num_tries < 3:
        print(total_score)
        ask_question()

        if ask_question is True:
            total_score += 5
            input("That's correct! Press ENTER to continue.")

        if ask_question is False:
            num_tries += 1
            print("The correct answer is: ", ask_question)
            input("Press ENTER to continue.")

    again = input("Sorry! You lose! Play Again?: ")
    if again == "yes":
        main()
    else:
        quit()


main()
