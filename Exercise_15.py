"""Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
In case of input data being supplied to the question, it should be assumed to be a console input."""

value = str(input())
num2 = value + value
num3 = num2 + value
num4 = num3 + value
print(int(value) + int(num2) + int(num3) + int(num4))
