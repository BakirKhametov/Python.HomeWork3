# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))
binary = ''
while n > 0:
    binary = str(n % 2) + binary
    n = n // 2
print(binary)