"""Write a function to compute 5/0 and use try/except to catch the exceptions.
Use try/except to catch exceptions."""

def divide_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

print(divide_by_zero())