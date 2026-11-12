n = int(input())

best_road = 1
best_height = 0

for i in range(1, n + 1):
    k = int(input())

min_height = 10**9

for j in range(k):
    h = int(input())
    min_height = min(min_height, h)

if min_height > best_height:
    best_height = min_height
    best_road = i
print(best_road, best_height)