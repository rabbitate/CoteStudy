import sys

n, m = map(int, input().split())
iceMold = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def dfs(x, y):
    iceMold[x][y] = 1

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if 0 <= newX < n and 0 <= newY < m and iceMold[newX][newY] != 1:
            dfs(newX, newY)

for i in range(n):
    for j in range(m):
        if iceMold[i][j] == 0:
            dfs(i, j)
            answer += 1

print(answer)
