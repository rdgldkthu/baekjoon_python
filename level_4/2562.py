count = 0
max = 0
result = 0
while count < 9:
    num = int(input())
    if num > max:
        max = num
        result = count + 1
    count += 1
print(max)
print(result)