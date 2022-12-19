# Program: Play a guessing game
# Author: Amir Akbari
# Date: 03/08/22
"""
    Problem: Use a flag-controlled and counter-controlled loop to play a
        number guessing game
    Input: a guessed number
    Processing: check whether number is matched with the magic number
    Output: Display message of either winning or not winning
    Detailed Pseudocode:
        1. Generate the magic number
        2. Start while loop to play the game
        3.   a. prompt the user to guess a number
             b. check whether number is matched
             c. if number is not matched, ask user to guess again
             d. increment the guess counter
             e. if user guesses correctly or user used up all the attempts,
                 get out of the loop.
        4. If user guess correctly, display congrats message, else display try
           again message
    variables: guess_number, magic_number, attempt, matched
    constants: TOTAL_ATTEMPTS = 4
"""
import random
TOTAL_ATTEMPTS = 4
attempt = 0
matched = False
magic_number = random.randint(1,10)
while matched == False and attempt < TOTAL_ATTEMPTS:
    guess_number = int(input("Enter the guess number 1-10:"))
    if guess_number == magic_number:
        matched = True
    elif guess_number > magic_number:
        print("Your number is too big")
    elif guess_number < magic_number:
        print("Your number is too small")
    attempt += 1
print("The magic is:",magic_number)
if matched:
    print("Congratulations, you won")
else:
    print("Try another time!")
