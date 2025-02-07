"""Write a program that accepts a sentence and calculate the number of upper case letters and lower case
letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
In case of input data being supplied to the question, it should be assumed to be a console input."""

string=input()
upper=lower=0

for char in string:
    if char.isupper():
        upper +=1
    elif char.islower():
        lower +=1
    continue

print("UPPER CASE",upper)

print("LOWER CASE",lower)