# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число списка Фибоначчи: '))
m = -1
def fibanacci(n):
    if n in [1,2]:
        return 1
    else:
        return fibanacci(n-1) + fibanacci(n-2)

list = []
for e in range(1, n+1):
    list.append(fibanacci(e))
list.sort(reverse=True)
print(list)

list2 = []
for e in range(1, n+1):
    list2.append(fibanacci(e))
    for i in range(len(list2)):
        if i%2 != 0:
         list2[i] = list2[i] * m
print(list2)

join_list = list + list2
print(join_list.insert(n, 0))
print(join_list)