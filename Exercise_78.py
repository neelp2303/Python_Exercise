"""Please generate a random float where the value is between 10 and 100 using the Python math module.
Use random.random() to generate a random float in [0,1]."""

import random

def generate_random_float():
    return random.random()*(100-10)+10

print(generate_random_float())