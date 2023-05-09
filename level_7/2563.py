'''
def overlap(x1, y1, x2, y2, w=10, h=10):
    if x1 > x2:
        xx = x1
        dx = abs(w + x2 - x1)
    else:
        xx = x2
        dx = abs(w + x1 - x2)
    if y1 > y2:
        yy = y1
        dy = abs(h + y2 - y1)
    else:
        yy = y2
        dy = abs(h + y1 - y2)
    if x1 == x2 and y1 == y2:
        return [w*h, xx, yy, dx, dy]
    else:
        return [(dx * dy) % (w*h), xx, yy, dx, dy]
n = int(input())
coor = []
ovl = []
res = 100 * n
for _ in range(n):
    coor.append(list(map(int, input().split())))
for i in range(n-1):
    for j in range(i,n):
        if i == j:
            continue
        union = overlap(coor[i][0], coor[i][1], coor[j][0], coor[j][1])
        ovl.append(union)
        res -= union[0]
# overlap된 overlap의 면적 다시 추가해줘야 함 - overlap 함수 수정 필요
print(res)
'''
n = int(input())
pal = [[0 for x in range(100)] for y in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            pal[i][j] = 1
res = 0
for l in pal:
    res += sum(l)
print(res)