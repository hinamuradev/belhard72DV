# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
# 1 Способ
text = input()
word = text.split()
text1 = '-'.join(word)
print(text1)
# 2 способ
name = input()
wordout = name.replace(' ', '-')
print(wordout)
