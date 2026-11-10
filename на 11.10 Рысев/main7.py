A = float(input("Введите размер стипендии: "))
B = float(input("Введите расходы на проживание: "))

summa = 0

for i in range(10):
    summa = summa + B - A
    B = B * 1.03

print("Необходимая сумма от родителей:", summa, "рублей")