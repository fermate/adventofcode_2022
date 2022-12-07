def readFile(fileName, toStrip = True):
    fileContent = []
    with open(fileName) as inputFile:
        fileContent = inputFile.readlines()
    
    if (toStrip):
        for i in range(len(fileContent)):
            fileContent[i] = fileContent[i].rstrip()
    
    return fileContent

def makeInt(array):
    for i in range(len(array)):
        if array[i]:
            array[i] = int(array[i])
    return array


# a = 1
# x = 1
# g = True

# while (g):
#     if(13*a - 7*x > 1):
#         x += 1
#     elif(13*a - 7*x < 1):
#         a += 1
#     else:
#         g = False

# print(str(a) + " + " + str(x))