n = int(input())
scores = list(map(int, input().split()))
average = sum(scores)/n
m = max(scores)
new_average = average/m*100
print(new_average)