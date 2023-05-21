n = int(input())
coin_val = (25, 10, 5, 1)

while n:
    C = int(input())
    changes = [0, 0, 0, 0]
    for i in range(4):
        if C >= coin_val[i]:
            changes[i] = int(C / coin_val[i])
        C = C % coin_val[i]

    for j in changes:
        print(j, end=' ')
    print('')
    n -= 1