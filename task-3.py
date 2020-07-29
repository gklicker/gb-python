"""
Задание:
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

di = {"wage": 43000, "bonus": 25000}


class Worker:
    name = None
    surname = None
    position = None
    _income = di


class Position(Worker):
    def get_full_name(self):
        return "{} {}".format(self.name, self.surname)

    def get_total_income(self):
        return sum([value for name, value in self._income.items()])


IvanovIvan = Position()
IvanovIvan.name = "Ivan"
IvanovIvan.surname = "Ivanov"

print(IvanovIvan.get_full_name(), end=" ")
print(IvanovIvan.get_total_income())
