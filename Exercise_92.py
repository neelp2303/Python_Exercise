"""By using list comprehension, please write a program to print the list after removing delete numbers which are
divisible by 5 and 7 in [12,24,35,70,88,120,155].
Use list comprehension to delete a bunch of elements from a list."""

numbers = [12, 24, 35, 70, 88, 120, 155]


numbers = [num for num in numbers if num % 7 == 0 and num % 5 == 0]

print(numbers)
