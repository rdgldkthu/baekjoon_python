from sys import stdin
words = [[' ' for x in range(15)] for y in range(5)]
longest = 0
for i in range(5):
    col = list(map(str, stdin.readline().rstrip()))
    l = len(col)
    if l > longest:
        longest = l
    words[i][:l] = col
for i in range(longest):
    for j in range(5):
        letter = words[j][i]
        if letter != ' ':
            print(letter, end="")