"""Define a function that can accept two strings as input and print the string with maximum length in the console.
If two strings have the same length, then the function should print all strings line by line.
Use len() function to get the length of a string"""


def max_length_string(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    elif len(str1) == len(str2):
        print(str1)
        print(str2)


str1 = "Hello"
str2 = "World"
max_length_string(str1, str2)
