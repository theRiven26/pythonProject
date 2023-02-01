# Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример 10: 0, 1, 2, 3
import math

n = int(input("enter N: "))
p = 2
for i in range(n):
    if math.pow(p, i) <= n:
        print(i)
    else:
        break
