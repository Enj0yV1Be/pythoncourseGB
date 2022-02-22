# Практическое задание №1 Варинат 1 - через именную функцию
"""Функция считает и выводит сумму чисел a и b """
def delenie(a, b):
    try:
        res = a / b
        print(res)
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    except ValueError:
        return 'Вводить только числа!'

a = int(input('a='))
b = int(input('b='))
delenie(a, b)

""""" Если через if, то так:
if b != 0:
  res = a / b
  print(res)
else:
    print('На ноль делить нельзя!') """

# Практическое задание №1 Варинат 2 - через лямбда функцию
delenie2 = lambda m, n: m / n
m = int(input('m='))
n = int(input('n='))
print(delenie2(m, n))

# Практическое задание №2
def pers_info(name = input('Name: '), surname = input("Surname: "), year = int(input("Year: ")), country = input("country:"), city = input("City: ")):
    print(name, surname, year, country, city)

pers_info()

# Практическое задание №3
def summ(i1, i2, i3):
    if i1 == i2 and i2 == i3:
        res_pz2 = i1 + i3
        print('Лучше вводить разные значения')
    elif i1 < i2 and i1 < i3:
        res_pz2 = i2 + i3
    elif i2 < i1 and i2 < i3:
        res_pz2 = i1 + i3
    elif i3 < i1 and i3 < i2:
        res_pz2 = i1 + i2
    print(res_pz2)
    return res_pz2

r1 = int(input('Первое число: '))
r2 = int(input('Второе число: '))
r3 = int(input('Третье число: '))
summ(r1, r2, r3)

# Практическое задание №4 Вариант 1 -  через оператор **
stepen = lambda x, y: x ** y

x = float(input('x='))
y = int(input('y='))
print(stepen(x, y))

# Практическое задание №4 Вариант 2 - через цикл for
x1 = float(input('x='))
y1 = int(input('y='))

def stepen1(x1, y1):
    for el in range(abs(y1)):
        prom_x = x1 * x1
        if abs(y1) == 2:
            return 1 / prom_x
        elif abs(y1) == 1:
            return 1 / x1
        else:
            z = prom_x * x1
        return 1 / z

print(stepen1(x1, y1))

# Практическое задание №5
res = 0
while True:
    li = input('Вводите числа через пробел: ').split()
    i = 0
    total = 0
    for el in range(len(li)):
        if li[el] == 'q':
            break
        else:
            li[i] = int(li[i])
            i = i + 1
            res = res + li[el]
    total = total + res
    print(total)

# Практическое задание №6-7
def int_func(*args):
    word = input('Введитеслова через пробел: ').title()
    print(word)

int_func()
