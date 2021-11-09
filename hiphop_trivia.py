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
# below loop needs to be the child wild loop 
    while num_tries < 3:
        print(total_score)
        # create separate fx get_questions, returning the question bank
        # use copy.deepcopy to copy question bank
        answer_bool, answer = ask_question()
        

        if answer_bool is True:
            total_score += 5
            input("That's correct! Press ENTER to continue.")

        else:
            num_tries += 1
            print("The correct answer is: ", answer)
            input("Press ENTER to continue.")

    again = input("Sorry! You lose! Play Again?: ")
    if again == "yes":
        main()
    else:
        quit()


main()
