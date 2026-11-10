import math
k = float(input())
h = float(input())
y = 2
while y <= 3:
    a = math.acos(y / k )
    a = math.degrees(a)
    print(y, a)
    y += h