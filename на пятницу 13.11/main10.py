n = int(input())
for i in range(2, n):
    prostoe = True
    for j in range(2, i):
        if i % j == 0:
            prostoe = False
            break
    if prostoe:
        print(i)