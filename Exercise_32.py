"""Define a function that can accept an integer number as input and print "It is an even number" if the number is
even, otherwise print "It is an odd number".
Use the% operator to check if a number is even or odd."""

def check_number(num):
    if num % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")



check_number(10)  
check_number(7)  


