"""Write a program which can filter() to make a list whose elements are an even number between 1 and 20 (both
included).
Use filter() to filter elements of a list.
Use lambda to define anonymous functions."""

numbers = list(range(1, 21))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)