import sys

n, k = map(int, input().split())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))

arrA.sort()
arrB.sort(reverse=True)

for i in range(k):
    if arrA[i] < arrB[i]:
        arrA[i] = arrB[i]
    else: break

print(sum(arrA))
