def isgroup(str):
    id = {}
    for i in range(len(str)):
        if str[i] not in id.keys():
            id[str[i]] = list()
        id[str[i]].append(i)
    for i in id.keys():
        if len(id[i]) == 1:
            continue
        for j in range(len(id[i])-1):
            if id[i][j] != id[i][j+1] - 1:
                return 0
    return 1

res = 0
for _ in range(int(input())):
    res += isgroup(input())
print(res)