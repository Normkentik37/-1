n = int(input())
S = int(input())
summa = 0
norma = 10
for i in range(S):
    summa += norma
    norma += norma * 0.1 
print(summa)