# Вывести первые N чисел кратные M и больше K
n = int(input())
m = int(input())
k = int(input())

while True:
    if n % m == 0 and n > k:
        print(f"Числа {n} кратные числу {m} и больше {k}")
        break
    else:
        print("loh")
        break