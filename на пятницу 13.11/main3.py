n = int(input("nach"))
k = int(input("koh"))
d = int(input("shag"))
for a in range(1, k+1, d):
    for b in range(1, k+1, d):
        print(a, "+", b,"=", a+b, end = "\t")
    print()