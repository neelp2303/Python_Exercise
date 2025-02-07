"""Write a program that accepts a sequence of lines as input and prints the lines after making all characters in
the sentence capitalised.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
In case of input data being supplied to the question, it should be assumed to be a console input."""

# lines = input().splitlines()

# for line in lines:
#     print(line.upper())



lines = []
while True:
    try:
        line = input()
        if line:
            lines.append(line.upper())
        else:
            break
    except EOFError:
        break
for line in lines:
    print(line)