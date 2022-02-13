#Практическое задание №2
time = int (input('Время в секундах: '))
hours = time // 3600
min = (time - hours * 3600) // 60
sec = time % 60
print (f'{hours}:{min}:{sec}')