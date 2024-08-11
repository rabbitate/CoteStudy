money = [500, 100, 50, 10]
n = int(input())
answer = 0

for coin in money:
    answer += n // coin
    n = n % coin

# 아래 코드는 비효율적
# while n > 0:
#     for m in money:
#         if n >= m:
#             answer += n // m
#             n = n % m
#             break

print(answer)
