"""
Урок 7. Работа с файловой системой. Исключения в Python
"""
import os

# определяем путь до базовой директории, относительно которой будем работать
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

# получаем список файлов и папок в директориях
# print(os.listdir(BASE_DIR))
# parent_dir = os.path.dirname(BASE_DIR)
# print(os.listdir(parent_dir))
# print([filename for filename in os.listdir(BASE_DIR) if filename.endswith('.py')])

# generate_some_data.py
# профилирование скорости поиска файлов при проверке их размера
from time import perf_counter

folder = os.path.join(BASE_DIR, 'some_data')
# if os.path.exists(folder):
#     size_threshold = 15 * 2 ** 10
#
#     start = perf_counter()
#     small_files = [item for item in os.listdir(folder) if os.stat(os.path.join(folder, item)).st_size < size_threshold]
#     print(len(small_files), perf_counter() - start)
# else:
#     print(f'Директория {folder} отсутствует')


# переименование
new_dir_name = os.path.join(BASE_DIR, 'some_data_2')

if os.path.exists(folder) and not os.path.exists(new_dir_name):
    os.rename(folder, new_dir_name)

# revert
# revert_dir_name = os.path.join(BASE_DIR, 'some_data')
# if os.path.exists(new_dir_name) and not os.path.exists(revert_dir_name):
#     os.rename(new_dir_name, revert_dir_name)

# Модуль shutil
import shutil
import random


# Удаление директорий - благодаря возможностям модуля os
# if os.path.exists(new_dir_name):
#     os.rmdir(new_dir_name)

# shutil.copyfileobj()
path_hello_file = os.path.join(BASE_DIR, 'hello.txt')
path_summary_file = os.path.join(BASE_DIR, 'summary.txt')
# for _ in range(3):
#     with open(path_hello_file, encoding='utf-8') as src:
#         with open(path_summary_file, 'a', encoding='utf-8') as dst:
#             head_size = random.randint(0, 21)
#             print(head_size, src.read(head_size))
#             shutil.copyfileobj(src, dst)

# Ещё функции копирования


def show_stat(f_path):
    """Функция вывода статистических данных по файлу, на который указывает путь f_path"""
    stat = os.stat(f_path)
    print(f'{f_path}: perm - {oct(stat.st_mode)}, modify {stat.st_mtime:.0f}, access {stat.st_atime:.0f}')


new_dir_trash = os.path.join(BASE_DIR, 'trash')
if not os.path.exists(new_dir_trash):
    os.mkdir(new_dir_trash)

path_summary_file_2 = os.path.join(new_dir_trash, 'summary_clone.txt')
path_summary_file_3 = os.path.join(new_dir_trash, 'summary_clone_2.txt')

show_stat(path_summary_file)
show_stat(shutil.copyfile(path_summary_file, path_summary_file_2))  # не копирует настройки доступа
show_stat(shutil.copy(path_summary_file, new_dir_trash))  # не копирует метаданные
show_stat(shutil.copy2(path_summary_file, path_summary_file_3))  # копирует всё


# TODO пояснить по последнему примеру почему access из метаданных не скопировался


# рекурсивный обход папок
for root, dirs, files in os.walk(BASE_DIR):
    print(root, len(dirs), len(files))


# Обработка исключительных ситуаций в Python
# exception_hierarchy.txt


# current_file_path = __file__
# try:
#     with open(current_file_path, 'r', encoding='utf-8') as fr:
#         content = fr.read()
# except Exception as e:
#     print(f'{e.__class__.__name__} Поймали ошибку: {e}')
# else:
#     print(content)
#     print('Красавчики, ни одной ошибки не словили!!!')


# finally

# def do_calc(f_path):
#     """Функция логирования операций деления в файл"""
#     f = open(f_path, 'a', encoding='utf-8')
#     try:
#         x = float(input('enter x val: '))
#         y = float(input('enter y val: '))
#     except ValueError as err:
#         print(f'wrong val: {err}')
#     else:
#         result = x / y
#         f.write(f'{x} / {y} = {result}\n')
#     finally:
#         print(f'closing file - {f_path}')
#         f.close()
#
#
# path_calc_file = os.path.join(BASE_DIR, 'calc_log.txt')
# try:
#     do_calc(path_calc_file)
# except ZeroDivisionError:
#     print('fault: Zero division')
# except Exception as e:
#     print(f'global error {e}')


# Ключевое слово raise
# Наши вспомогательные модули в utils

"""
Причины использования raise:
1. хотим, чтобы ошибку продолжил обрабатывать ещё один обработчик
2. поднять «своё»  (кастомное) исключение
3. абстрагирование поведения кода от деталей
4. искусственно прервать выполнение кода, когда нет ошибки выполнения, 
    но что-то идёт не так или, наоборот
"""


# 1) хотим, чтобы ошибку продолжил обрабатывать ещё один обработчик
# from utils.arithmetic import division
#
# try:
#     print(division(3, 0))
# except ArithmeticError as err:
#     print(f'ArithmeticError: {err}')
# except Exception as err:
#     print(f'Exception {err}')

# 2) поднять «своё» (кастомное) исключение
# from utils.arithmetic import division_with_my_exc
# from utils.my_exceptions import FuncAttributeFailError
#
# try:
#     print(division_with_my_exc(6, 0))
# except FuncAttributeFailError as err:
#     print(f'FuncAttributeFailError: {err}')
# except Exception as err:
#     print(f'Exception {err}')


# 3) абстрагирование поведения кода от деталей
from utils.copir import files_in_dir, search_file_in_dir

try:
    # path_search_dir = os.path.join(BASE_DIR, 'utils')
    # print(files_in_dir(path_search_dir))
    # path_fake_dir = os.path.join(BASE_DIR, 'fake_dir')
    # print(files_in_dir(path_fake_dir))
    # path_file_in_dir = os.path.join(BASE_DIR, 'hello.txt')
    # print(search_file_in_dir(path_file_in_dir))
    path_file_in_dir = os.path.join(BASE_DIR, 'gb.txt')
    print(search_file_in_dir(path_file_in_dir))
except OSError as err:
    print(f"OsError: {err}")
