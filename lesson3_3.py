# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
name = input("Как вас зовут ")
age = input("Сколько лет ")
city = input("Город ваш ")
# 1 способ
print("Здравствуйте Я " + name + "\n" + "Мне " + age + "\n" + "Я живу в городе: " + city)
# 2 способ
print("Здравствуйте Я %s \n Мне %s \n Я живу в городе: %s" % (name, age, city))
# 3 способ
print(f"Здравствуйте Я {name}\n Мне {age}\n Я живу в городе: {city}")
