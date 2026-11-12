n = int(input())
k = int(input())
symb = input()
for i in range(n):
    if i == 0 or i == n - 1:
        print(symb * k)
    else:
        print(symb + " " * (k-2) + symb)