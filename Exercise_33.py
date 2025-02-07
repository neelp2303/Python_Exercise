"""Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included)
and the values are square of keys.
Use dict[key]=value pattern to put an entry into a dictionary.
Use ** operator to get the power of a number."""


def square_dict():
    dictionary = {}
    for i in range(1, 4):
        dictionary[i] = i**2
    print(dictionary)


square_dict()
