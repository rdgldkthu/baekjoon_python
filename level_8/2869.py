a, b, v = map(int, input().split())
v -= a # subtract one full length that can be traveled in a day
full_days = v/(a-b) # number of full travels(a-b) needed for the rest
if v%(a-b) == 0:
    print(int(full_days)+1) #if no remainder, add one day 
else:
    print(int(full_days)+2) #if remainder, need two more days