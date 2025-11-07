# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com)
# to assist in drafting parts of the code in this file.


import random

def guess_the_number():
    number = random.randint(1, 10)
    print("Welcome to Guess the Number!")
    while True:
        guess = int(input("Enter your guess (1–10): "))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("🎉 Correct! You guessed the number!")
            break

guess_the_number()