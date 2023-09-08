"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
 Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
 Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
import random


def solve(s, p):
    for i in range(1001):
        for j in range(1001):
            if i + j == s and i * j == p:
                return i, j
            



if __name__ == '__main__':
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    s = x + y
    p = x * y
    print(f'I guessed 2 numbers. Their sum is {s}, and their product is {p}')
    maybe_x, maybe_y = solve(s, p)
    if maybe_x == x and maybe_y == y:
        print(f"You we found them: x={maybe_x}, y={maybe_y}")