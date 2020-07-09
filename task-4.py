"""
Задание:
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input("Введите число "))

max_number = 0

while number // 10:
    next_number = number % 10
    number = number // 10

    if max_number < next_number:
        max_number = next_number
else:
    if max_number < number:
        max_number = number

print("Максимальное число {}".format(max_number))