# # Практическое задание 1

class Matrix:

    def __init__(self, matr):
        self.m = matr

    def __str__(self):
        st = ''
        for i in range(len(self.m)):
            st = st + '\t'.join(map(str, self.m[i])) + '\n'
        return st


    def __add__(self, other):
        res = [[0, 0], [0, 0], [0, 0]]
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                res[i][j] = self.m[i][j] + other.m[i][j]
        return Matrix(res)

m1 = Matrix([[1, 2], [3, 4], [5, 6]])
m2 = Matrix([[6, 5], [4, 3], [2, 1]])
print(m1)
print(m2)
print(m1.__add__(m2))


# Практическое задание 2
# from abc import ABC, abstractmethod
#
# class Clothes(ABC):
#     def __init__(self, name, size, height):
#         self.n = name
#         self.s = size
#         self.h = height
#
#     @abstractmethod
#     def all_rash(self):
#         a = round((self.s / 6.5 + 0.5)  + (self.h * 2 + 0.3), 2)
#         print(f'Общий расход ткани для {self.n} - {a}')
#
#     @property
#     def size(self):
#         return self.s
#
#     @size.setter
#     def size(self, size):
#         if self.s < 36:
#             self.s = 36
#         elif self.s > 48:
#             self.s = 48
#         else:
#             self.s = size
#
#     def size_check(self):
#         return f'Размер одежды - {self.s}'
#
# class Coat(Clothes):
#     def rashod(self):
#         r = round(self.s / 6.5 + 0.5, 2)
#         print(f'Расход материала для {self.n} = {r}')
#
#     def all_rash(self):
#         a = round((self.s / 6.5 + 0.5) + (self.h * 2 + 0.3), 2)
#         print(f'Общий расход ткани для {self.n} - {a}')
#
# class Costume(Clothes):
#     def rashod(self):
#         r = self.h * 2 + 0.3
#         print(f'Расход материала для {self.n} = {r}')
#
#     def all_rash(self):
#         a = round((self.s / 6.5 + 0.5)  + (self.h * 2 + 0.3), 2)
#         print(f'Общий расход ткани для {self.n} - {a}')
#
# coat = Coat('Пальто', 40, 1.5)
# cos = Costume('Костюм', 42, 1.78)
# coat.rashod()
# cos.rashod()
# coat.all_rash()
# cos.all_rash()
# print(coat.size_check())
# print(cos.size_check())

# Практическое задание 3
# class Cell:
#     def __init__(self, compartment):
#         self.c = compartment
#
#     def __add__(self, other):
#         return Cell(self.c + other.c)
#
#     def __sub__(self, other):
#         if self.c - other.c < 0:
#             return 'Отрицательно количество ячеек!'
#         else:
#             return Cell(self.c - other.c)
#
#     def __mul__(self, other):
#         return Cell(self.c * other.c)
#
#     def __truediv__(self, other):
#         return Cell(self.c // other.c)
#
#     def __str__(self):
#         return f'Новое количество ячеек - {self.c}'
#
#     def make_order(self, obj, arg):
#         self.a = arg
#         res = self.c + obj.c         # Здесь можно любой знак подставить, я решил сложение
#         print(res)
#         while res >= arg:
#             print('*' * self.a, sep='\n')
#             res = res - self.a
#         if res % self.a > 0:
#             print('*' * (res % self.a))
#
# c1 = Cell(10)
# c2 = Cell(5)
# c1.make_order(c2, 5)
# print(c1 + c2)
# print(c1 - c2)
# print(c1 * c2)
# print(c1 / c2)

