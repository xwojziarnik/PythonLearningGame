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

    The game has several stages:
        - Introduction (user has to write his name/nickname),
        - Short info about the game,
        - Questions based on random chosen methods from a particular set -> chosen in the beginning,
        - End of the game, where points are displayed and not known methods are explained.
    """
    # VARIABLES
    subject = None

    # intro
    print("-" * 40)
    print(">>>>> Hello in an exercise game! <<<<<".center(40))
    print("-" * 40)
    player = input("Write down your name: ")
    player = player.title()
    print("-" * 40)
    number_of_question = 1
    points = 0

    # choose version of game
    print(
        f"Welcome in the game {player}! What do you want to do?\nLearn: type 'a'\nPlay game: type 'b'"
    )
    learn_or_play = input("Your choice: ")

    # validating choice
    while learn_or_play.upper() not in "AB":
        learn_or_play = input(
            "Bad answer! You have to choose from 'a' (which stands for learning) or 'b' (which stands for "
            "playing game). Remember to type letter a or b without quotes! "
        )

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

        # validating subject
        while subject_input.upper() not in "ABCDEFG":
            subject_input = input(f"Oopsie! Bad answer! Type again: ")

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
        print("-" * 20)

        # questions
        while number_of_question <= 10:
            task = random.choice(list(subject.keys()))
            print(
                f"Question number {number_of_question}:\nWhat does {task} method?"
                f"\nType:"
                f"\ny (yes) -> if you can explain,"
                f"\nn (no) -> if you can't,"
                f"\ne (exit) -> to exit the game."
            )
            print("-" * 20)
            answer = input("Answer: ")
            while answer.title() not in "YNE":
                answer = input(
                    "Choose one option from below:"
                    "\ny (yes) -> if you can explain,"
                    "\nn (no) -> if you can't,"
                    "\ne (exit) -> to exit the game.\n"
                )
            if answer.title() == "Y":
                points += 1
                if points == 1:
                    print(f"Nice one! You have {points} point!")
                else:
                    print(f"Nice one! You have {points} points!")
                print("-" * 20)
            elif answer.title() == "N":
                print(f"Next time you'll get it!\nPoints: {points}")
                print("-" * 20)
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


if __name__ == "__main__":
    game()
