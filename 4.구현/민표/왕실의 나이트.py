position = input()
x = ord(position[0]) - ord('a')
y = int(position[1]) 
limit = 8
answer = 0

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

answer = 0

for i in range(len(dx)):
    newX = x + dx[i]
    newY = y + dy[i]

    if 1 <= newX <= limit and 1 <= newY <= limit:
        answer += 1

print(answer)
