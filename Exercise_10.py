"""Write a program that accepts a sequence of whitespace separated words as input and prints the words after
removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set containers to remove duplicated data automatically and then use sorted() to sort the data."""

string = input()
words = string.split()
unique= set(words)
sorted= sorted(unique)
print(" ".join(sorted))