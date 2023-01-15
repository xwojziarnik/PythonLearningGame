import random

from additional_info.dict_methods import dict_methods
from additional_info.int_float_bool_methods import int_bool_methods, float_methods
from additional_info.list_methods import list_methods
from additional_info.set_methods import set_method
from additional_info.string_methods import string_methods
from additional_info.tuple_methods import tuple_methods


def game():
    """
    Bash game where user can learn about methods based on Python types.

    Game has two modes:
        - learn (infinite loop):
            Choose subject get randomly chosen method and try to answer.
            User can skip to next method, get description of method or exit.

        - play game:
            Choose subject and try to answer ten questions based methods in selected subject.
            For every correct answer user is getting one point. After collecting 10 points user is winning the game.
    """
    # VARIABLES
    subject = None
    interlude = "-" * 40
    number_of_question = 1
    points = 0

    # intro
    print(interlude)
    print(">>>>> Hello in an exercise game! <<<<<".center(40))
    print(interlude)
    player = input("Write down your name: ")
    player = player.title()
    print(interlude)

    # choose version of game
    print(
        f"Welcome in the game {player}! What do you want to do?\nLearn: type 'a'\nPlay game: type 'b'"
    )
    learn_or_play = input("Your choice: ")
    print(interlude)

    # validating choice
    while learn_or_play.upper() not in "AB":
        learn_or_play = input(
            "Bad answer! You have to choose from 'a' (which stands for learning)\nor 'b' (which stands for "
            "playing game).\nRemember to type letter a or b without quotes!\nChoice: "
        )
        print(interlude)

    if learn_or_play.upper() == "A":
        # choose subject of questions
        print(
            f"Welcome {player} in learning mode! Now, you have to choose, which subject you want to use in learning. "
            f"Choose from below:\n"
            f"Methods on dictionaries: type 'a'\n"
            f"Methods on integers/boolean: type 'b'\n"
            f"Methods on floats: type 'c'\n"
            f"Methods on lists: type 'd'\n"
            f"Methods on sets: type 'e'\n"
            f"Methods on strings: type 'f'\n"
            f"Methods on tuples: type 'g'"
        )
        subject_input = input("Your choice: ")
        print(interlude)

        # validating subject
        while subject_input.upper() not in "ABCDEFG":
            subject_input = input(f"Oopsie! Bad answer! Type again: ")
            print(interlude)

        # adding subject dict
        if subject_input.upper() == "A":
            subject = dict_methods
        elif subject_input.upper() == "B":
            subject = int_bool_methods
        elif subject_input.upper() == "C":
            subject = float_methods
        elif subject_input.upper() == "D":
            subject = list_methods
        elif subject_input.upper() == "E":
            subject = set_method
        elif subject_input.upper() == "F":
            subject = string_methods
        elif subject_input.upper() == "G":
            subject = tuple_methods

        print(f"Let the learning begin {player}!")
        print(interlude)

        # beginning of learning mode
        while True:
            method_item = random.choice(list(subject.items()))
            method_key = method_item[0]
            method_value = method_item[1]

            print(f"Method: {method_key.title()}")
            answer = input(
                "Type:\n"
                "If you want to get description of above method: y\n"
                "If you want to skip that one: n\n"
                "If you want to exit: e\n"
                "Your choice: "
            )
            print(interlude)

            # validate:
            if answer.upper() not in "YNE":
                answer = input("Oopsie! Bad answer - type again: ")
                print(interlude)

            if answer.upper() == "Y":
                print(f"Method: {method_key}\nDescription: {method_value}")
                print(interlude)
            elif answer.upper() == "E":
                break

    if learn_or_play.upper() == "B":
        # choose subject of questions
        print(
            f"Welcome {player} in play game mode! Now, you have to choose, which subject you want to use in game. "
            f"Choose from below:\n"
            f"Methods on dictionaries: type 'a'\n"
            f"Methods on integers/boolean: type 'b'\n"
            f"Methods on floats: type 'c'\n"
            f"Methods on lists: type 'd'\n"
            f"Methods on sets: type 'e'\n"
            f"Methods on strings: type 'f'\n"
            f"Methods on tuples: type 'g'"
        )
        subject_input = input("Your choice: ")
        print(interlude)

        # validating subject
        while subject_input.upper() not in "ABCDEFG":
            subject_input = input(f"Oopsie! Bad answer! Type again: ")
            print(interlude)

        # adding subject dict
        if subject_input.upper() == "A":
            subject = dict_methods
        elif subject_input.upper() == "B":
            subject = int_bool_methods
        elif subject_input.upper() == "C":
            subject = float_methods
        elif subject_input.upper() == "D":
            subject = list_methods
        elif subject_input.upper() == "E":
            subject = set_method
        elif subject_input.upper() == "F":
            subject = string_methods
        elif subject_input.upper() == "G":
            subject = tuple_methods

        # beginning of the game
        print(
            f"Let the game begin {player}! Now you will have to answer 10 questions about chosen subject. "
            "\nCollect 10 points to win the game! "
            f"\nPoints: {points}"
        )
        print(interlude)

        # questions
        while number_of_question <= 10:
            task = random.choice(list(subject.items()))
            key = task[0]
            value = task[1]
            print(
                f"Question number {number_of_question}:\nWhat does {key} method?"
                f"\nType:"
                f"\ny (yes) -> if you can explain,"
                f"\nn (no) -> if you can't,"
                f"\ne (exit) -> to exit the game."
            )
            answer = input("Answer: ")
            print(interlude)
            while answer.title() not in "YNE":
                answer = input(
                    "Choose one option from below:"
                    "\ny (yes) -> if you can explain,"
                    "\nn (no) -> if you can't,"
                    "\ne (exit) -> to exit the game.\n"
                    "Answer: "
                )
                print(interlude)
            if answer.title() == "Y":
                points += 1
                if points == 1:
                    print(f"Nice one! You have {points} point!")
                else:
                    print(f"Nice one! You have {points} points!")
                print(interlude)
            elif answer.title() == "N":
                print(f"Next time you'll get it!\nPoints: {points}")
                print(interlude)
                print(f"Here you can see method and the description:\nMethod:\n{key.title()}\n\nDescription:\n{value}")
                print(interlude)
            elif answer.title() == "E":
                print("See you next time!")
                break
            number_of_question += 1

        # end of the game
        if points == 10:
            print(f"Amazing job, {player}! You won the game!")
        elif 9 <= points >= 7:
            print(f"Good job, {player}! You collected {points} points!")
        elif 6 <= points >= 3:
            print(
                f"Keep doing, {player}! You collected {points} points, but next time you'll be better!"
            )
        else:
            print(
                f"Don't be sad {player}. Try again - I think it's going to be better next time."
            )

    # check if player wants to play again
    print(interlude)
    print(
        "Thanks for playing my game! Do you want to play it once again?\n"
        "Type:\nPlay once again: y\nNaaah, not this time: n"
    )
    choice = input("Your choice: ")

    # validating
    if choice.upper() not in "YN":
        choice = input("Bad answer! Choose from above: ")

    if choice.upper() == "Y":
        game()
    else:
        print("Thank you for game! Bye! :)")


if __name__ == "__main__":
    game()
