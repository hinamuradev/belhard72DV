# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

lists = ["gfdgdf", 12 , 34, "fdsfsd"]

def is_onn(word):
    words = []
    for n in lists:
        if type(n) == str:
            words.append(n)
    print(words)

is_onn(1)

