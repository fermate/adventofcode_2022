import numpy as np
import re
import common

path = "inputs/day_05_input.txt"

fileContent = common.readFile(path, False)

result1 = ''  # result for part 1
score2 = 0  # score for part 2
regex = 'move ([\d]*) from ([\d]*) to ([\d]*)'

stackPart = fileContent[:fileContent.index('\n')]
moves = fileContent[fileContent.index('\n') + 1:]

stackPart = [list(str) for str in stackPart]
stackPart = np.rot90(stackPart,-1)

stacks1 = [[]]  # initial state for part 1
stacks2 = [[]]  # initial state for part 2
# Creating the initial state
for line in stackPart:
    if(line[0].isnumeric()):
        aa = ''
        pile = list(aa.join(line[1:]).rstrip())
        stacks1.append(pile)
        stacks2.append(pile)


############
# Part 1
for move in moves:
    command = re.search(regex, move)
    for _ in range(int(command.group(1))):
        stacks1[int(command.group(3))].append(stacks1[int(command.group(2))].pop())

result1 = result1.join([line[-1] for line in stacks1[1:]])


############
# Part 2


print(result1)   # Correct answer: 
print(score2)   # Correct answer: 