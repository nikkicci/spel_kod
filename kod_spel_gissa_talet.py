
import random

print("Välkommen till gissningspelet!")
print("Gissa vilket tal jag tänker på mellan 1 och 100.")

number = random.randint(1, 100)  # generate random number
guess = -1  # initialize guess to an invalid value

while guess != number:
    guess_str = input("Skriv ditt svar: ")
    guess = int(guess_str)

    if guess < number:
        print("För lågt, försök igen.")
    elif guess > number:
        print("För högt, försök igen.")

print(f"Grattis! Du gissade rätt på nummer {number}!")
