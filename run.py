"""
Project 3, Hangman
"""

from time import sleep
import random
from hangman_parts import parts

#Prints a hangman picture
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

#Creating a list of words from which the player will receive a random choice.
words = ['mouse',]

picked = random.choice(words)

print('The word has', len(picked), 'letters')

right = ['_'] * len(picked)
wrong = []

def update():
    for i in right:
        print(i, end = ' ')
    print()

update()

#Creating a loop for player to choose new letters
while True:
    
    print('=====================')

#This will make any correct letter picked go into the correct underscore
    
    guess = input("Guess a letter..")

    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index += 1
        update()
    
    else:
        wrong.append(guess)
        print('Wrong:' ,wrong)


