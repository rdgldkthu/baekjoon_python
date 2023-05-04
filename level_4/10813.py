n, m = map(int, input().split())
baskets = []
balls = ""
temp = 0
for num in range(n):
    baskets.append(num+1)
for exchange in range(m):
    i, j = map(int, input().split())
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp
for ball in range(n):
    balls += str(baskets[ball])
    balls += " "
print(balls)