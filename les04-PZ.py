# Практическое задание №1
from sys import argv
print(argv)
chas = int(argv[1])
stavka = float(argv[2])
prem = float(argv[3])

zp = (chas * stavka) + prem
print(zp)

# Практическое задание №2
li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [li[i] for i in range(1, len(li)) if li[i-1] < li[i]]
print(new)

# Практическое задание №3
spisok = [el for el in range(241) if el % 20 == 0 or el % 21 == 0]
print(spisok)

# Практическое задание №4
pz4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_pz4 = [el for el in pz4 if pz4.count(el) == 1]
print(new_pz4)

# Практическое задание №5
from functools import reduce

pz5 = [el for el in range(100, 1001) if el % 2 ==0]
print(pz5)

def chet(a,b):
    return a * b

print(reduce(chet, pz5))

# Практическое задание №6
from itertools import count, cycle

# Первая часть задния
for el in count(int(input('Введите начально число: '))):
    print(el)
    if el == 10:
        break

# Вторая часть
li_pz6 = ['hello', 11, 12, True, [0, 1], None, 'hello']
for el in cycle(li_pz6):
        print(el)




