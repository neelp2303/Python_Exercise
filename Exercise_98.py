"""With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all
duplicate values with the original order reserved.
Use set() to store a number of values without duplicates."""

given_list = [12,24,35,24,88,120,155,88,120,155]    

unique_list = list(set(given_list))

print(unique_list)
