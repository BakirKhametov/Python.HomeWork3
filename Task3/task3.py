# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []
for i in range(len(list)):
    list2.append (round((list[i]%1), 3))
print(list)
print(list2)

maximum = 0
for i in range(len(list2)):
    if list2[i] > maximum:
        maximum = list2[i]
else:
    print(f'Максимальное значение дроби:{maximum}')   

min_value = None
for value in list2:
    if not min_value:
            min_value = value
    elif value < min_value:
            min_value = value
else:
    print(f'Минимальное значение дроби:{min_value}')   

print(f'Разница между максимальным и минимальным значением: {maximum-min_value}')