# Без использования collections, написать программу, которая будет создавать словарь
# для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры
text = input()
# objs = dict.fromkeys(text, 0)
# for i in text:
#     objs[i] += 1
# print(objs)
objs = {i : text for i in text}
print(objs)
