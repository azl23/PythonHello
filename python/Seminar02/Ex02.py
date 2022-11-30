# Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.

line_1 = str(input('Введите строку:\n'))            # вводим первую переменную
line_2 = str(input('Введите строку:\n'))            # вводим вторую переменную
n = 0                                               # вводим счетчик                                
for first in range(len(line_1) - len(line_2) + 1):  # first -элемент, который сверяется. (len(line_1) - len(line_2) + 1) - чтоб дошло до границы и не вышло
    if line_1[first:first+len(line_2)] == line_2:   # Берет из line_1
        n += 1
print(n)

# a = list(input())
# b = list(input())
# cnt = 0
# for i in range(len(a)-len(b)+1):
#     if a[i] == b[0]:
#         switch=True
# for j in range(len(b)):
#     if a[i+j] != b[j]:
#         switch=False
#         break
# if switch:
#     cnt += 1
#     print(cnt)