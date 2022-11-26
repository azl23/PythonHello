# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# print('Введите первое число: ')
# number_one = int(input())
# print('Введите второе число: ')
# number_two = int(input())
# print('Введите третье число')
# number_three = int(input())
# print('Введите четверное число')
# number_four = int(input())
# print('Введите пятое число')
# number_five = int(input())

# max_number = number_one

# if number_two > number_one:
#     max_number = number_two
# elif number_three > number_two:
#     max_number = number_three
# elif number_four > number_three:
#     max_number = number_four
# elif number_five > number_four:
#     max_number = number_five
# else:
#     max_number = number_one

# print(max_number)

nums = [4, 6, 8, 22, 77, 2]
maximum = nums[0]
for i in nums:
    if maximum < i:
        maximum = i
print (maximum)


