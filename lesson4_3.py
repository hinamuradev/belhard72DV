# Заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name" и "email",
# а значения для этих ключей будут браться с клавиатуры
n = int(input("Введите число: "))
my_dict = {n: [{"Name": values1 for values1 in input("Введите Имя")},{"Email": values2 for values2 in input("Введите мыло")}] for n in range(1, n+1)}
print(my_dict)
