"""Write a program which accepts a sequence of comma-separated numbers from the console and generates a
list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple"""

num = input()
list = num.split(",")
tuple = tuple(list)

print(tuple)
print(list)
