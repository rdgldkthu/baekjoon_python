n = int(input())
a = list(map(int, input().split()))
max = a[0]
min = a[0]
for i in range(n):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
result = str(min) + " " + str(max)
print(result)