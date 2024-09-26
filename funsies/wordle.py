from termcolor import colored
import random as rn


def grab_random_word(words: list[str]) -> str:
    return rn.choice(words)


def validate_user_input(user_input: str) -> bool:
    user_input = user_input.strip().lower()
    if len(user_input) != 6 or not user_input.isalpha():
        print(
            "Error: Word must be 6 letters long and contain only alphabetical characters."
        )
        return False
    return True


def show_word_status(user_input: str, random_word: str) -> None:
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

    while True:
        attempts = 6
        guessed = False
        random_word = grab_random_word(word_list)

        for attempt in range(attempts):
            print(f"\nAttempt {attempt + 1}/{attempts}")
            guess = input("Enter a 6 letter word: ").strip().lower()

            if not validate_user_input(guess):
                continue

            show_word_status(guess, random_word)

            if guess == random_word:
                guessed = True
                break

        if guessed:
            print("\nYou Win!")
        else:
            print("\nYou lose. The word was:", random_word)

        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again != "y":
            break


word_list = ["spaces", "parses", "mourns"]


play_game()
