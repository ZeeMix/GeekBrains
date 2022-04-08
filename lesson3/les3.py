"""
Урок 3. Функции. Словари
"""


# def func(a: int, b: int) -> int:
#     """пример простейшей функции"""
#     c = a + b
#     return c
#     # print(c)


# e = 20
# m = 40
#
# value = func(e, m)
# print(value)

# callback = func
# print(type(callback), callback(10, 20))
# print(func(20, 30))
# print(id(func))
# print(id(callback))


# from random import randint as rd
# a = rd(10, 20)
# b = rd(10, 20)
# print(a, b)

#  возвращаем callback - упрощенный пример
# nums = ['1578.4', '892.4', '354.1', '871.5']
# summa = 0
# for num in nums:
#     summa += float(num)
# print(summa)
#
# #  более сложный вариант
# print(sum(map(float, nums)))


# def say_hello():
#     print(name)
#
#
# name = 'Иван'
# say_hello() # Иван


# def say_hello():
#     name = 'Петр'
#     print(name)
#
#
# name = 'Иван'
# say_hello()  # Петр
#
#
# def say_hello_wrapper():
#     name = 'Петр'
#     def say_hello():
#         print(name)
#     say_hello()
#
#
# name = 'Иван'
# say_hello_wrapper() #  Петр


# def say_hello():
#     name = 'Петр'
#     print(name)
#
#
# name = 'Иван'
# say_hello() #  Петр
# print(name) #  Иван


# def say_hello():
#     global name
#     name = 'Петр'
#     print(name)
#
#
# name = 'Иван'
# print(name)  # Иван
# say_hello()  # Петр
# print(name)  # Петр


# user_1 = ['Иванов', 'Иван', 'Иванович', 25]
# user_2 = ['Петров', 'Петр', 'Петрович', 28]
#
#
# def info(user):
#     print(f'Фамилия - {user[0]}, имя - {user[1]}, отчество - {user[2]}, возраст - {user[3]}')
#
#
# info(user_1)
# info(user_2)

# user_1 = {'фамилия': 'Иванов',
#           'имя': 'Иван',
#           'отчество': 'Иванович',
#           'возраст':  {'5 лет назад': 15, 'сейчас': 20},
#           'увлечения': ['хоккей', 'пиво', 'бег']}

# print(user_1['отчество'])
# user_1['фамилия'] = 'Петров'
# user_1['адрес'] = 'ул.Пушкина, д.Колотушкина'
# print(user_1)
# print(user_1['возраст']['5 лет назад'])

# print(user_1['цвет глаз'])
# print(user_1.get('цвет глаз'))
# print(user_1.get('цвет глаз', 'такой параметр на найден'))
#
# print(user_1.setdefault('цвет глаз', 'черные'))
# # print(user_1)


# address = {'street': 'Невский проспект', 'house': 15}
# user_8 = {'first_name': 'Роман', 'last_name': 'Григорьев'}
# user_8.update(address)
# print(user_8)


# user_9 = {'first_name': 'Роман', 'last_name': 'Григорьев', 'street': 'Ленина'}
# some_pair = user_9.popitem()
# print(some_pair)  # ('street', 'Ленина')
# print(user_9)  # {'first_name': 'Роман', 'last_name': 'Григорьев'}


# user_10 = {'first_name': 'Егор', 'last_name': 'Родионов'}
# last_name = user_10.pop('last_name')
# print(last_name)  # Родионов
# print(user_10)  # {'first_name': 'Егор'}


# user_1 = {'фамилия': 'Иванов',
#           'имя': 'Иван',
#           'отчество': 'Иванович',
#           'возраст':  {'5 лет назад': 15, 'сейчас': 20},
#           'увлечения': ['хоккей', 'пиво', 'бег']}
# # for item in user_1:
# #     print(item)
# #
# # for i in user_1.values():
# #     print(i)
# #
# # for j in user_1.keys():
# #     print(j)
#
# for i, j in user_1.items():
#     print(f'{i}: {j}')


# def my_sum(args):
#     return sum(args)
#
#
# print(my_sum([1, 5, 89])) # 95
# print(my_sum(1, 5, 89))


# def my_sum(*a):
#     return sum(a)
#
#
# # print(my_sum([1, 5, 89])) # 95
# print(my_sum(1, 5, 89))


# def square(r, pi=3.14):
#     print(pi * r ** 2)
#
#
# square(10, 3.141)


# def hello(name='незнакомец'):
#     print('hello', name)
#
#
# hello()
# hello('Иван')
#
#
# def box_show(w, h, unit='м', lang='ru'):
#     if lang == 'ru':
#         print(f'ширина {w} {unit}, высота {h} {unit}')
#     else:
#         print(f'width {w} {unit}, height {h} {unit}')
#
#
# box_show(5, 10)  # ширина 5 м, высота 10 м
# box_show(5, 10, 'см', 'en')  # ширина 5 см, высота 10 см
#
# box_show(h=10, w=5)  # ширина 5 м, высота 10 м
# box_show(5, 10, lang='en')  # width 5 м, height 10 м
#
#
# def box_show(w, h, unit='м', lang='ru', **kwargs):
#     print(f'kwargs: {kwargs}')
#     if lang == 'ru':
#         print(f'ширина {w} {unit}, высота {h} {unit}')
#     else:
#         print(f'width {w} {unit}, height {h} {unit}')
#
#
# box_show(5, 10, lang='en', color='red')

#
# def show_user(name, *args, **kwargs):
#     print(f'Пользователь {name}')
#     print(f'args: {args}')
#     print(f'kwargs: {kwargs}')
#
#
# show_user('Иван', 'Иванов', 'Иванович', age=25)
#
#
# def accepted(el):
#     return el.lower().startswith('i')
#
#
# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# products_sample = filter(accepted, products)
# print(type(products_sample))
# print(*products_sample)
#
# nums = ['0', 'Samsung Galaxy', '15.5', '18,1', 'iPhone', '748', 'HelloWord']
# int_nums = list(filter(str.isalpha, nums))
# print(int_nums)
#
#
# user_names = ['Иван', 'Петр', 'Ольга', 'Сергей']
# user_logins = ['ivan', 'petr', 'olga', 'sergey']
# user_roles = ['user', 'staff', 'admin', 'user']
# for i in range(len(user_names)):
#     print(f'{user_names[i]}, {user_logins[i]}, {user_roles[i]}')
#
#
# for name, login, role in zip(user_names, user_logins, user_roles):
#     print(f'{name}, {login}, {role}')


# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# products_sample = filter(lambda el: el.lower().startswith('i'), products)
# print(*products_sample)  # iPad iPhone iRiver
#
#
# func = lambda c: c ** 2
# print(func(10))



# # 3) дз 3 задание к прошлому уроку
# def edit_list(some_list):
#     idx = 0
#     while idx < len(some_list):
#         if some_list[idx].isdigit():
#             if len(some_list[idx]) == 1:
#                 some_list[idx] = f'0{some_list[idx]}'
#                 some_list.insert(idx, '"')
#                 idx += 2
#                 some_list.insert(idx, '"')
#             else:
#                 some_list.insert(idx, '"')
#                 idx += 2
#                 some_list.insert(idx, '"')
#         elif some_list[idx][0] == '+' or some_list[idx][0] == '-':
#             if len(some_list[idx]) == 2:
#                 some_list[idx] = f'{some_list[idx][0]}0{some_list[idx][1:]}'
#                 some_list.insert(idx, '"')
#                 idx += 2
#                 some_list.insert(idx, '"')
#             else:
#                 some_list.insert(idx, '"')
#                 idx += 2
#                 some_list.insert(idx, '"')
#         idx += 1
#
#     return some_list


