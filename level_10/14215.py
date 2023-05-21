def isvalid(a, b, c):
    return (a+b > c) and (a+c > b) and (b+c > a)


a, b, c = map(int, input().split())
l = sorted([a, b, c])
while True:
    if isvalid(l[0], l[1], l[2]):
        print(sum(l))
        break
    l[-1] -= 1