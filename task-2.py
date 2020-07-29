"""
Задание:
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""
class Road:

    __length = None
    __width = None
    __deep = None
    __weight = None

    def calc(self):
        return int(self.__deep * self.__weight * self.__length * self.__width)

    def __init__(self, length, width, deep=5, weight=25):
        self.__length = length
        self.__width = width
        self.__deep = deep / 1000
        self.__weight = weight

Road1 = Road(20, 5000)
print("{} Т".format(Road1.calc()))