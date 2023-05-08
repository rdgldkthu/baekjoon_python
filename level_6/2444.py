'''
n = int(input())
for i in range(1, 2*n):
    stars = "*" * ((2*n-1) - 2*abs(n-i))
    print(f"{stars:^{2*n-1}s}")
'''
n = int(input())
for i in range(1, 2*n):
    blanks = " " * abs(n-i)
    stars = "*" * ((2*n-1) - 2*abs(n-i))
    print(blanks + stars)
