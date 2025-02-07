"""A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT
and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps. Please write a program to compute the distance from the current
position after a sequence of movement and original point. If the distance is a float, then just print the nearest
integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
In case of input data being supplied to the question, it should be assumed to be a console input."""

x = y = 0
while True:
    direction = input().split()
    if len(direction) != 2:
        break
    if direction[0] == "UP":
        x += int(direction[1])
        continue
    elif direction[0] == "DOWN":
        x -= int(direction[1])
        continue
    elif direction[0] == "LEFT":
        y -= int(direction[1])
        continue
    elif direction[0] == "RIGHT":
        y += int(direction[1])
        continue
print("(" + str(x) + "," + str(y) + ")")
