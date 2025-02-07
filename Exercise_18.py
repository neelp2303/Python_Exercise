"""A website requires the users to input username and password to register. Write a program to check the validity
of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the
above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
In case of input data being supplied to the question, it should be assumed to be a console input."""

passwords = input().split(",")
valid_passwords = []

for password in passwords:
    if len(password) >= 6 and len(password) <= 12:
        has_lowercase = any(char.islower() for char in password)
        has_uppercase = any(char.isupper() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special_char = any(char in "$#@%" for char in password)
        
        if has_lowercase and has_uppercase and has_digit and has_special_char:
            valid_passwords.append(password)
    
print(",".join(valid_passwords))
