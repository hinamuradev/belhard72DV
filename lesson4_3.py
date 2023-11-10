# Заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name" и "email",
# а значения для этих ключей будут браться с клавиатуры
n = int(input("Введите число: "))
my_dict = {}
for num in range(1, n + 1):
    name = input("name")
    email = input("email")
    nested_dict = {"name": name, "email": email}
    my_dict[num] = nested_dict
print(my_dict)
