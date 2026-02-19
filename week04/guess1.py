# guess1.py
# Guess a number until you get it right
# Author: John Crumlish

number_to_guess = 30

guess = int(input("Guess a Number!: "))
while guess != number_to_guess:
    print("Wrong")
    guess = int(input("Guess Again!: "))

print("Well Done! The Number Was:", number_to_guess)