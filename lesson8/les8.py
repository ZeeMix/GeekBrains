"""
Урок 8. Регулярные выражения и декораторы в Python
"""


import re


# RE_NAME = re.compile(r'^[А-ЯЁ][а-яё]+$')
# name = 'Иван'
# name1 = 'анастасия Олеговна'
# print(RE_NAME.match(name))

#match
# RE_DATE = re.compile(r'^(\d{2}\.){2}\d{4}$')
#
# for date in ['23.01.2021', '23,01,2021', '23~01~2021', '23-01-2021', r'23\01\2021']:
#     try:
#         assert RE_DATE.match(date), f'wrong date {date}'
#     except AssertionError as err:
#         print(err)
#
#
# txt = 'Погода 23.01.2021 была отличная! Зато за день до этого (22/01/2021) - очень холодно. ' \
#       'Надеемся, что 24-01-2021 будет без ветра.'
#
# #findall
# RE_DATE_2 = re.compile(r'(?:\d{2}[./-]){2}\d{4}')
# print(RE_DATE_2.findall(txt))
#
#
# own_text = """
#     ВНИМАНИЕ! 25.01.2022 состоится вебинарное занятие по теме "Регулярные выражения и декораторы в Python"
#     Всем рекомендуется сдать практические задания по прошлому занятию до 24-01-2022, а по проводимому
#     занятию до 28/01/2022. Также не забывайте, что писать даты в заданиях нужно согласно
#     установленного формата 11.01.1900
# """
#
#
# print()
# print(RE_DATE_2.findall(own_text))
# print(RE_DATE_2.search(own_text))
# print(RE_DATE_2.match(own_text))
# print(*RE_DATE_2.finditer(own_text))


# RE_COST = re.compile(r'\d*\s*\d+[.,]\d+')
# row_csv = "Стоимость данного товара составляет 10 001.50 рублей, а со скидкой Вы получите его за 999,99 рублей."
# print(RE_COST.split(row_csv))
# RE_COST_2 = re.compile(r'(\d+\s*\d+[.,]\d+)\s+(\b\w+\b)')
# print(RE_COST_2.findall(row_csv))


# Декораторы
# def hello_world():
#     print('Hello world!')
#
#
# hello = hello_world()
# hello()


# def wrapper_function():
#     def hello_world():
#         print('hello world')
#     hello_world()
#
#
# wrapper_function()


# def higher_order(func):
#     print(f'Получена функция {func} в качестве аргумента')
#     func()
#     # return func
#
#
# def func1():
#     print(5 + 5)
#
#
# higher_order(func1)


# def decorator_function(func):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обернутую функцию')
#         func()
#         print('Выходим из обертки')
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world!')
#
#
# hello_world()


# def benchmark(func):
#     import time
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print(f'Время выполнения функции {end - start}')
#         return return_value
#     return wrapper
#
#
# @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text
#
#
# webpage = fetch_webpage('http://ya.ru')
# print(webpage)

import random
import json
import pickle
import os
from time import perf_counter


BASE_DIR = os.path.dirname(__file__)


def decorator_func(func):
    print('Я - декоратор')

    def wrapper(*args, **kwargs):
        print('Я - обёртка')

        start = perf_counter()
        result = func(*args, **kwargs)
        print(f'Время сохранения данных: {perf_counter() - start}')

        return result

    return wrapper


# несколько декораторов и декоратор с аргументами
def print_docs(verbosity=0):
    print('АТРИБУТНАЯ ОБЁРТКА')
    def _logger(func):
        print('ДЕКОРАТОР')
        def wrapper(*args, **kwargs):
            print('ФУНКЦИОНАЛЬНАЯ ОБЁРТКА')
            msg = ''
            result = func(*args, **kwargs)
            if verbosity == 0:
                msg = f'\tcall {func.__name__} -> {result}'
            if verbosity > 0:
                msg = f'\tcall {func.__name__}\n{func.__doc__}\nРезультат: {result}'
            return msg

        return wrapper

    return _logger


@decorator_func
@print_docs(verbosity=10)
def file_saver(future_name_file: str, numbers: list, databytes=False):
    """Функция сохранения переданного списка в файл
    :param future_name_file: название файла, который будет сохранён в директории trash
    :param numbers: список элементов
    :param databytes: флаг сохранения данных в байтах или строково
    :return: str
    """
    dir_path = os.path.join(BASE_DIR, 'trash')
    file_path = os.path.join(BASE_DIR, f'trash/{future_name_file}')
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    manager = (json, pickle)[databytes]
    mode = 'wb' if databytes else 'w'
    with open(file_path, mode) as fw:
        manager.dump(numbers, fw)
    return 'Я закончил'


nums = [random.random() * 10 ** 3 for _ in range(10 ** 6)]

print(file_saver('json_saver.json', nums))
print(file_saver('pickle_saver.pickle', nums, databytes=True))