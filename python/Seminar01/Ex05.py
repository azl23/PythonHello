# Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(0,100))
print(numbers)
count = 0
maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
for i in numbers:
    if i < (maximum * 0.1):
        count += 1
print(maximum)
print(count)