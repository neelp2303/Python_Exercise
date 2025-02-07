"""Write a program to generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10).
Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list."""

given_tuple = (1,2,3,4,5,6,7,8,9,10)
even_tuple = tuple(num for num in given_tuple if num % 2 == 0)

print(even_tuple)