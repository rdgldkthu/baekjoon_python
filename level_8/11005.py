n, b = map(int, input().split())

numbers = {}
for i in range(10):
    numbers[i] = str(i)
for i in range(65, 91):
    numbers[i - 55] = chr(i)

if b == 10:
    print(str(n))
else:
    remainders = []
    
    while n != 0:
        remainders.append(n%b)
        n = int(n/b)
    for i in remainders[::-1]:
        print(numbers[i],end="")
    print('')