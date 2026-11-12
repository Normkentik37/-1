n = int(input())
m = int(input())
for i in range(1, n+1):
    for j in range(m - i +1):
        b = m - i -j 
        if i * 5 + j * 10 + b * 20 == n:
         print(i, j, b)