n, b = input().split()
res = 0

numbers = {}
# Add 0~9 into numbers
for i in range(10):
    numbers[str(i)] = i

# Add 10~36 into numbers
for i in range(65,91):
    numbers[chr(i)] = i-55

# Add the value of each digit from right to left
for i in range(len(n)-1,-1,-1):
    digit = numbers[n[i]]
    res += digit*pow(int(b),len(n)-i-1)

print(res)