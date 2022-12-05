# with open('file.txt', 'w') as data:  # в даннои случае конструкцию with open('file.txt', 'w') воспринимать как data
#     data.write('line 1\n')
#     data.write('line 2\n')
# Тут происходит автоматическое закрытие файла. Не надо делать data.close()

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')  # 'file.txt' - путь к файлу, 'a' -мод
# # data.writelines(colors) # разделителей не будет
# data.write('\nLINE2\n')
# data.write('LINE3\n')
# data.close()  # после завершения работы с файлом нужно разорвать подключение файловой переменной с файлом на диске(чтоб не было утечки)




path = 'file.txt'           # Создаем файл file.txt
data = open(path, 'r')      # открываем файл в режиме чтения
for line in data:           # при помощи цикла пробежимся по файлу
    print(line)             # считаем все строки
data.close()                # после того как закончим чтение, разорвем связь
exit() # чтоб не читался дальнейший код