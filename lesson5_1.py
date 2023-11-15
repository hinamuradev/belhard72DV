# Вывести первые N цисел кратные M и больше K
n = int(input())
m = int(input())
k = int(input())
for n in range(1, n + 1):
    if n % m == 0 and n > k:
        print(f"Числа {n} кратные числу {m} и больше {k}")