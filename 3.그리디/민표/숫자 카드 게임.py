import sys

n, m = map(int, input().split())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
value = 0

for i in range(n):
    if i == 0:
        value = min(numbers[i])
    else:
        value = max(value, min(numbers[i]))

print(value)
