# Guess The Number Game

import random

number = random.randint(1, 10)

print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == number:
    print("🎉 Correct! You won!")

elif guess > number:
    print("Too high!")

else:
    print("Too low!")

print("The number was:", number)