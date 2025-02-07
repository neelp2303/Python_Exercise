"""Write a program which can map() to make a list whose elements are squares of numbers between 1 and 20
(both included).
Use map() to generate a list.
Use lambda to define anonymous functions."""

squares = list(map(lambda x: x**2, range(1, 21)))
print(squares)
