import sys

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

gameMap = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
directionList = [0, 3, 2, 1]
moveList = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for i in range(len(directionList)):
    if direction == directionList[i]:
        directionIndex = i
        
answer = 1

while True:
    visited[x][y] = True

    for i in range(4):
        if directionIndex == len(directionList)-1:
            directionIndex = 0
        else:
            directionIndex += 1

        newX = x + moveList[directionIndex][0]
        newY = y + moveList[directionIndex][1]

        if gameMap[newX][newY] == 1 or visited[newX][newY]:
            continue
        else:
            x = newX
            y = newY
            answer += 1
            break
    else:
        newX = x - moveList[directionIndex][0]
        newY = y - moveList[directionIndex][1]

        if gameMap[newX][newY] == 1:
            break
        else:
            x = newX
            y = newY

print(answer)
