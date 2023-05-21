str = input()
res = len(str)
cro = {'c=': 1, 'c-': 1, 'dz=': 2, 'd-': 1, 'lj': 1, 'nj': 1, 's=': 1, 'z=': 1}
for i in cro.keys():
    if i in str:
        res -= cro[i] * str.count(i)
if 'dz=' in str and 'z=' in str:
    res += str.count('dz=')
print(res)