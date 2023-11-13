# Заполнить список степенями числа 2( от 2^1 до 2^n)
n = int(input("Введите n: "))
my_list = [2**n for n in range(1, n+1)]
print(my_list)
