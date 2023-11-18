# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
def revers(n):
    newlist = [1, 2, 3, 4, 5, 6, 7]
    newlist = newlist[n:] + newlist[:n]
    return newlist

print(revers(int(input())))
