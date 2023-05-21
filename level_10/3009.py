xx = {}
yy = {}
for _ in range(3):
    x, y = map(int, input().split())
    if x not in xx.keys():
        xx[x] = 1
    else:
        xx[x] += 1
    if y not in yy.keys():
        yy[y] = 1
    else:
        yy[y] += 1
x = [i for i in xx.keys() if xx[i] == 1]
y = [j for j in yy.keys() if yy[j] == 1]
print(x[0], y[0])