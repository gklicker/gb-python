"""
Задание:
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def my_join(fname, lname, byear, cyear, email, phone):
    return "{}, {}, {}, {}, {}, {}".format(fname, lname, byear, cyear, email, phone)


print(my_join("Иван", "Иванов", 1989, 2020, "a@a.ru", "89000000000"))
