p = int(input())
for i in range(p):
    r, s = map(str, input().split())
    for l in s:
        print(l*int(r), end="")
    print("")