import common

path = "inputs/day_02_input.txt"

fileContent = common.readFile(path)

elf = ['A', 'B', 'C']
me = ['X', 'Y', 'Z']

# Part 1
score1 = 0  # score for part 1

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
    
# Part 2
score2 = 0  # score for part 2
toLose = [3, 1, 2]
toWin = [2, 3, 1]

for line in fileContent:
    answers = line.split(' ')
    elfA = elf.index(answers[0])

    if (answers[1] == 'X'):  # lose
        score2 += toLose[elfA]
    elif (answers[1] == 'Y'):  # draw
        score2 += (elfA + 1) + 3
    else:  # win
        score2 += 6 + toWin[elfA]

print(score2)