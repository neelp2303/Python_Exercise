"""Write a program which can map() to make a list whose elements are square of elements in
[1,2,3,4,5,6,7,8,9,10].
Use map() to generate a list.
Use lambda to define anonymous functions."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x**2, numbers))
print(squares)

