"""Please write a program to compress and decompress the string "hello world!hello world!hello world!hello
world!".
Use zlib.compress() and zlib.decompress() to compress and decompress a string."""

import zlib


original_string = "hello world!hello world!hello world!hello world!"
original_bytes = original_string.encode()

compressed_string = zlib.compress(original_bytes)

decompressed_string = zlib.decompress(compressed_string)

print("Original String:", original_string)
print("compressed String:", compressed_string)
print("Decompressed String:", decompressed_string)
