def isprime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def fsp(num): #find smallest prime divisor
    for i in range(2, num+1):
        if isprime(i) and num % i == 0:
            return i
n = int(input())
if n == 1:
    pass
else:
    while True:
        if isprime(n):
            print(n)
            break
        p = fsp(n)
        print(p)
        n = int(n / p)