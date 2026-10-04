# Q12: Number Guessing Game
# Why a while loop? We don't know how many guesses the user will need.
# The loop must keep running until the guess is correct, so while fits.

import random

secret = random.randint(1, 100)   # generated ONCE, before the loop
attempts = 0

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue                  # invalid input is not counted as an attempt

    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue                  # out-of-range guess is not counted either

    attempts += 1

    if guess == secret:
        print(f"Correct! The number was {secret}.")
        print(f"You guessed it in {attempts} attempt(s).")
        break
    elif guess > secret:
        print("Too High")
    else:
        print("Too Low")