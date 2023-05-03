mods = []
for _ in range(10):
    num = int(input())
    mod = num % 42
    if mod not in mods:
        mods.append(mod)
    else:
        continue
print(len(mods))