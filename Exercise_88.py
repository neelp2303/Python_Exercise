"""Please write a program to shuffle and print the list [3,6,7,8].
Use shuffle() function to shuffle a list."""

import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(shuffle_list([3,6,7,8]))