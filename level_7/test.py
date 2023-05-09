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