"""
Project 3, Hangman
"""

from time import sleep
import random
from hangman_parts import parts
import string


def welcome():
    # Prints a hangman picture
    print("Welcome to Hangman")
    print('   ',  '------')
    print('   ',  '|    |')
    print('   ',  '|    O')
    print('   ',  '|   -|-')
    print('   ',  '|    |')
    print('   ',  '|   / \\')
    print('------------')
    print(
            """
                To play the game you must guess the letters of the hidden word.
                If the guess is correct, the letter missing in the word
                is replaced by the correct letter.
                You can enter the whole word if you know what the word is.
                Each wrong guess takes one life. You have four lives in total.

                Good luck!
                """
    )


def update():
    for i in right:
        print(i, end=' ')
    print()


# creating a time function when generating a word
def wait():
    for i in range(5):
        print('.', end='')
        sleep(.5)
    print()


def check_user_input(user_input):
    user_input = user_input.lower()
    if (user_input in string.ascii_lowercase) and (user_input not in ['']):
        return True
    return False


def play_game(picked):
    while True:
        print('=====================')
    # This will make any correct letter picked go into the correct underscore
        input_valid = False
        while input_valid is False:
            guess = input("Guess a letter..")
            input_valid = check_user_input(guess)
            if input_valid is False:
                print('Only letters allowed')
        print('let me check...')
        wait()
        if guess in picked:
            index = 0
            for i in picked:
                if i == guess:
                    right[index] = guess
                index += 1
            update()

        else:
            if guess not in wrong:
                wrong.append(guess)
                parts(len(wrong))
            else:
                print('You already guessed that letter')
                print(wrong)
    # code to maximise amount of lives or guesses of user
        if len(wrong) > 4:
            print('You lose...')
            print('The correct word is ', picked)
            break

        if '_' not in right:
            print('Well done! You win!')
            break


if __name__ == "__main__":
    # Creating a list of words from which the player will receive a random one.
    words = ['mouse', 'budget', 'corner', 'detail', 'appeal', 'diamond',
             'comfort', 'combine', 'college', 'auction', 'account', 'academy',
             'achieve', 'beyond', 'digital']
    play_again = True
    while play_again is True:
        picked = random.choice(words)
        welcome()
        print('The word has', len(picked), 'letters')
        right = ['_'] * len(picked)
        wrong = []
        print('choosing a word')
        wait()
        update()
        parts(len(wrong))
        play_game(picked)
        again = input("Press Y/y to play again or press anything else to quit")
        play_again = again.lower() in ['y']
    print('Thank you for playing')
