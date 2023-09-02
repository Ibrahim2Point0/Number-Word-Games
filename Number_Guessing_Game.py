# This is a number guessing game. The program will generate a random whole number between 0 - 50 and the user must guess the number. The program will let the user know if the guess is too high or too low until the correct number is guessed.

import random

start_game = input("Do you want to play a guessing game? Enter 'Y' or 'N': ")


while start_game == "Y":
    if start_game == "Y":
        secret_number = random.randrange(0, 51)
        print(secret_number)
        user_guess = int(input("Guess a number between 0 - 50: "))
        while user_guess != secret_number:
            if user_guess != secret_number:
                if user_guess > secret_number:

                    user_guess = int(input("Guess is too high, guess again: "))
                elif user_guess < secret_number:
                    user_guess = int(input("Guess is too low, guess again: "))
        else:
            if user_guess == secret_number:
                print(f"Congrats! You guessed right! The secret number is {secret_number}!")
                start_game = input(f"Do you want to play again? Enter 'Y' or 'N': ")
else:
    print(f"Have a nice day.")