"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
import random


def flip_coins_counter(n):
    heads = tails = 0
    sides = [0, 1]
    coins = []
    for i in range(n):
        random.shuffle(sides)
        coins.append(int(sides[0]))
        if int(coins[i]) == 0:
            heads += 1
        if int(coins[i]) == 0:
            tails += 1
    print("All coins: ", coins)
    if heads >= tails:
        answer = heads
    else:
        answer = tails
    print(f"You need to flip {answer} coins")


if __name__ == '__main__':
    print("Enter a number of the coins\n")
    n = int(input())
    flip_coins_counter(n)
