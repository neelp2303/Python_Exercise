"""Define a function which can generate and print a list where the values are square of numbers between 1 and
20 (both included).
Use ** operator to get the power of a number.
Use range() for loops.
Use list.append() to add values into a list."""

def generate_squares():
    squares = []
    for i in range(1, 21):
        squares.append(i**2)
    return squares

print(generate_squares())