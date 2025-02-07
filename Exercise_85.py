"""Please write a program to randomly print an integer number between 7 and 15 inclusive.
Use random.randrange() to a random integer in a given range."""

import random

def print_random_number():
    random_number = random.randrange(7, 16)
    print(random_number)

print_random_number()