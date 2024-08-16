from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    x -= 1
    y -= 1
    d = deque()
    d.append((x, y))
    miro[x][y] = 1

    while d:
        x, y = d.popleft()

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newX < n and 0 <= newY < m:
                if miro[newX][newY] == 1:
                    d.append((newX, newY))
                    miro[newX][newY] = miro[x][y] + 1

bfs(1, 1)
print(miro[n-1][m-1])
