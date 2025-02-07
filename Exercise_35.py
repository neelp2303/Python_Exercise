"""Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both
included) and the values are square of keys. The function should just print the values only.
Use dict[key]=value pattern to put an entry into a dictionary.
Use ** operator to get the power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs."""

def square_dict():
    square_dict = {}
    for i in range(1, 21):
        square_dict[i] = i ** 2
    for key, value in square_dict.items():
        print(key,value)
    print(square_dict)
square_dict()