"""The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form
with a given input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13

We can define a recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.
In case of input data being supplied to the question, it should be assumed to be a console input."""

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())

fib_sequence = [str(fibonacci(i)) for i in range(n+1)]

print(",".join(fib_sequence))