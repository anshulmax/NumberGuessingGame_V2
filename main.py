# Anshul Anugu
# Purpose: Upgrading our original Number Guessing Game.
# Asking Player for their name prior to playing the game
# Displaying the results of the game. Only saving the top 5 players.
# Allowing the player to play again without rerunning the program.
# Make it feel like a game
# Let's upgrade this!
# Import in random and my_data file.
from random import randint
from my_data import *
# Create Variables
guess_count = 0
correct_guess = 0
user_guess = ""
p_quit = False
random_number = randint(1, 100)
# Print our instructions
print(f"Hello and Welcome to my Guessing Game! ")
print(f"Please enter a guess between 1 and 100. ")
print(f"I will tell you if your guess is too high or low to aid. ")
print(f"You can exit the game at any time by typing the letter 'Q', but we hope this will not be the case! ")
print(f"Have fun and please share this with your friends! ")
print()
# Get the user's name to begin.
user_name = input("Welcome, please insert your name to get started! ")
# Use similar strategy as first guessing game and have a loop active till player wants to quit.
while True:
    # Use a try block with a while loop going through it.
    try:
        while correct_guess == 0:
            user_guess = input("What is your guess? ")
            guess_count, correct_guess = testGuess(user_guess, guess_count, random_number, user_name)
            if correct_guess == 2:
                p_quit = True
        if not p_quit:
            p_quit = updateScores(user_name, guess_count)
            if p_quit != True:
                    p_quit = displayScores()
                    print("Would you like to play again?")
                    if input("Enter 'Q' to quit. Type anything else to play again! ").upper() == "Q":
                        p_quit = True
                    # Remember to make p_quit = false this time around
                    else:
                        random_number = randint(1, 100)
                        guess_count = 0
                        user_guess = ""
                        correct_guess = 0
                        p_quit = False
        # Alternative case. Make sure you include a break statement
        if p_quit:
            print("GAME OVER! Thanks for Playing! ")
            if correct_guess == 2:
                print(f"The correct number was {random_number}.")
            break
    # Remember to close your try block with an exception
    except Exception as e:
        print(f"There seems to be an error on our end. We apologize. ")
        break