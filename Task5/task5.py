# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


def fibanacci(n):
    if n in [1,2]:
        return 1
    else:
        return fibanacci(n-1) + fibanacci(n-2)
list = []
for e in range(1, 9):
    list.append(fibanacci(e))
print(list)

list2 = []
for e in range(1, 9):
    list2.append(fibanacci(e)*-1)
    list.sort(list2)
print(list2)