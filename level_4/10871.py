n, x  = map(int, input().split())
a = list(map(int, input().split()))
b = ""
for i in range(n):
    if a[i] < x:
        b += str(a[i])
        b += " "
print(b)
