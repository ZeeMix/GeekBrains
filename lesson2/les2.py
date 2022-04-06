# a = 25
# print(type(a))

# winter_months = ['декабрь', 'январь', 'февраль']
# print(type(winter_months) == list)
# print(isinstance(winter_months, list))
# print(dir(winter_months))
# winter_months.append(['март', 'апрель'])
# # winter_months.append('апрель')
# winter_months.extend(['май', 'июнь'])
# print(winter_months)

# last_month = winter_months.pop()  удаление по индексу
# print(last_month)
# print(winter_months)

# list_numbers = [1, 4, 7, 9, 0, -2, 8, 9, 10]
# for i in range(len(list_numbers), 0, -1):
#     if i % 2 == 0:
#         list_numbers.pop(i)
# print(list_numbers)
#
# list_numbers = [1, 4, 7, 9, 0, -2, 8, 9, 0, 10]
# for idx, num in enumerate(list_numbers):
#     if idx % 2 == 0:
#         list_numbers.pop(idx)
# print(list_numbers)

# list_numbers.remove(0)  # удаление по значению
# list_numbers.remove(3)

# for i in list_numbers:
#     if list_numbers.index(i) % 2 == 0:
#         list_numbers.remove(i)

# for i in list_numbers:
#     if i == 0:
#         list_numbers.remove(i)
# print(list_numbers)

# print(list_numbers.index(7))
# print(list_numbers.count(0))

# winter_months = ['декабрь', 'январь', 'февраль']
# # winter_months.insert(0, 'январь')
# # print(winter_months)
# print(id(winter_months))
# # winter_months.reverse()
# # print(winter_months)
# # print(id(winter_months))
#
# winter_months_2 = list(reversed(winter_months))
# print(winter_months_2, id(winter_months_2))

# Создайте список из случайных чисел, найдите номер его последнего локального максимума
# import random
# list_of_numbers = []
# for _ in range(10):
#     number = random.randint(0, 10)
#     list_of_numbers.append(number)
# print(list_of_numbers)
# loc_max = []
# for idx in range(8, 0, -1):
#     if list_of_numbers[idx - 1] < list_of_numbers[idx] > list_of_numbers[idx + 1]:
#         print(list_of_numbers[idx])
#         break


# winter_months = ['декабрь', 'январь', 'февраль']
# print(id(winter_months))  # 195803208
# winter_months.sort()
# print(id(winter_months))  # 195803208
# print(winter_months)  # ['декабрь', 'февраль', 'январь']

# winter_months = ['декабрь', 'январь', 'февраль']
# print(id(winter_months))  # 195803208
# winter_months_2 = sorted(winter_months, reverse=True)
# print(id(winter_months_2), winter_months_2)

# a = 15
# print(id(a))
# a = str(a)
# print(id(a))

# word = 'привет, мир, у, меня, сегодня, хорошее, настроение'
# # print(dir(word))
# # list_word = list(word)
# # print(list_word)
# list_word = word.split(', ')
# print(list_word)
# print(', '.join(list_word))

# word = 'привет, меня зовут Александр'
# # print(word.upper())
# # print(word.islower())
# # print(word.title())
# # print(word.capitalize())
#
# print(id(word))
# word2 = word.upper()
# print(id(word2))

# op = "mdnkcsnd skdmclksdm"
# print(id(op))
# op.upper()
# print(id(op))
# print(id(op.upper()))

op = list("mdnkcsnd skdmclksdm")
print(id(op))
print(id(op.reverse()))