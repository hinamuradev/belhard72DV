# **Вывести четные числа от 2 до N по 5 в строку
n = int(input("Введите N: "))
num = []
for n in range(2, n+1):
    if n % 2 == 0:
        num.append(n)
print(num)
