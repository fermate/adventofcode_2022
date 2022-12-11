import numpy as np
import math
import common


########
## Additional class
class Point:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y
        pass

    def moveLeft(self):
        self.x -= 1

    def moveRight(self):
        self.x += 1

    def moveUp(self):
        self.y += 1

    def moveDown(self):
        self.y -= 1

    def moveX(self, step):
        self.x += step
    
    def moveY(self, step):
        self.y += step

    def move(self, p):
        self.x += p.x
        self.y += p.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def moveTowards(self, p):
        if p.x > self.x:
            self.x += 1
        elif p.x < self.x:
            self.x -= 1

        if p.y > self.y:
            self.y += 1
        elif p.y < self.y:
            self.y -= 1

    def distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.hypot(dx, dy)


## End of the class

path = "inputs/day_09_input.txt"

fileContent = common.readFile(path)

distances = {
    'L': 0,
    'R': 0,
    'U': 0,
    'D': 0
}
for line in fileContent:
    a = line.split(' ')
    distances[a[0]] += int(a[1])

visitedCountPart1 = np.zeros((distances['U'] + distances['D'], distances['L'] + distances['R']))
visitedCountPart1[0,0] = 1
visitedCountPart2 = np.zeros((distances['U'] + distances['D'], distances['L'] + distances['R']))
visitedCountPart2[0,0] = 1

head = Point()
tail = Point()
long = [Point()] * 10
for line in fileContent:
    a = line.split(' ')
    
############
# Mixed solution
    for _ in range(int(a[1])):
        match a[0]:
            case 'L':
                head.moveLeft()     # Part 1
                long[0].moveLeft()  # Part 2
            case 'R':
                head.moveRight()    # Part 1
                long[0].moveRight() # Part 2
            case 'U':
                head.moveUp()       # Part 1
                long[0].moveUp()    # Part 2
            case 'D':
                head.moveDown()     # Part 1
                long[0].moveDown()  # Part 2

        # Part 1 moving the tail
        if(head.distance(tail) >= 2):
            tail.moveTowards(head)
            visitedCountPart1[tail.x, tail.y] = 1

        # Part 2 moving the rest
        for i in range(1,10):
            if (long[i-1].distance(long[i]) >= 2):
                long[i].moveTowards(long[i-1])
                if (i == len(long) - 1):
                    visitedCountPart2[long[i].x, long[i].y] = 1

# end of for


print(np.sum(visitedCountPart1))   # Correct answer: 5779
print(np.sum(visitedCountPart2))   # Correct answer: 2331