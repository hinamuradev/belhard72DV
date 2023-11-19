# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом

def random_list(numbers):
    chet = []
    nechet = []
    n = len(numbers)
    for i in range(n):
        if i % 2 == 0 and i != 0:
            chet.append(i)
        else :
            if i != 0:
                nechet.append(i)
    print(chet)
    print(nechet)


lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 87, 78]
result = random_list(lists)
print(result)
