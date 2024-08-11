import sys
n, m, k = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
answer = 0
limit = 0

for _ in range(m):
    if limit < k:
        answer += numbers[-1]
        limit += 1
    elif limit == k:
        answer += numbers[-2]
        limit = 0

print(answer)
