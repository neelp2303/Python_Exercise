"""Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
Use random.sample() to generate a list of random values."""

import random


def generate_even_numbers():
    even_numbers = random.sample(range(100, 201, 2), 5)
    return even_numbers


numbers = generate_even_numbers()
print(numbers)
