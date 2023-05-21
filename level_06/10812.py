n, m = map(int, input().split())
baskets = [x+1 for x in range(n)]
for i in range(m):
    i, j, k = map(int, input().split())
    baskets[i-1:j] = baskets[k-1:j] + baskets[i-1:k-1]
for j in baskets:
    print(j, end=" ")