import math

def clear():
    """
    Функция для очистки консоли перед выводом/вводом данных
    """
    print("\n" * 100)


clear()

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    try:
        int(n)
        int(m)
    except:
        return 'Ошибка вводных значений'
    else:
        if int(n) >= int(m):
            return 'Ошибка, конец раньше или совпадает с началом'
        elif int(n) <= 0:
            return 'Неверная начальная позиция'
        else:
            if int(m) <= 2:
                return [1, 1]
            else:
                num_fib = [1,1]
                for x in range(2, int(m)-1):
                    num_fib.append(num_fib[x-1]+num_fib[x-2])
                return num_fib[int(n)-1:]


def obj_1():
    print('Результаты - Задача №1:\n')
    start_num = input('Введите номер позиции, с которой начать (от 1): ')
    stop_num = input('Введите номер завершающей позиции: ')
    print('Ряд Фибоначи с {}-го по {} число: {}'.format(start_num, stop_num, fibonacci(start_num,stop_num)))
    print('\n')

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sorted_list = []
    for ind in range(len(origin_list)):
        temp_var = origin_list[0]
        for x in range(len(origin_list)):
            if origin_list[x] < temp_var:
                temp_var = origin_list[x]
        origin_list.remove(temp_var)
        sorted_list.append(temp_var)
    return sorted_list


def obj_2():
    print('Результаты - Задача №2:\n')
    print('Сортировка списка: [2, 10, -12, 2.5, 20, -11, 4, 4, 0]\n'
          'Результат: {}'.format(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter(func, iter).
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, itr):
    try:
        result = []
        for x in range(len(itr)):
            if func(x):
                result.append(x)
        return result
    except:
        return 'Ошибка'


def obj_3():
    print('Результаты - Задача №3:\n')
    func = lambda x: x % 2 == 0
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Пример функции: lambda x: x % 2 == 0')
    print('Вводные данные: {}'.format(list))
    print('Результат: {}'.format(my_filter(func, list)))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_line(coords_list):
    if (coords_list[0][0] - coords_list[1][0]) / (coords_list[2][0] - coords_list[1][0]) == \
            (coords_list[0][1] - coords_list[1][1]) / (coords_list[2][1] - coords_list[1][1]):
        return True
    else:
        return False

def is_par(coords_list):
    try:
        for xy in coords_list:
            float(xy[0])
            float(xy[1])
    except:
        return 'Ошибка вводных данных'
    else:
        centr_1_x = round((coords_list[0][0] + coords_list[3][0]) / 2, 10)
        centr_1_y = round((coords_list[0][1] + coords_list[3][1]) / 2, 10)
        centr_2_x = round((coords_list[1][0] + coords_list[2][0]) / 2, 10)
        centr_2_y = round((coords_list[1][1] + coords_list[2][1]) / 2, 10)

        if is_line(coords_list):
            return '3 точки на одной линии'

        if centr_1_x == centr_2_x and centr_1_y == centr_2_y:
            return '{} {} / {} {} - координаты центра, это параллелограмм'.format(centr_1_x, centr_1_y, centr_2_x, centr_2_y)

        centr_1_x = round((coords_list[0][0] + coords_list[1][0]) / 2, 10)
        centr_1_y = round((coords_list[0][1] + coords_list[1][1]) / 2, 10)
        centr_2_x = round((coords_list[2][0] + coords_list[3][0]) / 2, 10)
        centr_2_y = round((coords_list[2][1] + coords_list[3][1]) / 2, 10)

        if centr_1_x == centr_2_x and centr_1_y == centr_2_y:
            return '{} {} / {} {} - координаты центра, это параллелограмм'.format(centr_1_x, centr_1_y, centr_2_x, centr_2_y)

        centr_1_x = round((coords_list[0][0] + coords_list[2][0]) / 2, 10)
        centr_1_y = round((coords_list[0][1] + coords_list[2][1]) / 2, 10)
        centr_2_x = round((coords_list[1][0] + coords_list[3][0]) / 2, 10)
        centr_2_y = round((coords_list[1][1] + coords_list[3][1]) / 2, 10)

        if centr_1_x == centr_2_x and centr_1_y == centr_2_y:
            return '{} {} / {} {} - координаты центра, это параллелограмм'.format(centr_1_x, centr_1_y, centr_2_x, centr_2_y)

        return 'Неть - не параллелограмм'


def obj_4():
    print('Результаты - Задача №4:\n')
    print('Введите координаты вершин А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4)')
    coords = []
    for ind in range(4):
        coord_x = float(input('Введите координату X вершины номер {}: '.format(ind+1)))
        coord_y = float(input('Введите координату Y вершины номер {}: '.format(ind + 1)))
        coords.append((coord_x, coord_y))

    print('Координаты: {}'.format(coords))
    print(is_par(coords))

# Интерфейс

alert = """
[1] Задача №1
[2] Задача №2
[3] Задача №3
[4] Задача №4
[a] Выполнить все задачи
[q] Завершить работу

Выберите действие: """

answer = ''
while answer not in ('q', 'Q'):
    answer = input(alert)
    clear()
    if answer is '1':
        obj_1()
    elif answer is '2':
        obj_2()
    elif answer is '3':
        obj_3()
    elif answer is '4':
        obj_4()
    elif answer in ('a', 'A'):
        obj_1()
        obj_2()
        obj_3()
        obj_4()

print('Спасибо, за использования нашего программного обеспечения, удачи.')