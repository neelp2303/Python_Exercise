"""Please write a program to output a random even number between 0 and 10 inclusive using a random module
and list comprehension.
Use random.choice() to a random element from a list."""

import random

numbers = [i for i in range(0, 11, 2)]
random_number = random.choice(numbers)

print(random_number)