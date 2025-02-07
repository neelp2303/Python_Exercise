"""Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise
print "No".
Use if statement to judge condition."""

input_string = input("Enter a string: ")

if input_string == "yes" or input_string == "Yes" or input_string == "YES":
    print("Yes")
else:
    print("No")