# Практическое задание №1 Вариант - 1
with open('pz1.txt', 'x', encoding='utf-8') as pz1:
    text = input('Вводите слова через пробел: ').split()
    for el in text:
        print(el, file=pz1)
#Если просто вводить все нужные слова по порядку через пробел за один раз не предусматривая повторный ввод и выход

# Практическое задание №1 Вариант - 2
a = True
li_pz1 = []
while a == True:
    word = input("Введите слово: ")
    li_pz1.append(word)
    with open('pz1.txt', 'w', encoding='utf-8') as pz1:
        for el in li_pz1:
            print(el, file=pz1)
    if word == '' or word == ' ':
        a = False


# Практическое задание №2
with open('pz2.txt', 'r', encoding='utf-8') as file:
    n_str = file.readlines()
    print(f'Cтрок в файле - {len(n_str)}')
    file.seek(0)
    i = 1
    for el in file:
       words = int(len(el.split()))
       print(f'Слов в {i}-й строке - {words}')
       i += 1

# Практическое задание №3
from functools import reduce
def sum(a,b):
    return a+b

all_sal = 0
li_pz3 = []
with open('pz3.txt ', 'r', encoding='utf-8') as pz3:
    info = list(pz3.read().split())
    print(info)
    for i in range(1, len(info), 2):
        sal = float(info[i])
        li_pz3.append(sal)
        if sal <= 20000.0:
            print(f'{info[i-1]} имеет зарплату меньше 20000, а именно -  {sal}')
    all_sal = reduce(sum, li_pz3)
    average_sal = all_sal / len(li_pz3)
    print('Средняя зарплата -', round(average_sal, 2))


# Практическое задание №4
rus = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
i = 0
f = open('pz4_new.txt', 'w', encoding='utf-8')

with open('pz4.txt', 'r+', encoding='utf-8') as pz4:
    for el in pz4:
        info = el.split(' - ')
        print(info)
        for key in rus:
            if key == info[0]:
                info.pop(0)
                info.insert(0, rus[key])
                print(info)
        print(f'{info[0]} - {info[1]}', end='', file=f)

f.close()

# Практическое задание №5
res = 0

with open('pz5.txt', 'x', encoding='utf-8') as pz5:
    try:
        num = input('Вводите числа через пробел: ')
        pz5.write(num)
        num = num.split()
        num = list(map(int, num))
        for el in num:
            res = res + el
        print('\n' + str(res), file=pz5, )
    except ValueError:
        print("Вводите только числа!")

# Практическое задание №6


# Практическое задание №7
li = []
prof_comp = []
all_prof = 0
di_prof = {}
di_aver = {}
li_json = []

with open('pz7.txt', 'r', encoding='utf-8') as pz7:
    for el in pz7:
        info = el.split()
        print(info)
        prib = int(info[2]) - int(info[3])
        if prib < 0:
            print(f'{info[0]} работа в убыток {prib}')
            di_prof[info[0]] = prib
        else:
            print(f'{info[0]} Прибыль = {prib}')
            prof_comp.append(prib)
            print(prof_comp)
        all_prof = reduce(sum, prof_comp)
        aver_prof = all_prof / len(prof_comp)
        di_prof[info[0]] = prib
        di_aver['Средняя прибыль'] = round(aver_prof, 2)
    print(f'Средняя прибыль - {round(aver_prof, 2)}')
    print(di_prof)
    print(di_aver)
    li_json.append(di_prof)
    li_json.append(di_aver)
    print(li_json)

with open('pz7_new.json', 'x', encoding='utf-8') as pz7_new:
    print(li_json, file=pz7_new)

