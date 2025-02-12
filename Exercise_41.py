"""Define a function which can generate a list where the values are square of numbers between 1 and 20 (both
included). Then the function needs to print all values except the first 5 elements in the list.
Use ** operator to get the power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list"""

def generate_squares():
    squares = []
    for i in range(1, 21):
        squares.append(i**2)

    
    return squares[5:]

print(generate_squares())