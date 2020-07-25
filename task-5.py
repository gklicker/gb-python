"""
Задание:
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random
import functools

with open(file="task-5.txt", mode="w+") as of:
    print(" ".join(
        [str(random.randint(-1000, 1000)) for i in range(1, random.randint(5, 10))]
    ), file=of)
    of.seek(0)
    sum = 0
    for ln in of:
        sum += functools.reduce((lambda a, b: int(a) + int(b)), ln.split())
print("Cумма чисел в файле {}".format(sum))
