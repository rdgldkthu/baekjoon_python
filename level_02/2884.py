h, m = 99, 99
while (h not in range(0,24)) and (m not in range(0,60)):
    h, m = map(int, input().split())

def fourtyfive(h, m):
    if m >= 45:
        return [h, m-45]
    else:
        if h == 0:
            return [23, m+15]
        else:
            return [h-1, m+15]
        
hh, mm = map(int, fourtyfive(h, m))
print(hh, mm)