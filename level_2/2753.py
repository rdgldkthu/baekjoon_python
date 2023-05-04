def isleap(num):
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
    
year = int(input())
print(isleap(year))
    