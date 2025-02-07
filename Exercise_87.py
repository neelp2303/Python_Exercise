"""Please write a program to print the running time of execution of "1+1" for 100 times.
Use timeit() function to measure the running time."""

import timeit

time_taken = timeit.timeit("1+1",number=100)


print(time_taken)

