n = int(input())
d = (n-1)/6
for i in range(n):
    a = i*(i+1)/2
    if a >= d:
        print(i+1)
        break