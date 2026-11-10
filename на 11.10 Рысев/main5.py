n = 0 
k = 0 
d = 0 
for n in range(1, 11):
    for k in range(1, 21):
        for d in range(1, 201):
            if n * 10 + k * 5 + d * 0.5 == 100: 
                if n + k + d == 100:
                    print(n, k, d)