import common

path = "inputs/day_02_input.txt"

fileContent = common.readFile(path)

elf = ['A', 'B', 'C']
me = ['X', 'Y', 'Z']

score1 = 0  #score for part 1

# part 1
for line in fileContent:
    answers = line.split(' ')
    elfA = (elf.index(answers[0]) + 1) * 10
    meA = me.index(answers[1]) + 1

    sum = elfA + meA

    if (sum in [11, 22, 33]):
        score1 += 3
    elif (sum in (12, 23, 31)):
        score1 +=6

    score1 += meA

print(score1)
    