# Практическое задание №1
# class Data:
#     def __init__(self, dmy):
#         self.dmy = dmy
#
#     @classmethod
#     def extract(cls, dmy):
#         my_date = []
#
#         for i in dmy.split():
#             if i != '-': my_date.append(i)
#
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month):
#
#         if 1 <= day <= 31:
#             pass
#         else:
#             return 'Неправильный день'
#         if 1 <= month <= 12:
#             pass
#         else:
#             return 'Неправильный месяц'
#
#
#     def __str__(self):
#         return f'Сегодня {Data.extract(self.dmy)}'
#
#
# today = Data('2 - 10 - 2021')
# print(today)

# Практическое задание №2
# class Pz2(Exception):
#     def __init__(self, txt):
#         self.txt = txt
# try:
#     num1 = int(input('Введите делимое: '))
#     num2 = int(input('Введите делитель: '))
#     if num2 == 0:
#         print(Pz2('Делить на ноль нельзя!'))
# except (ZeroDivisionError, Pz2('Делить на ноль нельзя!')) as err:
#     print(err)

# Практическое задание №3
# class Pz3(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# li = []
#
# while True:
#     a = input('Вводите только числа: ')
#     try:
#         a = int(a)
#         li.append(a)
#     except (TypeError, ValueError, Pz3) as err:
#         print(Pz3('Вводите только числа!'))
#     print(li)

# Практическое задание №4,5
# class Tech:
#
#     def __init__(self, name, cost, year):
#         self.c = cost
#         self.y = year
#         self.name = name
#
#     def sklad(self, num):
#         self.n = num
#         self.sk = {'name': self.name, 'cost': self.c, 'year': self.y, 'amount': self.n}
#         print(self.sk)
#
#
#
#     def info(self):
#         return f'name - {self.name}, cost - {self.c}, year - {self.y}, amount - {self.n}'
#
# class Printer(Tech):
#     def __init__(self, name, cost, year, paper_count):
#         super().__init__(name, cost, year)
#         self.pc = paper_count
#
# class Scanner(Tech):
#     def __init__(self, name, cost, year, format):
#         super().__init__(name, cost, year)
#         self.f = format
#
# class Xerox(Tech):
#     def __init__(self, name, cost, year, side):
#         super().__init__(name, cost, year)
#         self.side = side
#
#
# p = Printer('Priner', 200, 2021, 50)
# p.sklad(2)
# s = Scanner('Scanner', 150, 2022, 'PDF')
# s.sklad(5)
# x = Xerox('Xerox', 100, 2020, 'both side')
# x.sklad(3)
#
# print(p.info())
# print(s.info())
# print(x.info())
