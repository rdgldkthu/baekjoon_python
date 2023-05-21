n, m = map(int, input().split())
baskets = [x+1 for x in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    a = []
    b = []
    c = []
    if i > 1 and j < n:
        a = baskets[:i-1]
        b = baskets[i-1:j]
        c = baskets[j::]
    elif i == 1 and j == n:
        b = baskets
    elif i == 1 and j < n:
        b = baskets[:j]
        c = baskets[j::]
    elif i > 1 and j == n:
        a = baskets[:i-1]
        b = baskets[i-1:]
    b.reverse()
    baskets = a + b + c
result = ""
for x in baskets:
    result += str(x)
    result += " "
print(result)
