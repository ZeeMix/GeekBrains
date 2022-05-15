"""
Урок 10. Объектно-ориентированное программирование. Продвинутый уровень
"""
# Сегодня обучаемся в режиме игры "БОМЖ" )))

# Перегрузка операторов
# from actions.operators import Bottle
#
# our_bottles = set()  # Наша коллекция пузырей в кармане
#
# # __init__
# bottle_1 = Bottle(1.5, our_bottles)
# bottle_2 = Bottle(0.5, our_bottles)
# bottle_3 = Bottle(1, our_bottles)
# print(f'У нас сейчас есть бутылки: {our_bottles}')
# print()
#
# # __del__
# bottle_2.trow_away()
# del bottle_2
# print(f'У нас сейчас есть бутылки: {our_bottles}')
# print()
#
# # __str__
# print('Ты посчитал свои запасы и увидел:')
# for bottle in our_bottles:
#     print(f'\t{bottle}')
# print()
#
# # __add__
# bottle_1 + bottle_3
# bottle_3 + bottle_1
#
# print()
#
# # __call__
# bottle_3(3)
# print()
#
# print()
#
#
# # Реструктуризацию запасов пузырей Warehouse - закупим себе сарай))
# from actions.my_extra import Warehouse
#
#
# # __setattr__
# warehouse = Warehouse()
# warehouse.note = 'текст моей записки'
# warehouse.title = 'Заначка'
# warehouse.title = 6
# warehouse.download_bottles(*our_bottles)
# bottle_4 = Bottle(0.5, warehouse.our_bottles)
# bottle_5 = Bottle(2, warehouse.our_bottles)
# print()
#
# # __getitem__
# accepted_bottle = warehouse[1]
# print('Соотвествует условию объема больше 1 или равного ему:', *accepted_bottle, sep='\n')
# print()
#
# # __eq__
# warehouse_2 = Warehouse()
# if warehouse == warehouse_2:
#     print(f'Кол-во бутылок на складах "{warehouse.title}", "{warehouse_2.title}" РАВНЫ!')
# else:
#     print(f'Кол-во бутылок на складах "{warehouse.title}", "{warehouse_2.title}" НЕ РАВНЫ!')
# print()
#
# # __lt__
# if warehouse < warehouse_2:
#     print(f'Название склада "{warehouse.title}" КОРОЧЕ названия склада "{warehouse_2.title}"')
# else:
#     print(f'Название склада "{warehouse.title}" ДЛИННЕЕ названия склада "{warehouse_2.title}"')
#
#
# # __iadd__
# bottle_6 = Bottle(5, warehouse_2.our_bottles)
# warehouse_2 += bottle_6
# print()
# print()

# Интерфейсы
from actions.my_interfaces import VacuumCleaner, VacuumCleaner2
# robot_1 = VacuumCleaner()
robot_2 = VacuumCleaner2()
# robot_1.on_off_action()
robot_2.on_off_action()
robot_2.say()
print()

# Задача на закрепление (скриншот в телеге)

# import datetime as dt
#
#
# class Date:
#     def __init__(self, month, day):
#         self.month = month
#         self.day = day
#
#     def __sub__(self, other):
#         date1 = dt.date(2020, self.month, self.day)
#         date2 = dt.date(2020, other.month, other.day)
#         total_date = str(date1 - date2).split()
#         if len(total_date) != 1:
#             return total_date[0]
#         else:
#             return 0
#
#
# jan5 = Date(1, 5)
# jan1 = Date(1, 1)
#
# print(jan5 - jan1)
# print(jan1 - jan5)
# print(jan1 - jan1)
# print(jan5 - jan5)
#
# # Задача из телеги №2
#
#
# class SparseArray:
#     def __init__(self):
#         self.data = {}
#
#     def __getitem__(self, item):
#         return self.data.get(item, 0)
#
#     def __setitem__(self, key, value):
#         self.data[key] = value
#
#
# arr = SparseArray()
# arr[1] = 10
# arr[8] = 20
# for i in range(10):
#     print('arr[{}] = {}'.format(i, arr[i]))
