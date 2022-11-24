# типы данных и переменная
# int. float, boolean, str, list, None

# value = None
# print(type(value))
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello world'

a = 123
b = 1.23

# print(s) # Вывод строки
# print(a, '-' , b, '-' , s)               #способы выводов
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True  # переменная(f) присвоить True
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

#print('Введите a');
#a = float(input())    #int(input()) - от input
#print('Введите b');
#b = float(input())    #float(input())  - вещественное (float это, например, 6.0)
#print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.formate(a, b))
# print(f'{a} {b}')




# Арифметические операции
# +, -,*, /, %, //,**
# **, ⊕, ⊖,*, /, //, %, +, -
# () Сокращенные операции
# a = 3
# a += 5 # a = a + 5
# print(a)




# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
#  is, is not, in, not in
# gen

#f = [1, 2, 3, 4]
#print(f)
#print(not 2 in f)

#is_odd = f[0] % 2
#print(is_odd)



# Управляющие конструкции
# if, if-else

#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
#    print(a)
#else:
#    print(b)

#username = input('Введите имя: ')
#if username == 'Маша':
#    print('Ура, это же МАША!')
#elif username == 'Марина':       # elif - в противном случае
#    print('Я так ждал Вас, Марина!')
#elif username == 'Ильнар':
#    print('Ильнар - топ)')
#else:
#    print('Привет, ', username)



# Оператор цикла whil

#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10   #компановка перевернутого числа и делим на 10
#    print(original)
#else:
#    print('Пожалуй')
#    print('хватит)')
#print(inverted)



# Управляющие конструкции:
# for

#list = [1,2,3,4,5]
#for i in list:         #cписок цифр в переменной, которые будут указываться
#    print(i**2)        #квадрат

#for i in 'qwerty':         
#    print(i)     



# ecsr

#print(len(text))                    #39
#print('еще' in text)                #True
#print(text.isdigit())               #False
#print(text.islower())               #True
#print(text.replace('ещё', 'ЕЩЁ'))

#for c in text:
#    print(c)

#text = 'съешь еще этих мягких французских булок'
#print(text[0]) # c
#print(text[1]) # ъ
#print(text[len(text)-1]) # к
#print(text[-5]) # б
#print(text[:]) # print(text)
#print(text[:2]) # съ
#print(text[len(text)-2:]) # ок
#print(text[2:9]) # ешь ещё
#print(text[6:-18]) # ещё этих мягких
#print(text[0:len(text):6]) # сеикакл
#print(text[::6]) # сеикакл
#text = text[2:9] + text[-5] + text[:2] # ...



# Список – пронумерованная, изменяемая коллекция объектов произвольных типов 
# Списки: введение
## list = list

#numbers = [1, 2, 3, 4, 5]
#print(numbers) # [1, 2, 3, 4, 5]
#numbers = list(range(1, 6))
#print(numbers) # [1, 2, 3, 4, 5]
#numbers[0] = 10
#print(numbers) # [10, 2, 3, 4, 5]
#for i in numbers:
# i *= 2 #в текущую переменную кладем новое значение. не в сам список!
# print(i) # [20, 4, 6, 8, 10]
#print(numbers) # [10, 2, 3, 4, 5]

#colors = ['red', 'green', 'blue']
#for e in colors:
# print(e) # red green blue
#for e in colors:
# print(e*2) # redred greengreen blueblue
#colors.append('gray') # добавить в конец
#print(colors == ['red', 'green', 'blue', 'gray']) # True
#colors.remove('red') #del colors[0] # удалить элемент

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg =1
print(f(arg))
print(type(f(arg)))





