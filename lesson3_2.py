# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
average = (float((a + b + c)/3))
print(round(average, 3))
