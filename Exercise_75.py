"""Please write a program which accepts basic mathematical expression from console and print the evaluation
result.
Example:
If the following string is given as input to the program:
35+3
Then, the output of the program should be:
38

Use eval() to evaluate an expression."""

expression = input("Enter an expression: ")
result = eval(expression)
print(result)

