word = input().upper()
alph = {}
for i in word:
    if i not in alph.keys():
        alph[i] = 1
    else:
        alph[i] += 1
m = max(alph.values())
max_value_count = 0
max_value_key = ""
for k, v in alph.items():
    if v == m:
        max_value_count += 1
        max_value_key = k
if max_value_count > 1:
    print("?")
else:
    print(max_value_key)