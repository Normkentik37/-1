for x in range(29):
    a = 2 * x ** 2 + 29
    prostoe = True
for i in range(2, a):
    if a % i == 0:
        prostoe = False
        break
    if prostoe:
        print(a)