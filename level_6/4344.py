c = int(input())
for i in range(c):
    ci = list(map(int, input().split()))
    avg = sum(ci[1:]) / (len(ci)-1)
    cnt = 0
    for g in ci[1:]:
        if g > avg:
            cnt += 1
    pctg = cnt / (len(ci)-1)
    print(f"{pctg:.3%}")