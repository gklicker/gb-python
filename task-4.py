"""
Задание:
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open(file="numbers_another.txt", mode="a", encoding="utf-8") as fo0:
    with open(file="numbers.txt", mode="r", encoding="utf-8") as fo1:
        for line in fo1:
            my_list = line.split()
            print("{} {} {}".format(dic[my_list[0]], my_list[1], my_list[2]), file=fo0)