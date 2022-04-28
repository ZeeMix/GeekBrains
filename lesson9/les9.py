"""
Урок 9. Объектно-ориентированное программирование. Введение
"""
# from datetime import datetime
#
#
# class Woman:
#     name: str = 'Карина'
#     birthday: datetime = datetime(year=2000, month=5, day=10)
#
#     # методы класса
#     def introduce_yourself(self):
#         print(f"I'm {self.__class__.__name__}")
#
#     def get_info(self):
#         print(f'Давай знакомиться: я - {self.name} и я родилась {self.birthday.strftime("%d %B %Y")}')
#
#     def say(self, message: str):
#         print(f'{self.name} сказала нам: "{message}"')
#
#
# girl = Woman()
# print(girl)
# print(type(girl))
# girl.introduce_yourself()
# girl.get_info()
# girl.say('Ты крутой!')
# print('\n')
# girl_2 = Woman()
# girl_2.name = 'Евгения'
# print(girl.name, girl_2.name, Woman.name)
# print('\n')
#
#
# class Warehouse:
#     """Документирование класса в целом"""
#     count: int = 0
#
#     def new_build(self, number: float, region: str):
#         """Объявляет о постройке нового склада"""
#         self.number = number
#         self.region = region
#         Warehouse.count += 1  # инкрементируем общее количество складов
#
#
# warehouse_1 = Warehouse()
# warehouse_1.new_build(555.5, 'Москва')
# print(warehouse_1.number, warehouse_1.region, f"Всего складов: {warehouse_1.count}")
# warehouse_2 = Warehouse()
# warehouse_2.new_build(150, 'Волгоград')
# print(warehouse_2.number, warehouse_2.region, f"Всего складов: {warehouse_2.count}")
# print("\n")
#
#
# # Конструктор __init__
# class Rabbit:
#     auto_count: int = 0
#
#     def __init__(self):
#         Rabbit.auto_count += 1
#
#
# rabbits = [Rabbit() for _ in range(10)]
# first_rabbit = rabbits[0]
# print(f'Наплодили кроликов - {first_rabbit.auto_count} шт.')
# print(f'Наплодили кроликов - {Rabbit.auto_count} шт.')
# print('\n')
#
#
# # Локальные и глобальные переменные
# class Cat:
#     breed_2 = 'Дурная'
#
#     def her_breed(self):
#         breed = 'Породистая'
#         return breed
#
#
# kitty = Cat()
# # print(kitty.breed)
# print(kitty.breed_2)
# print(kitty.her_breed())
# print('\n')
#
#
# """
# Модификаторы доступа
#
# Public(публичный)
# Protected(защищенный)
# Private(приватный)
# """
#
#
# class Dog:
#     def __init__(self):
#         self.voice = 'гав-гав'
#         self._size = '100 попугаев'
#         self.__place = 'будка во дворе'
#
#
# dog = Dog()
# print(dog.voice)
# print(dog._size)
# # print(dog.__place)
#
#
# # Инкапсуляция
# class Ant:
#     __species: str = 'коричневый'
#
#     def __get_species(self):
#         print(f'защищенный метод')
#
#
# ant = Ant()
# ant._Ant__get_species()
# print(ant._Ant__species)
# print('\n')
#
#
# # Наследование
# import time
#
#
# class People:
#     """Так зарождалось всё человечество"""
#     def __init__(self, name: str, birthday: datetime):
#         self.name = name
#         self.birthday = birthday
#
#     def introduce_yourself(self):
#         return f"I'm {self.__class__.__name__}", self.__get_info()
#
#     def __get_info(self):
#         return dict(name=self.name, birthday=self.birthday.strftime('%d %B %Y'))
#
#
# class Man(People):
#     sex: str = 'm'
#
#     def working(self, sleeping: int = 5):
#         """Мужик должен уметь работать"""
#         while sleeping:
#             print(f'Осталось спать секунд: {sleeping}')
#             time.sleep(1)
#             sleeping -= 1
#         print('Поработали, теперь можно и домой!')
#
#
# worker = Man('Иван', datetime(year=1997, month=1, day=19))
# introduce_message, worker_info = worker.introduce_yourself()
# print(f' {3 * "-//-"} '.join(map(str, [introduce_message, worker_info, type(introduce_message), type(worker_info)])))
#
#
# class Woman2(People):
#     sex: str = 'w'
#
#     def __init__(self, name: str, birthday: datetime, secret: str):
#         super().__init__(name, birthday)
#         self.secret = secret
#
#
# girl_3 = Woman2('Юлия', datetime(year=2001, month=2, day=1), 'я Карина')
# introduce_message, girl_info = girl_3.introduce_yourself()
# print(f' {3 * "-//-"} '.join(map(str, [introduce_message, girl_info, type(introduce_message), type(girl_info)])))
# # girl_3.working()
# print('\n')
#
#
# # Множественное наследование
# # class Father:
# #     def send_money(self):
# #         print('Деньги перечислены')
# #
# #     def my_dream(self):
# #         print('Я стану космонавтом')
#
#
# class Mother:
#     def be_happy(self):
#         print('Не в деньгах счастье')
#
#     def my_dream(self):
#         print('Где спрятаться от этого всего')
#
#
# # class Child(Mother, Father):
# #     pass
#
#
# # Полиморфизм / перегрузка методов
# class Father:
#
#     def send_money(self, empty: bool = False):
#         if not empty:
#             print('Деньги перечислены')
#         else:
#             print('Я иду заработать')
#
#     def my_dream(self):
#         print('Я стану космонавтом')
#
#
# class Child(Mother, Father):
#     def my_dream(self):
#         super().my_dream()
#         print('Я закончу школу и жизнь изменится ))')
#
#
# baby = Child()
# baby.send_money()
# baby.send_money(True)
# baby.be_happy()
# baby.my_dream()
# print('\n')
#
#
# class BigBell:
#     count = 0
#
#     def sound(self):
#         if self.count % 2 == 0:
#             print('ding')
#         else:
#             print('dong')
#         self.count += 1
#
#
# bell = BigBell()
# bell.sound()
# bell.sound()
# bell.sound()
#
#
# print('\n')


# class MinMaxWordFinder:
#
#     def __init__(self):
#         self.text = []
#
#     def add_sentence(self, sentence):
#         self.text.extend(sentence.split())
#
#     def longest_words(self):
#         self.max_len = 0
#         self.max_word = []
#         for word in self.text:
#             if len(word) > self.max_len:
#                 self.max_len = len(word)
#         for word in self.text:
#             if len(word) == self.max_len:
#                 self.max_word.append(word)
#         self.max_word = list(set(self.max_word))
#         return sorted(self.max_word)
#
#     def shortest_words(self):
#         self.min_len = 100000
#         self.min_word = []
#         for word in self.text:
#             if len(word) < self.min_len:
#                 self.min_len = len(word)
#         for word in self.text:
#             if len(word) == self.min_len:
#                 self.min_word.append(word)
#         return sorted(self.min_word)
#
#
# finder = MinMaxWordFinder()
# finder.add_sentence('hello')
# finder.add_sentence('  abc     def    ')
# finder.add_sentence('world')
# finder.add_sentence('            abc          ')
# finder.add_sentence('asdf')
# finder.add_sentence('qwert')
# print(' '.join(finder.shortest_words()))
# print(' '.join(finder.longest_words()))