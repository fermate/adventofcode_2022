import numpy as np
import re
import common

path = "inputs/day_05_input.txt"

fileContent = common.readFile(path, False)

result1 = ''  # result for part 1
result2 = ''  # result for part 2
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
        stacks1.append(pile.copy())
        stacks2.append(pile.copy())


for move in moves:
    command = re.search(regex, move)
    count = int(command.group(1))
    fromStack = int(command.group(2))
    toStack = int(command.group(3))
    ############
    # Part 1
    for _ in range(count):
        stacks1[toStack].append(stacks1[fromStack].pop())
    
    ############
    # Part 2
    stacks2[toStack].extend(stacks2[fromStack][-1 * count:])
    del stacks2[fromStack][-1 * count:]


result1 = result1.join([line[-1] for line in stacks1[1:]])
result2 = result2.join([line[-1] for line in stacks2[1:]])

print(result1)   # Correct answer: TLFGBZHCN
print(result2)   # Correct answer: 