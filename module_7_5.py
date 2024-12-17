import os, time

from os.path import join, getmtime, getsize, dirname

for root, dirs, files in os.walk(r'C:\Users\Ilnar\PycharmProjects\Module 7'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formated_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(os.path.abspath(filepath))
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formated_time}, '
              f'Родительская директория: {parent_dir}')