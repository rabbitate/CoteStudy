# def transTime(time):
#     sec = time % 60
#     if time // 60 > 60:
#         hour = time // 3600
#         min = time // 60 % 60
#     else:
#         hour = 0
#         min = time // 60

#     for h in str(hour):
#         if h == '3':
#             return True
        
#     for m in str(min):
#         if m == '3':
#             return True
        
#     for s in str(sec):
#         if s == '3':
#             return True
    
#     return False
    
# n = int(input())
# answer = 0

# for i in range((n+1) * 3600):
#     if transTime(i):
#         answer += 1

# 가독성이 더 좋은 코드로 변경

n = int(input())
answer = 0

for hour in range(n+1):
    for min in range(60):
        for sec in range(60):
            if '3' in str(hour) + str(min) + str(sec):
                answer += 1

print(answer)
