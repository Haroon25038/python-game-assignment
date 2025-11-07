# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com)
# to assist in drafting parts of the code in this file.

import random

def guess_the_number():
    number = random.randint(1, 10)
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 10.")
    print("Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess (1-10): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < 1 or guess > 10:
            print("Number out of range! Try again.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("🎉 Correct! You guessed the number!")
            break

guess_the_number()

