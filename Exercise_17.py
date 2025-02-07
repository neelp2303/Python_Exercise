"""Write a program that computes the net amount of a bank account based on a transaction log from console
input. The transaction log format is shown as follows:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
In case of input data being supplied to the question, it should be assumed to be a console input."""

balance = 0
while True:
    transaction = input().split()
    if len(transaction) != 2:
        break
    if transaction[0] == "D":
        balance += int(transaction[1])
        # print(balance)
        continue
    elif transaction[0] == "W":
        balance -= int(transaction[1])
        # print(balance)
        continue
print(balance)
