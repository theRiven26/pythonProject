# Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
n = int(input("enter count coin:"))
count1 = 0
count0 = 0
for i in range(n):
    temp = 3
    while temp > 1:
        temp = int(input(f"enter 0 or 1. {i + 1}/{n} "))
    if temp == 0:
        count0 += 1
    else:
        count1 += 1

if count0 > count1:
    print(count1)
else:
    print(count0)
