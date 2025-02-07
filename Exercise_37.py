"""Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many
chickens do we have?
Use a for loop to iterate all possible solutions."""

for chicken_num in range(1, 95):
    rabbit_num = 35 - chicken_num
    if chicken_num * 2 + rabbit_num * 4 == 94:
        print(f"Number of chickens: {chicken_num}, Number of rabbits: {rabbit_num}")
