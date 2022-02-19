#Практические задания к уроку №2
#Практическое задание №1
li_pz1 = [19, 'apple', [1,2,3,99], True, False, None, ('orange', 11)]
for el in li_pz1 :
    print (type(el))

#Практическое задание №2
my_list2 = list (input('Ввод: '))
for x in range(1, len(my_list2), 2):
    my_list2[x-1], my_list2[x] = my_list2[x], my_list2[x-1]
print(my_list2)
#Воспользовался помощью куратора, после вроде разобрался что к чему

#Практическое задание №3 Варинат 1 - через list
month = int (input('Номер месяца: '))
li_pz2 = ['зима', 'весна', 'лето', 'осень']
if month == 1 or month == 2 or month == 12:
    print (li_pz2[0])
elif month == 3 or month == 4 or month ==5:
    print (li_pz2[1])
elif month == 6 or month == 7 or month == 8:
    print (li_pz2[2])
elif month == 9 or month == 10 or month == 11:
    print (li_pz2[3])
else:
    print ('Номер месяца введен не корректно ')

#Практическое задание №3 Варинат 2 - через dict
month2 = int (input('Номер месяца: '))
di = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
if month2 == 1 or month2 == 2 or month2 == 12:
    print (di.get(1))
elif month2 == 3 or month2 == 4 or month2 ==5:
    print (di.get(2))
elif month2 == 6 or month2 == 7 or month2 == 8:
    print (di.get(3))
elif month2 == 9 or month2 == 10 or month2 == 11:
    print (di.get(4))
else:
    print ('Номер месяца введен не корректно ')

# Практическое задание №4
st = input('Ввод: ')
st1 = st.split(' ')
for y, el2 in enumerate (st1):
    if len(el2) >= 10:
        el_new = el2[0:10]
        print(y+1, el_new)
    else:
        print(y+1, el2)

# Практическое задание №5
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
i = 0
digit = int(input("Введите число: "))
for el in range(len(my_list)):
    i = i + 1
    if my_list[0] <= digit:
        my_list.insert(0, digit)
        break
    elif my_list[-1] >= digit:
        my_list.append(digit)
        break
    elif my_list[i-1] > digit and my_list[i] <= digit:
        my_list.insert(i, digit)
        break
print(f"текущий список - {my_list}")

