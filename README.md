# Hangman

Hangman is a Python terminal game, which runs in the Code Institute mock terminal Heroku. 

Users can try to beat the computer by guessing the letters of the missing word. Every wrong guess takes one life. The game is over if the user guesses all the missing letters of the hidden word or if he loses all his lives.

You can view the live site [here](https://hangman-fun-game.herokuapp.com/)

# How to play

It's a popular word guessing game where the player attempts to build a missing word by guessing one letter at a time. 

The player must guess the letters of the hidden word, if the guess is correct, the letter missing in the word is replaced by the correct letter.

If the player puts an incorrect letter, the error message is displayed and the player is asked to resubmit their choice. Each wrong guess takes 1 life. 


Game ends if the player correctly guesses all the letters of the missing word or if the player loses all his lives.

# User Stories 

- As a user I want to easily understand the purpose of the game
- As a user I want to have fun
- As a user I want to see my remaining lives
- As a user I want the game to be challenging 

# Features

- Welcome Screen - User can start a game and see the rules

<p align="center">
<img src="readme-assets/images/screenshot1.png" width="600px" height="400">
</p>

- Game - the game will start by selecting a random word from a list of selected words

- User Input - the player is asked to guess a letter. If the entry is correct, the letter will appear in the word, if the entry is incorrect, the user will lose one life and the hangman will start drawing.

<p align="center">
<img src="readme-assets/images/screenshot2.png" width="600px" height="400">
</p>

- Invalid inputs - to be sure that the user provided  the correct input. For any invalid input, the error message  will appear.

<p align="center">
<img src="readme-assets/images/screenshot3.png" width="600px" height="400">
</p>

# Issues and Bugs
 - Error message line too long
    - I fixed the error by splitting the string into two lines

# Technologies Used
- Languages 
    - Python

# Testing
## Validators
The [Python Code Checker](https://extendsclass.com/python-tester.html) was used to check my code for syntax errors in this project.

- Manually tested user inputs by purposefully inputing incorrect data to confirm error messages where capturing wrong inputs

- Tested in the local terminal and on the mock terminal on the deployment site on Heroku 

# Deployment 
### The project was deployed using Code Institute mock terminal for Heroku.

### Steps to deploy:
- Fork or clone this repository
- Ensure the Procfile is in place
- Create a new app in [Heroku](https://id.heroku.com/login)
- Select "New" and "Create new app"
- Name the new app and click "Create new app"
- In "Settings" select "BuildPacks" and select Python and Node.js
- While still in "Settings", click "Reveal Config Vars" and input the following. KEY: PORT, VALUE: 8000. Nothing else is needed here as this project does not have any sensitive files.
- Click on "Deploy" and select your deploy method and repository.
- Click "Connect" on selected repository.
- Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
- Heroku will now deploy the site.