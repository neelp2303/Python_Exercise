"""Assuming that we have some email addresses in the "username@companyname.com" format, please write a
program to print the company name of a given email address. Both user names and company names are
composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
In case of input data being supplied to the question, it should be assumed to be a console input.
Use \w to match letters."""

import re

def find_company_name(email):
    pattern = r'\w+@(\w+)\.com'
    match = re.search(pattern, email)
    if match:
        return match.group(1)

email = input("Enter an email address: ")

company_name = find_company_name(email)

if company_name:
    print("Company name:", company_name)


