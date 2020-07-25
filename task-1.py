"""
Задание:
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


print("Введите текст, для выхода введите пустую строку.")

with open(file="task-1.txt", mode="a+", encoding="utf-8") as fh:
    while True:
        user_line = input("")
        if not len(user_line):
            break
        fh.write(user_line + "\n")
