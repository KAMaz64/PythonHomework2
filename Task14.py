# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

max_number = int(input('input N: '))
number = 2
degree = 0
flag = True

while flag:
    result = pow(number, degree)
    degree += 1
    if result <= max_number:
        print(result, end=',')
    else:
        flag = False