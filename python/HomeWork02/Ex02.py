# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

number = input('Введите число N:\n')
if number.isdigit() and int(number)>0:
    number = int(number)
    result = [1]
    for i in range(2,number+1):
        result.append(result[i-2]*i)
    print(f'N = {number}, Набор произведений: {result}')
else:
    print("Нужно ввести число больше 0")
