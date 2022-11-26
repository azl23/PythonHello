# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# print('Введите первое число: ')
# number_one = int(input())
# print('Введите второе число: ')
# number_two = int(input())
# if number_one * number_one == number_two or number_two * number_two == number_one:
#     print('Да ')
# else:
#     print('Нет')

number_one = int(input('Введите первое число:\n'))
number_two = int(input('Введите второе число:\n'))
if number_one * number_one == number_two or number_two * number_two == number_one:
    print('Да ')
else:
    print('Нет')

