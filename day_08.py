import numpy as np
import common

path = "inputs/day_08_input.txt"

fileContent = common.readFile(path)

# make array from map ( map string array to int map(make an array of string from a long string))
fileContent = [list(map(int, list(num))) for num in fileContent]

rowCount = len(fileContent)
colCount = len(fileContent[0])
max = rowCount if rowCount > colCount else colCount

padding = ((0, max - rowCount), (0, max - colCount))

fileContent = np.pad(fileContent, padding, mode = 'constant', constant_values = -1)
seenCount = np.zeros((max, max))

maxViewingDistance = 0

for i in range(max):
    leftHighest = -1
    topHighest = -1
    rightHighest = -1
    bottomHighest = -1
    
    k = max - (i + 1)

    for j in range(max):
        l = max - (j + 1)

############
# Part 1

        # Looking from the left
        if (fileContent[i, j] > leftHighest and fileContent[i, j] != -1):
            leftHighest = fileContent[i, j]
            seenCount[i, j] = 1
        
        # Looking from the top
        if (fileContent[j, i] > topHighest and fileContent[j, i] != -1):
            topHighest = fileContent[j, i]
            seenCount[j, i] = 1
        
        # Looking from the rigth
        if (fileContent[k, l] > rightHighest and fileContent[k, l] != -1):
            rightHighest = fileContent[k, l]
            seenCount[k, l] = 1
        
        # Looking from the bottom
        if (fileContent[l, k] > bottomHighest and fileContent[l, k] != -1):
            bottomHighest = fileContent[l, k]
            seenCount[l, k] = 1

############
# Part 2
        if (i == 0 or j == 0 or i == max - 1 or j == max - 1):
            continue

        leftViewingDist = 1
        topViewingDist = 1
        rightViewingDist = 1
        bottomViewingDist = 1
        leftSee = True
        topSee = True
        rightSee = True
        bottomSee = True
        currHeight = fileContent[i,j]
        while (leftSee or topSee or rightSee or bottomSee):
            if (fileContent[i, j - leftViewingDist] < currHeight and j - leftViewingDist > 0):
                leftViewingDist += 1
            else: 
                leftSee = False

            if (fileContent[i - topViewingDist, j] < currHeight and i - topViewingDist > 0):
                topViewingDist += 1
            else: 
                topSee = False
                
            if (fileContent[i, j + rightViewingDist] < currHeight and j + rightViewingDist < max - 1):
                rightViewingDist += 1
            else: 
                rightSee = False
                
            if (fileContent[i + bottomViewingDist, j] < currHeight and i + bottomViewingDist < max - 1):
                bottomViewingDist += 1
            else: 
                bottomSee = False

            pass

        currViewingDistance = leftViewingDist * rightViewingDist * topViewingDist * bottomViewingDist
        if (currViewingDistance > maxViewingDistance):
            maxViewingDistance = currViewingDistance

# end of for


print(np.sum(seenCount))   # Correct answer: 1840
print(maxViewingDistance)   # Correct answer: 405769
