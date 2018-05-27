import os
import shutil
from hw_default_libs import clear

LINE_SEPARATOR = '---------------------------------------------------------'


def show_current_path():
    """
    Выводит на экран путь к текущей рабочей директории
    """

    path = os.getcwd()
    print('Путь к текущей папке: {}\n'.format(path))


def show_subdirectory_list():
    """
    Выводит на экран список поддиректорий рабочей папки
    """

    print('В текущей папке присутствуют следующие папки:')
    print(LINE_SEPARATOR)

    subdir_content = os.listdir(os.getcwd())
    subdir_list = [x for x in subdir_content if os.path.isdir(os.path.join(os.getcwd(), x))]
    iter_key = 0
    for el in subdir_list:
        iter_key += 1
        print('\t {}. {}'.format(iter_key, el))
    print(LINE_SEPARATOR)
    print('')


def go_to_folder():
    """
    Изменяет положение рабочей директории
    """

    clear()
    show_subdirectory_list()
    answer = input('Введите папку (".." для перехода на уровень выше): ')
    if answer == '..':
        new_path = os.path.join(os.getcwd(), os.pardir)
    else:
        new_path = os.path.join(os.getcwd(), answer)

    if os.path.isdir(new_path):
        os.chdir(new_path)
        print('Текущая папка изменена')
    else:
        print('Указанная папка не существует')

    show_current_path()


def folder_content():
    """
    Выводит на экран содержимое директории
    """

    print('Содержимое текущей папки:')
    print(LINE_SEPARATOR)

    subdir_content = os.listdir(os.getcwd())
    iter_key = 0
    for el in subdir_content:
        iter_key += 1
        el_type = 'folder-->' if os.path.isdir(el) else 'file---->'
        print('\t {}. \t{}\t{}'.format(iter_key, el_type, el))
    print(LINE_SEPARATOR)
    print('')


def delete_folder():
    """
    Удаление папки
    """

    clear()
    show_subdirectory_list()
    answer = input('Удалить папку: ')
    delete_path = os.path.join(os.getcwd(), answer)
    if os.path.isdir(delete_path):
        shutil.rmtree(delete_path, ignore_errors=True)
        print('Папка {} удалена\n'.format(answer))
    else:
        print('Папка {} не существует\n'.format(answer))


def create_folder():
    """
    Создание папки
    """

    clear()
    show_subdirectory_list()
    answer = input('Создать папку: ')
    make_path = os.path.join(os.getcwd(), answer)
    if not os.path.isdir(make_path):
        os.mkdir(make_path)
        print('Папка {} создана\n'.format(answer))
    else:
        print('Папка {} уже существует\n'.format(answer))
