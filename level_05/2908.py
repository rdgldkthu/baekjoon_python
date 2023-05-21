a, b = map(str, input().split())
nums = [int(x[::-1]) for x in [a, b]]
print(max(nums))