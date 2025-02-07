"""Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive
using a random module and list comprehension.
Use random.choice() to a random element from a list."""

import random

numbers = [i for i in range(0, 11) if i % 7 == 0 and i % 5 == 0]
print(random.choice(numbers))
