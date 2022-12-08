import common

class Element:
    name = ""
    size = 0
    children = None
    isFile = True
    parent = None

    def __init__(self, name, parent, isFile = False, size = 0):
        self.name = name
        self.size = size
        self.isFile = isFile
        self.parent = parent
        if(not isFile):
            self.children = []
        pass


# end of class

path = "inputs/day_07_input.txt"

fileContent = common.readFile(path)

result1 = 0
result2 = 0

root = Element('root', False)
pointer = root

# Build the file structure
for line in fileContent:
    if (line.startswith('$')):  # command mode    
        if (line.startswith("$ cd")):
            a = line.split(' ')
            toName = a[2]
            if (toName == '/'):
                pointer = root
            elif(toName == '..'):
                pointer = pointer.parent
            else:
                pointer = [g for g in pointer.children if g.name == toName][0]
    else: # list mode
        item = line.split(' ')
        e = Element(item[1], pointer)
        if (item[0] != 'dir'): # it is a folder
            e.isFile = True
            e.size = item[0]
        pointer.children.append(e)

############
# Part 1
def countSize(folder):
    size = 0
    for item in folder.children:
        if (item.isFile):
            size += int(item.size)
        else:
            size += countSize(item)
    folder.size = size
    if(size <= 100000):
        global result1
        result1 += size
    return size


############
# Part 2
def findSmallest(folder):
    global result2
    for item in folder.children:
        if (int(item.size) > int(needed) and int(item.size) < int(result2)):
            result2 = int(item.size)
        if (not item.isFile):
            findSmallest(item)
    pass

############
# The result
countSize(root)

needed = root.size - 40000000
result2 = root.size
findSmallest(root)

print(result1)   # Correct answer: 1334506
print(result2)   # Correct answer: 7421137