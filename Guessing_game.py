# emelu codes
import random
n = 20
guess_num = int(n * random.random()) + 1
guess = 0
while guess != guess_num:
    guess = int(input("Guess a number from 1 to 20: "))
    if guess > 0:
        if guess > guess_num:
            print("Guessed number is too Large")
        elif guess < guess_num:
            print("Guessed number is too small")
        else:
            print("Congratulation, you made it")

    elif guess < 0:
        print("Guess again")