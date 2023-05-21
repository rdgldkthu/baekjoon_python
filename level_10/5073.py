def valid_triangle(a, b, c):
    return (a+b > c) and (a+c > b) and (b+c > a)


def euqilateral(a, b, c):
    return a == b == c


def isosceles(a, b, c):
    return (a == b and a != c) or (a == c and a != b) or (b == c and b != a)


while True:
    a, b, c = map(int, input().split())
    if a+b+c == 0:
        break
    if not valid_triangle(a, b, c):
        print("Invalid")
    elif euqilateral(a, b, c):
        print("Equilateral")
    elif isosceles(a, b, c):
        print("Isosceles")
    else:
        print("Scalene")