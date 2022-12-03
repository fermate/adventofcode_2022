import common

path = "inputs/day_03_input.txt"

fileContent = common.readFile(path)

def getPriorities(letter):
    priority = 0

    if (ord(letter) >= ord('a')):
        priority = ord(letter) - ord('a') + 1
    else:
        priority = ord(letter) - ord('A') + 27
    
    return priority

############
# Part 1
score1 = 0  # score for part 1

for line in fileContent:
    part1 = line[:len(line)/2]
    part2 = line[len(line)/2:]
    letter = list(set(part1)&set(part2))[0]
    
    score1 += getPriorities(letter)

print(score1)   # Correct answer: 8298


############
# Part 2
score2 = 0  # score for part 2

for i in range(len(fileContent)/3):
    part1 = fileContent[i * 3]
    part2 = fileContent[i * 3 + 1]
    part3 = fileContent[i * 3 + 2]

    letter = list(set(part1)&set(part2)&set(part3))[0]
    
    score2 += getPriorities(letter)

print(score2)   # Correct answer: 2708