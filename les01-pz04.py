#Практическое задание №4
num = int (input("Введите число: "))
max = 0
while num > 0:
    if num % 10 > 9:
        print("Максимальное цифра в числе: ", max)
        break
    num = num // 10
    if num % 10 > max:
        max = num % 10
    else:
        print("Максимальное цифра в числе: ", max)
        break