"""Please generate a random float where the value is between 5 and 95 using the Python math module.
Use random.random() to generate a random float in [0,1]."""

import random

def generate_random_float():
    return random.random()*(95-5)+5

print(generate_random_float())