#coding=utf-8


coins = input(f'Input several numbers equal to 0 or 1, using space key as separator (1 - reverse, 0 - averse): ').split()
coins = [int(coin) for coin in coins]
averse = 0
reverse = 0
for coin in coins:
    if coin:
        averse += 1
    else:
        reverse += 1

print(f'You need to turn {averse if averse <= reverse else reverse} coins')