# Задача 1. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n = int(input("enter count watermelon:"))

max = 0
min = 0
for i in range(n):
    temp = int(input(f"{i + 1} = "))
    if i == 0:
        max = temp
        min = temp
        continue
    if temp > max:
        max = temp
    elif temp < min:
        min = temp

print(f"max = {max}; min = {min}")
