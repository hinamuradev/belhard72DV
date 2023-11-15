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

# **Вывести четные числа от 2 до N по 5 в строку
n = int(input("Введите N: "))
num = []
for n in range(2, n+1):
    if n % 2 == 0:
        num.append(n)
print(num)
