# https://www.python.org/
# https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows

# print('Hello World!')
# print(10)

# print()
#
# a = 10
# b = 5
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)  # Остаток от деления
# print(a ** b)
#
# print(int(10.8))  # Преобразование типов данных

# name = 'Alexandr'
# surname = 'Salnikov'
# age = 20
# print('Hello', name, surname, age)
# print('Hello' + name + surname + str(age))
# print(f'Hello {name} {surname} {age}')


# name = input('Enter your name: ')
# print(f'Hello {name}')

# print(10 < 20)
# print(3 > 8)
# print(5 == 10)
# print(5 != 10)
# print(45 <= 45)
# print(30 >= 31)
# print(10 > 5 and 'a' == 'a')
# print(True or False)
# print(not 10 == 10)

# print(type(10))
# print(type(20.9))
# print(type('Yes'))
# print(type(True))
# print(type([3, 'No', False]))
# print(type(('a', 'b', 'c')))
# print(type({'age': 20, 'name': 'Alexandr'}))

# number = int(input())
# if number < 0:
#     print('Число отрицательное')
# elif number == 0:
#     print('Нулевое')
# else:
#     print('Число положительное')

# some_list = ['Alexandr', 'Макс', 'Федя']
# print(some_list)
# print(*some_list)
# print(some_list[0])
# print(some_list[-1])
# some_list[0] = 'Сергей'
# print(some_list)
# some_list.append('Илья')
# print(some_list)


# i = 0
# while i <= 10:
#     print(i)
#     i += 1


# numbers_list = [1, 9, 0, -1, 4, 8, 0]
# i = 0
# while i < len(numbers_list):
#     numbers_list[i] *= 10
#     i += 1
# print(numbers_list)


# for number in numbers_list:
#     print(number * 10)

# for i in range(20, 10, -2):
#     print(i)


# for idx, number in enumerate(numbers_list):
#     print(f'Под индексом {idx} стоит элемент {number}')


# Задача. Написать программу, определяющую, что число трёхзначное и средняя цифра равна 5.
number = int(input('Введи число: '))
if 99 < number < 1000 and number // 10 % 10 == 5:
    print('Yes')
else:
    print('No')
