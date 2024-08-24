import sys

def binarySearch(start, end, target):
    if start > end:
        return "no"
    
    mid = (start + end) // 2

    if parts[mid] == target:
        return "yes"
    elif parts[mid] < target:
        return binarySearch(mid+1, end, target)
    elif parts[mid] > target:
        return binarySearch(start, mid-1, target)

n = int(input())
parts = list(map(int, sys.stdin.readline().split()))
m = int(input())
needParts = list(map(int, sys.stdin.readline().split()))

parts.sort()

for p in needParts:
    print(binarySearch(0, len(parts)-1, p), end=" ")
