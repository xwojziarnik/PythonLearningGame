from additional_info.string_methods import string_methods
from additional_info.int_float_bool_methods import int_bool_methods, float_methods

import random

string_methods = [
    "capitalize",
    "casefold",
    "center",
    "count",
    "encode",
    "endswith",
    "expandtabs",
    "find",
    "format",
    "format_map",
    "index",
    "isalnum",
    "isalpha",
    "isascii",
    "isdecimal",
    "isdigit",
    "isidentifier",
    "islower",
    "isnumeric",
    "isprintable",
    "isspace",
    "istitle",
    "isupper",
    "join",
    "ljust",
    "lower",
    "lstrip",
    "maketrans",
    "partition",
    "removeprefix",
    "removesuffix",
    "replace",
    "rfind",
    "rindex",
    "rjust",
    "rpartition",
    "rsplit",
    "rstrip",
    "split",
    "splitlines",
    "startswith",
    "strip",
    "swapcase",
    "title",
    "translate",
    "upper",
    "zfill",
]


def game():
    """
    Bash game where user can learn about methods based on Python types.

    The game has several stages:
        - Introduction (user has to write his name/nickname),
        - Short info about the game,
        - Questions based on random chosen methods from a particular set -> chosen in the beginning,
        - End of the game, where points are displayed and not known methods are explained.
    """
    # intro
    print("-" * 20)
    print("Hello in exercise game!".center(20, "-"))
    print("-" * 20)
    player = input("Write down your name: ")
    player = player.title()
    print("-" * 20)
    number_of_question = 1
    points = 0

    # beginning of the game
    print(
        f"Welcome in the game {player}! Now you will have to answer 10 questions about chosen subject. "
        "\nCollect 10 points to win the game! "
        f"\nPoints: {points}"
    )
    print("-" * 20)

    # questions
    while number_of_question <= 10:
        task = random.choice(string_methods)
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
