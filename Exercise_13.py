"""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
Hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
In case of input data being supplied to the question, it should be assumed to be a console input."""

sentence = input("Enter a sentence: ")
letters = digits = 0

for char in sentence:
    if char.isalpha():
        letters += 1
        continue
    if char.isdigit():
        digits += 1
        continue

print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
