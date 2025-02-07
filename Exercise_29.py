"""Define a function that can receive two integral numbers in string form and compute their sum and then print it
in the console.
Use int() to convert a string to integer."""

def add_numbers(num1, num2):
    sum = int(num1) + int(num2)
    print("Sum:", sum)

add_numbers("10", "20")