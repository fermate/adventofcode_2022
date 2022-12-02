import common

path = "inputs/day_01_input.txt"

fileContent = common.readFile(path)

fileContent = common.makeInt(fileContent)

elfs = []

calories = 0

for line in fileContent:
    if line:
        calories = calories + line
    else:
        elfs.append(calories)
        calories = 0

elfs.append(calories)

# only for part 1
# max = 0
# for elf in elfs:
#     if elf > max:
#         max = elf

elfs.sort(reverse=True)

#part 1 answer
print(elfs[0])

#part 2 answer
print(elfs[0] + elfs[1] + elfs[2])
