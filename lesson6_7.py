# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

def sum_of_neighbors(numbers):
    result = []
    n = len(numbers)

    for i in range(n):
        left = numbers[(i - 1) % n]
        right = numbers[(i + 1) % n]
        result.append(left + right)

    return result

# Пример использования:
original_numbers = [1, 2, 3, 4, 5]
result_list = sum_of_neighbors(original_numbers)
print(result_list)
