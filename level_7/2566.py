import sys
max_val = -1
x = 0
y = 0
for row in range(9):
    col = list(map(int, sys.stdin.readline().split()))
    if max(col) > max_val:
        max_val = max(col)
        x = row + 1
        y = col.index(max_val) + 1
print(max_val)
print(x, y)