n = int(input())
student = []

for _ in range(n):
    name, score = input().split()
    student.append((name, int(score)))

student.sort(key=lambda x: x[1])

for name, score in student:
    print(name, end=" ")
