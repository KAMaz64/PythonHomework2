
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

coins = input(f'Input several numbers equal to 0 or 1, using space key as separator (1 - heads, 0 - tails): ').split()
coins = [int(coin) for coin in coins]
heads = 0
tails = 0
for coin in coins:
    if coin:
        heads += 1
    else:
        tails += 1

print(f'You need to flip {heads if heads <= tails else tails} coins')