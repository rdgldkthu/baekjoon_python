def isprime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
m = int(input())
n = int(input())
sum = 0
mini = n
for i in range(m, n+1):
    if isprime(i):
        sum += i
        if i < mini:
            mini = i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(mini)