import sys

n = int(input())
plans = list(sys.stdin.readline().strip())
x = y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

directions = ['L', 'R', 'U', 'D']

for plan in plans:
    # 가독성이 더 좋은 코드로 변경
    for i in range(4):
        if plan == directions[i]:
            newX = x + dx[i]
            newY = y + dy[i]
            break
    if newX < 1 or newX > n or newY < 1 or newY > n:
        continue
    x = newX
    y = newY

    # if plan == 'L':
    #     y -= 1
    # if plan == 'R':
    #     y += 1
    # if plan == 'U':
    #     x -= 1
    # if plan == 'D':
    #     x += 1
    
    # if x > 5:
    #     x = 5
    # if y > 5:
    #     y = 5
    # if x < 1:
    #     x = 1
    # if y < 1:
    #     y = 1

print(x, y)
