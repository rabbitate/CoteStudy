import sys

n, m = map(int, input().split())
ricecake = list(map(int, sys.stdin.readline().split()))
answer = 0

# 반복문으로 구현
# for i in range(max(ricecake), 0, -1):
#     amount = 0
#     for r in ricecake:
#         if r > i:
#             amount += r - i
#     if amount == m:
#         answer = i
#         break

start = 0
end = max(ricecake)

while(start <= end):
    mid = (start + end) // 2
    amount = 0

    for r in ricecake:
        if r > mid:
            amount += r - mid

    if amount >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
