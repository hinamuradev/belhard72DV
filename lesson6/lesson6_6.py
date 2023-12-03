# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом

def sort(x):
    return (x % 2, x)

random_numbers = [5, 2, 7, 4, 1, 8, 3, 6]
sorted_numbers = sorted(random_numbers, key=sort)
print(sorted_numbers)
