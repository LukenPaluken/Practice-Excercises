import csv
import random as rn
from termcolor import colored


def handle_csv_words() -> list[str]:
    """
    Reads a CSV file containing a list of 6-letter words and returns them as a list.

    Returns:
        list[str]: A list of six-letter words from the CSV file.
        If the file is not found, returns an empty list.
    """
    words = []
    file_name = "projects/wordle/real_six_letter_words.csv"
    try:
        with open(file_name, "r", encoding="utf-8") as words_file:
            csvreader = csv.reader(words_file)
            for row in csvreader:
                if row:
                    words.append(row[0])
    except FileNotFoundError:
        print("Error: File not found.")
        return []

    return words


def grab_random_word(words: list[str]) -> str:
    """
    Selects a random word from a list of words.

    Args:
        words (list[str]): The list of words to choose from.

    Returns:
        str: A randomly selected word from the list.
    """
    return rn.choice(words)


def validate_user_input(user_input: str) -> bool:
    """
    Validates the user's input to ensure it meets the criteria of being a 6-letter alphabetical word.

    Args:
        user_input (str): The user's input string.

    Returns:
        bool: True if the input is valid (6 letters and alphabetic), False otherwise.
    """
    user_input = user_input.strip().lower()
    if len(user_input) != 6 or not user_input.isalpha():
        print(
            "Error: Word must be 6 letters long and contain only alphabetical characters."
        )
        return False
    return True


def show_word_status(user_input: str, random_word: str) -> None:
    """
    Displays the status of the guessed word by comparing it to the random word.
    Letters in the correct position are colored green, letters in the wrong position
    but present in the word are colored yellow, and incorrect letters remain uncolored.

    Args:
        user_input (str): The user's guessed word.
        random_word (str): The target word to compare against.
    """
    status_output = []
    for idx, letter in enumerate(user_input):
        if letter == random_word[idx]:
            status_output.append(colored(letter, "green"))
        elif letter in random_word:
            status_output.append(colored(letter, "yellow"))
        else:
            status_output.append(letter)
    print(" ".join(status_output))


def play_game() -> None:
    """
    Plays a word-guessing game where the user tries to guess a random 6-letter word.
    The user has six attempts to guess the word, and after each guess, they are shown
    the status of their guess. The user can play multiple rounds.
    """
    while True:
        attempts = 6
        guessed = False
        random_word = grab_random_word(word_list)

        attempt = 0
        while attempt < attempts:
            print(f"\nAttempt {attempt + 1}/{attempts}")
            guess = input("Enter a 6-letter word: ").strip().lower()

            if not validate_user_input(guess):
                continue

            show_word_status(guess, random_word)
            attempt += 1

            if guess == random_word:
                guessed = True
                break

        if guessed:
            print("\nYou Win!")
        else:
            print(f"\nYou lose. The word was: {random_word}")

        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again != "y":
            break


word_list = handle_csv_words()

if word_list:
    play_game()
else:
    print("No words available to play the game.")
