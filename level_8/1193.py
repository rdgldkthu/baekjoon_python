n = int(input())
l = 0  # l = n for n-th diagonal line
t = 1
for i in range(n+1):
    t += i
    if t > n:
        l = i
        break
sum = l + 1  # the sum of denomenator and numerator
if l % 2 == 0:
    num = int(n - (l*(l-1)/2 + 1) + 1)
else:
    num = int((l*(l+1)/2) - n + 1)
den = sum - num
print(f"{num}/{den}")