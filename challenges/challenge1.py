'''
Challenge 1: The Number Guesser
Write a program where the computer picks a random number between 1 and 50. The user has a maximum of 5 attempts to guess the number.
'''

# IMPORTING LIBRARY
import random as rd # Importing random library with an alias

# INITIALIZING THE VARIABLES
# 1. INTERVAL TO GUESS
# Getting the minimum value from the user
while True:
    # Minimum value for the interval, it will enter here, even if there's no variable to initialize
    interval_min: int = int(input("Type the minimum interval's value: "))
    if interval_min < 0:
        print(f"Your minimum is less than 0, please retype your minimum!")
    else:
        print("Gotcha! Value accepted!!")
        break

# Getting the max value from the user
while True:
    # Getting the max value for the guessing game
    interval_max: int = int(input("Type the max value from your interval: "))
    # Interval max can't be lesser than minimum
    if interval_max < interval_min:
        print("Your max value is smaller than your minimum")
    else:
        break

user_attempts: int = 5 # NUMBER OF USER ATTEMPTS
guess_number: int = rd.randint(interval_min, interval_max) # It will select an number by random
user_guess: int = None # It starts with None because user don't guess anything

# GUESSING GAME:
while user_attempts != 0:
    user_guess = int(input("Type your guess: ")) # User will type their guess
    # Comparison between number and user guess
    if user_guess > guess_number:
        user_attempts -= 1 # Decrease the number of user attempts
        print(f"You're wrong, the number is smaller than your guess! | You have more {user_attempts} attempts") # Inform the user about the wrong choice
    elif guess_number > user_guess:
        user_attempts -= 1 # Decrease the number of user attempts
        print(f"Wrong choice, the number is greater than your choice! | You have more {user_attempts} attempts") # Inform about the wrong choice
    else: # If the user make the right guess
        print("Awesome, you hit the nail! Congratulations, you Won!")
        break

if user_attempts == 0:
    print(f"You lost your game, the correct choice were: {guess_number} \n Don't worry try it again")
else:
    print("You won, why don't you challenge me again ?")