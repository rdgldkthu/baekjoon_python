a, b, c = map(int, input().split())

l = [a, b, c]
l.sort()

num = 0
reps = 0

for i in l:
    if l.count(i) > reps:
        num = i
        reps = l.count(i)

if reps == 3:
    award = 10000 + num*1000
elif reps == 2:
    award = 1000 + num*100
else:
    award = l[-1] * 100

print(award)
