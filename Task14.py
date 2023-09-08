"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
import math

def find_power(n):
    res_arr = []
    if n < 0:
        print("N is lower than 0!")
        return
    if n == 0:
        print(1)
    power = 1
    num = 1
    while num <= n:
        num = 1
        for i in range(power):
            num *= 2
        if num <= n:
            res_arr.append(num)
        power += 1
    print(res_arr)


if __name__ == '__main__':
    n = int(input("Input N:\n"))
    find_power(n)