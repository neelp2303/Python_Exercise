"""Please write assert statements to verify that every number in the list [2,4,6,8] is even.
Use "assert expression" to make an assertion."""

numbers = [2,4,6,8]

for num in numbers:
    assert num % 2 == 0, f"{num} is not even"

print("All numbers in the list are even.")