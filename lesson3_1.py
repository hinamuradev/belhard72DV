# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
# 1 Способ
text = input()
word = text.split()
textlist = '-'.join(word)
print(textlist)
# 2 способ
name = input()
wordout = name.replace(' ', '-')
print(wordout)
