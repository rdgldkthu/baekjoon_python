h, m = map(int, input().split())
t = int(input())

def oven(h, m, t):
    if (m + t) < 60:
        return [h, m+t]
    else:
        h0 = (m + t)/60
        m0 = (m + t)%60
        if (h + h0) > 23:
            return [(h + h0)%24, m0]
        else:
            return [(h + h0), m0]

hh, mm = map(int, oven(h, m, t))
print(hh, mm)

