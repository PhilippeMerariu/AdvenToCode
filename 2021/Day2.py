from typing import List

file = open('input2.txt')
line = file.readline()

commands: List[str] = []
horizontal: int = 0
depth: int = 0

while line:
    commands.append(line.strip())
    line = file.readline()
file.close()

for com in commands:
    orientation, position = com.split(" ")
    if orientation == "forward":
        horizontal += int(position)
    elif orientation == "down":
        depth += int(position)
    else:
        depth -= int(position)


print("ANSWER = {0}".format(horizontal * depth))