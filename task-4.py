"""
Задание:
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = None
    name = None
    is_police = False

    def __init__(self):
        self.is_police = False

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass

    def show_speed(self):
        print("Speed {} kn/h".format(self.speed))

class TownCar(Car):
    def show_speed(self):
        #  60
        print("Speed {} kn/h{}".format(self.speed, "" if self.speed <= 60 else " превышение"))


class WorkCar(Car):
    def show_speed(self):
        #  40
        print("Speed {} kn/h{}".format(self.speed, "" if self.speed <= 40 else " превышение"))

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self):
        self.is_police = True

A = TownCar()
A.speed = 60
A.color = "red"
A.name = "Name A"
A.show_speed()

B = WorkCar()
B.speed = 60
B.color = "green"
B.name = "Name B"
B.show_speed()

C = SportCar()
C.speed = 60
C.color = "blue"
C.name = "Name C"
C.show_speed()

D = PoliceCar()
D.speed = 60
D.color = "transparent"
D.name = "Name D"
D.show_speed()