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


