n, k = map(int, input().split())
cnt = 0 
res = 0
i = 1
while(cnt < k):
    if n % i == 0:
        res = i
        cnt += 1
    i += 1
    if i > n:
        break
if cnt < k:
    print(0)
else:
    print(res)