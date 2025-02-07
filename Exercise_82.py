"""Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
Use random.sample() to generate a list of random values."""

import random

def generate_random_numbers():
    return random.sample(range(100, 201), 5)

random_numbers = generate_random_numbers()

print(random_numbers)