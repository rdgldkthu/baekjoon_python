a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 == 0:
    if a0 <= c*n0:
        print(1)
    else:
        print(0)
else:
    if a1 > c:
        print(0)
    else:
        if a1*n0 + a0 <= c*n0:
            print(1)
        else:
            print(0)