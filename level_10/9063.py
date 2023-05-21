N = int(input())
x, y = map(int, input().split())
n, s = y, y
e, w = x, x
for _ in range(N - 1):
    x, y = map(int, input().split())
    if x > e:
        e = x
    if x < w:
        w = x
    if y > n:
        n = y
    if y < s:
        s = y
print((n - s) * (e - w))