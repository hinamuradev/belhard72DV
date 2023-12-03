# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
def reverse_list(input_list):
    left, right = 0, len(input_list) - 1

    while left < right:
        # Обмен значениями между левым и правым элементами
        input_list[left], input_list[right] = input_list[right], input_list[left]

        # Переход к следующей паре элементов
        left += 1
        right -= 1

# Пример использования:
my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print(my_list)