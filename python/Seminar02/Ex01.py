#  Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

list_random = []
number = int(input('Введите число:\n'))

for i in range(0,number):
    list_random.append((-3)**i)
print(list_random)