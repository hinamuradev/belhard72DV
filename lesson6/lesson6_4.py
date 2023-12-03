# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

def filter_strings_in_place(input_list):
    i = 0
    while i < len(input_list):
        if not isinstance(input_list[i], str):
            input_list.pop(i)
        else:
            i += 1

mixed_list = [1, 'apple', 3.14, 'banana', True, 'orange', [1, 2, 3]]
filter_strings_in_place(mixed_list)
print(mixed_list)
