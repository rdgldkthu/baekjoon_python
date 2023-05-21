while True:
    n = int(input())
    if n == -1:
        break
    str_out = f'{n} = 1'
    int_out = 1
    for i in range(2,n):
        if n % i == 0:
            str_out += f' + {str(i)}'
            int_out += i
    if int_out == n:
        print(str_out)
    else:
        print(f'{n} is NOT perfect.')