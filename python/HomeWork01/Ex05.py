import math
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21


def calc_distance(xa, ya, xb, yb):
    return round(math.sqrt(((xb - xa)**2) + ((yb - ya)**2)), 3)

xa = int(input('Введите координату x точки A => '))
ya = int(input('Введите координату y точки A => '))
xb = int(input('Введите координату x точки B => '))
yb = int(input('Введите координату y точки B => '))

distance = calc_distance(xa, ya, xb, yb)
print(f'Расстояние между точками - {distance}')