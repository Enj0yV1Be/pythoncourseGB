#Практическое задание №6
a = float (input('Первый день: '))
b = float (input('Желаемый результат: '))
day = 1
a = a + (a * 0.1)
print (f'a= {a}')
while a < b:
    a = a + (a * 0.1)
    day = day + 1
    print (f'День {day}: {a} км')
print (f'Желаемый результат на день: {day}')
