import numpy as np

dafaFile = "06/board.txt"
dafaFile = "06/data_small.txt"

"""
example:
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

directionms = ["^", ">", "v", "<"]
direction = 0

position = [0, 0]
board = []

def findPosition():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in directionms:
                position = [i, j]
                return position
    print("Position not found")
    return [-1, -1]
def updateDirection():
    global direction
    for i in range(len(directionms)):
        if board[position[0]][position[1]] == directionms[i]:
            direction = i
            return i
    print("Direction not found")
    direction = -1
    return -1

def getNextPosition():
    global direction
    __position = position.copy()
    if direction == 0:
        __position[0] -= 1
    elif direction == 1:
        __position[1] += 1
    elif direction == 2:
        __position[0] += 1
    elif direction == 3:
        __position[1] -= 1
    return __position
    
def isEnded():
    nextPosition = getNextPosition()
    if board[nextPosition[0]][nextPosition[1]] == "#":
        return True
    return False

def turnRight():
    global direction
    updateDirection()
    direction = (direction + 1) % 4
    board[position[0]][position[1]] = directionms[direction]

def move():
    # move one step forward
    global position
    board[position[0]][position[1]] = "X"

    getNextPosition()
    global direction

    if direction == 0:
        board[position[0] - 1][position[1]] = directionms[direction]
    elif direction == 1:
        board[position[0]][position[1] + 1] = directionms[direction]
    elif direction == 2:
        board[position[0] + 1][position[1]] = directionms[direction]
    elif direction == 3:
        board[position[0]][position[1] - 1] = directionms[direction]
  

def noObstacleAhead():
    nextPosition = getNextPosition()
    # check if it is out of the board

    if nextPosition[0] < 0 or nextPosition[0] >= len(board):
        return False

    # check if there is an obstacle ahead
    if board[nextPosition[0]][nextPosition[1]] == "#":
        return False
    return True

            
ans = 0

# read line by line
with open(dafaFile) as f1:
    board = np.array([list(line.strip()) for line in f1])

    while not isEnded():
        position = findPosition()
        print("Position: ", position)
        updateDirection()
        print("Direction: ", direction)
        if(noObstacleAhead()):
            move()
            ans += 1
        else:
            turnRight()
        print(board)
    


    





print("Answer: ", ans)
