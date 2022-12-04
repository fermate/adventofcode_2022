import common

path = "inputs/day_04_input.txt"

fileContent = common.readFile(path)


score1 = 0  # score for part 1
score2 = 0  # score for part 2

for line in fileContent:
    elfs = line.split(',')
    section1 = elfs[0].split('-')
    section2 = elfs[1].split('-')

    section1 = [int(s) for s in section1]
    section2 = [int(s) for s in section2]

############
# Part 1
    range1 = range(section1[0], section1[1] + 1)
    range2 = range(section2[0], section2[1] + 1)
    
    fullRange = list(set(range1) & set(range2))

    if(len(fullRange) == len(range1) or len(fullRange) == len(range2)):
        score1 += 1


############
# Part 2
    if((section1[1] >= section2[0]) and 
       (section1[0] <= section2[1])):
        score2 += 1

# end of for


print(score1)   # Correct answer: 547
print(score2)   # Correct answer: 843