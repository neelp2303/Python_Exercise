"""Write a program to compute the frequency of the words from the input. The output should be output after
sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
In case of input data being supplied to the question, it should be assumed to be a console input."""

import re

def word_frequency(input_str):
    words = re.findall(r'\b\w+\b', input_str.lower())
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    sorted_dict = dict(sorted(frequency_dict.items()))
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
    
input_str = input("Enter the input string: ")

word_frequency(input_str)
