list1 = [1,2,3,4,5]
list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)


list1[0] = 123 # значение будет меняться в двух списках
list2[1] = 333 # значение будет меняться в двух списках

for e in list1:
    print(e)

print()

for e in list2:
    print(e)