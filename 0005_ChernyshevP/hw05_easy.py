import os
import shutil
# from pprint import pprint

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def directory_list_creator(input_list, path=os.getcwd()):
    """
    Функция создания списка директорий
    """

    try:
        for el in input_list:
            os.mkdir(os.path.join(path, el))
            # print(f'создана директория {el}')
    except FileExistsError:
        return 'Ошибка: директория уже существует'

    return 'Список директорий создан: {}'.format(input_list)


def directory_list_remover(input_list, path=os.getcwd()):
    """
    Функция удаление списка директорий

    """

    try:
        for el in input_list:
            os.rmdir(os.path.join(path, el))
            # print(f'создана директория {el}')
    except FileNotFoundError:
        return 'Ошибка: директория не существует'

    return 'Директории уничтожены: {}'.format(input_list)


if __name__ == "__main__":
    dir_list = ['dir_'+str(x) for x in range(1, 10)]
    print(directory_list_creator(dir_list))
    print(directory_list_remover(dir_list))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def subdirectory_list(path=os.getcwd()):
    """
    Функция возвращает список подпапок
    :param path: путь к рабочей директории, по умолчанию директория запуска скрипта
    :return: список директорий
    """
    try:
        subdir_content = os.listdir(path)
    except FileExistsError:
        return 'Ошибка'

    result = [x for x in subdir_content if not os.path.isfile(os.path.join(path, x))]

    return result


if __name__ == "__main__":
    print('Список папок в текущей папке: {}'.format(subdirectory_list()))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

self_path = os.sys.argv[0]
copy_path = self_path+'.copy'
result = shutil.copy(self_path, copy_path)

if __name__ == "__main__":
    print(f'Создана копия текущего скрипта - {result}')
