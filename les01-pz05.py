#Практическое задание №5
vir = float (input('Выручка: '))
izd = float (input('Издержки: '))
cash = float (vir- izd)
print (f'{vir}-{izd}={cash}')
if vir > izd:
    print (f'Работа в прибыль. Прибыль = {cash} ')
elif vir == izd:
    print ('Работа в ноль.')
else:
    print (f'Работа в убыток.')


