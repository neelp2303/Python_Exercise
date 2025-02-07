"""By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th
numbers in [12,24,35,70,88,120,155].
Use list comprehension to delete a bunch of elements from a list.
Use enumerate() to get (index, value) tuple."""

numbers = [12,24,35,70,88,120,155]


new_numbers = [num for i, num in enumerate(numbers) if i % 2 != 0]

print(new_numbers)  
