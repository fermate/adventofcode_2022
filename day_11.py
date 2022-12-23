import numpy as np

import common


########
## Additional class
class Monkey:
    def __init__(self, items, operation, divisionNumber, trueMonkey, falseMonkey) -> None:
        self.items = items
        self.operation = operation
        self.divisionNumber = divisionNumber
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.inspectionNumber = 0
        pass


def getItems(itemLine):
    items = itemLine[16:].split(', ')
    return [int(element) for element in items]

path = "inputs/day_11_input.txt"

fileContent = common.readFile(path)

monkeys1 = []
monkeys2 = []

########
## Processing the input file
items = []
operation = ''
divisionNumber = 0
trueMonkey = -1
falseMonkey = -1
for line in fileContent:
    line = line.strip()
    a = line.split(' ')

    match a[0]:
        case 'Starting':
            items = getItems(line)
        case 'Operation:':
            operation = line[17:]
        case 'Test:':
            divisionNumber = int(a[-1])
        case 'If':
            match a[1]:
                case 'true:':
                    trueMonkey = int(a[-1])
                case 'false:':
                    falseMonkey = int(a[-1])

    if line == '':
        monkeys1.append(Monkey(items, operation, divisionNumber, trueMonkey, falseMonkey))
        monkeys2.append(Monkey(items, operation, divisionNumber, trueMonkey, falseMonkey))
        
        items = []
        divisionNumber = 0
        trueMonkey = -1
        falseMonkey = -1

# Adding the last monkey
monkeys1.append(Monkey(items, operation, divisionNumber, trueMonkey, falseMonkey))
monkeys2.append(Monkey(items, operation, divisionNumber, trueMonkey, falseMonkey))

# Part 1
for _ in range(20):
    for m in monkeys1:
        itemCount = len(m.items)
        m.inspectionNumber += itemCount
        for _ in range(itemCount):
            old = m.items.pop(0)
            new = eval(m.operation)
            new = int(new / 3)
            if new % m.divisionNumber == 0:
                monkeys1[m.trueMonkey].items.append(new)
            else:
                monkeys1[m.falseMonkey].items.append(new)

inspected1 = [m.inspectionNumber for m in monkeys1]
inspected1.sort()

# Part 2
mod = np.lcm.reduce([m.divisionNumber for m in monkeys2])

for _ in range(10000):
    for m in monkeys2:
        itemCount = len(m.items)
        m.inspectionNumber += itemCount
        for _ in range(itemCount):
            old = np.uint64(m.items.pop(0))
            new = np.uint64(eval(m.operation))
            if new % m.divisionNumber == 0:
                monkeys2[m.trueMonkey].items.append(new % mod)
            else:
                monkeys2[m.falseMonkey].items.append(new % mod)

inspected2 = [m.inspectionNumber for m in monkeys2]
inspected2.sort()

print(inspected1[-1] * inspected1[-2])   # Correct answer for part1: 50172
print(inspected2[-1] * inspected2[-2])   # Correct answer for part1: 


# 11613109605 > x > 13272292845 


# 11614682178 ??