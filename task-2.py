"""
Задание:
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

line_counter = 0
with open(file="sample.txt", mode="r") as fh:
    for line in fh:
        line_counter += 1
        word_counter = len(line.split())
        print("В строке {} всего {} слов(а)".format(line_counter, word_counter))
print("Всего строк: {}".format(line_counter))
