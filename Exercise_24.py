"""Python has many built-in functions, and if you do not know how to use it, you can read documents online or
find some books. But Python has a built-in document function for every built-in function.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add documents for your own function
The built-in document method is __doc__"""

print(abs.__doc__)

print(int.__doc__)

print(input.__doc__)


def my_function(param1, param2):
    """
    This is a sample function that takes two parameters and returns their sum.

    Parameters:
    param1 (int): The first parameter.
    param2 (int): The second parameter.

    Returns:
    int: The sum of param1 and param2.
    """
    return param1 + param2


print(my_function.__doc__)
