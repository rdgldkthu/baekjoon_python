word = input().upper()
secs = {"ABC":3,"DEF":4,"GHI":5,"JKL":6,"MNO":7,"PQRS":8,"TUV":9,"WYXZ":10}
time = 0
for l in word:
    for key in secs.keys():
        if l in key:
            time += secs[key]
print(time)