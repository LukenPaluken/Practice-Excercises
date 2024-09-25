"""
Like wordle, but with numbers.
"""

import random as rn


def generate_random_number() -> list[int]:
    """
    Generates a list with 6 random numbers.

    returns: list[int]
    """
    return [rn.randint(0, 9) for _ in range(6)]


def measure_text_length() -> None:
    """
    Writes empty spaces that equal the length of the input text.
    """
    for _ in range(len(TEXT)):
        print(" ", end="")


def user_input() -> list[int]:
    """
    Handles user inputs.

    Splits input and casts each number(str) to int. Checks for errors.

    returns: user_number_int -> list[int]
    """
    try:
        user_number = input(TEXT).split()
        user_number_int = list(map(int, user_number))

        if len(user_number_int) != 6:
            print("Error: Please enter exactly 6 numbers.")
            return -1

        if any(number not in range(10) for number in user_number_int):
            print("Error: All numbers must be between 0 and 9.")
            return -2

        return user_number_int

    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return -1


def game(user_guess: list[int], random_number: list[int]) -> None:
    """
    Compares user input with random number.

    Prints graphical hints.

    parameters: user_guess -> list[int], random_number -> list[int]
    """
    for idx, number in enumerate(user_guess):
        if number == random_number[idx]:
            print(number, end=" ")
        elif number > random_number[idx]:
            print("▼", end=" ")
        else:
            print("▲", end=" ")
    print()


def app() -> None:
    """
    Handles game behavior (start, play, end).
    """
    random_number = generate_random_number()
    guessed = False
    attempts = 6

    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt}/{attempts}")

        user_guess = user_input()

        if user_guess == -1 or user_guess == -2:
            continue

        if user_guess == random_number:
            guessed = True
            break
        else:
            measure_text_length()
            game(user_guess, random_number)

    if guessed:
        print("\nWinner!")
    else:
        print(f"\nLoser. The correct number was {random_number}.")


TEXT = "Enter each number seperated by a space (x y z): "


app()
