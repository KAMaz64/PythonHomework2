# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

Sum = int(input("Подсказка №1: Сумма загаданных чисел равна  "))
Product = int(input("Подсказка №2: Произведение загаданных чисел равно  "))
for X in range(1000):
    for Y in range(1000):
        if Sum == X + Y and Product == X * Y:
            print('X =', X, 'Y =', Y)