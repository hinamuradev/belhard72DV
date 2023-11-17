# Вывести первые N чисел кратные M и больше K
n = int(input())
m = int(input())
k = int(input())

while k > 0:
    if n % m == 0:
        print(f"Числа {n} кратные числу {m} и больше {k}")
        break
    else:
        print("loh")