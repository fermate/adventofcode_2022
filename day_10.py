import common

path = "inputs/day_10_input.txt"

fileContent = common.readFile(path)
crt = ''

currentCycle = 0
currentValue = 1
strengthSum = 0

for line in fileContent:
    command = line.split(' ')

    cycleIncrement = 0

    if (command[0] == 'noop'):
        cycleIncrement = 1
    if (command[0] == 'addx'):
        cycleIncrement = 2 

    for _ in range(cycleIncrement):
        currentCycle += 1

        # For part 2
        if (currentCycle % 40 in [currentValue +2, currentValue, currentValue + 1]):
            crt += '#'
        else:
            crt += '.'

        # For part 1
        if (currentCycle % 40 == 20):
            strengthSum += currentCycle * currentValue
    
    if (command[0] == 'addx'):
        currentValue += int(command[1])


print(strengthSum)   # Correct answer par1: 14820

# Printing out part 2
width = 40
for i in range(0, len(crt), width):
    print(crt[i:i + width])   # Correct answer part2: RZEKEFHA

