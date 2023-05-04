n, m = map(int, input().split())
baskets = []
balls = ""
for _ in range(n):
    baskets.append(0)
for u in range(m):
    i, j, k = map(int, input().split())
    for v in range(i-1,j):
        baskets[v] = k
for ball in range(n):
    balls += str(baskets[ball])
    balls += " "
print(balls)