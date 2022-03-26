# Практическое задание №1
from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'зеленый']

    def running(self):
        for el in TrafficLight.__color:
            if el == TrafficLight.__color[0]:
                print(el)
                sleep(7)
            elif el == TrafficLight.__color[1]:
                print(el)
                sleep(2)
            else:
                print(el)
                sleep(5)


tl1 = TrafficLight().running()

# Практическое задание №2
class Road:
    def __init__(self, length, width, weight, height):
        self._l = length
        self._w = width
        self.we = weight
        self.h = height / 100


    def res_weigth(self):
        res = self._l * self._w * self.we * self.h
        print(res)

asph = Road(5000, 20, 25,5)
asph.res_weigth()

# Практическое задание №3
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))

pos = Position('Vasya', 'Petrov', 'doctor', 20000, 5000)
pos.get_full_name()
pos.get_total_income()

# Практическое задание №4
class Car:
    def __init__(self, speed, color, name, is_polis):
        self.s = speed
        self.c = color
        self.n = name
        self.p = is_polis


    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина стоит')

    def turn(self, direction):
        self.d = direction
        print(f'машина повернула {self.d}')

    def show_speed(self):
        print(f'Скорость машины: {self.s}')

    def get_info(self):
        print(f'марка: {self.n} цвет: {self.c} скорость: {self.s}')

class TownCar(Car):
    def show_speed(self):
        if self.s > 60:
            print(f'Скорость машины: {self.s} Превышение скорости!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.s > 40:
            print(f'Скорость машины: {self.s} Превышение скорости!')

class PoliceCar(Car):
    pass

town_car = TownCar(100, 'черная', 'toyota', False)
town_car.get_info()
town_car.turn('напарво')
town_car.show_speed()
sport_car = SportCar(240, 'красная', 'ferrari', True)
sport_car.get_info()
sport_car.go()
work_car = WorkCar(0, 'белая', 'volkswagen', False)
work_car.get_info()
work_car.stop()
police = PoliceCar(90, 'синяя', 'Geely', True)
police.get_info()
police.turn('налево')

# Практическое задание №5
class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'{self.t} может быть перьевая или шариковая')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.t} сделан из графита и дерева')
class Handle(Stationery):
    def draw(self):
        print(f'{self.t} помогает выделять информацию в конспектах')

pen = Pen('Ручка').draw()
pencil = Pencil('Карандаш').draw()
handle = Handle('Маркер').draw()