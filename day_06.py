import common

path = "inputs/day_06_input.txt"

fileContent = common.readFile(path)

def getFirstUnique(length):
    result = 0
    for i in range(len(fileContent[0])):
        a = fileContent[0][i:i + length]
        if (len(set(list(a))) == length):
            result = i + length
            return result

############
# Part 1
result1 = getFirstUnique(4)

############
# Part 2
result2 = getFirstUnique(14)

print(result1)   # Correct answer: 1909
print(result2)   # Correct answer: 3380