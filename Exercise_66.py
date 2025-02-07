"""Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
Use the unicode() function to convert."""

ascii_string = input("Enter an ASCII string: ")


utf8_encoded = ascii_string.encode("utf-8")

print("UTF-8 Encoded Bytes:", utf8_encoded)