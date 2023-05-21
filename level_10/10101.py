angles = {}
asum = 0
for _ in range(3):
    a = int(input())
    asum += a
    if a not in angles.keys():
        angles[a] = 1
    else:
        angles[a] += 1
if asum != 180:
    print('Error')
else: 
    if 3 in angles.values():
        print('Equilateral')
    elif 2 in angles.values():
        print('Isosceles')
    else:
        print('Scalene')