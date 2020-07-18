"""
Задание:
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

# Рекурсивная ф-ция проверки строки
# True если все символы в диапазоне от 96 до 123
def filter(word):
    if not len(word):
        return True
    if 96 < ord(word[0]) < 123 and filter(word[1:]):
        return True
    else:
        return False

def int_func(input_string):
    output = []
    for word in input_string.split():
        if filter(word):
            output.append(word.title())
    return " ".join(output)

print(int_func("text Text teXt text Text 47sa3 same"))