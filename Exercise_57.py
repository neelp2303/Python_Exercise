"""Please write a program which prints all permutations of [1,2,3]
Use itertools.permutations() to get permutations of lists."""

import itertools

numbers = [1, 2, 3]

permutations = list(itertools.permutations(numbers))

print(permutations)