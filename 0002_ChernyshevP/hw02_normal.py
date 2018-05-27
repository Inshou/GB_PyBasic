import random
import math
import datetime

# Функция для очистки консоли перед выводом/вводом данных
def clear():
    print("\n" * 100)


# Функция генерации рандомного списка
def random_list(count=10, random_el='123456789QWERTYUIOPASDFGHJKLZXCVBNM', length=2):
    random_el = list(random_el)
    result = []
    for i in range(0, count):
        random.shuffle(random_el)
        rnd_str = ''.join([random.choice(random_el) for x in range(length)])
        result.append(rnd_str)

    return result


def random_date():
    return datetime.date(random.randint(2005, 2025), random.randint(1, 12), random.randint(1, 28))


# очистка экрана при запуске
clear()


# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

def obj_1():
    print('Результаты - Задача №1:\n')

    list_A = [random.randint(-100, 100) for i in range(100)]
    list_B = []

    for item in list_A:
        if item >= 0:
            sqrt =  math.sqrt(item)
            if math.modf(sqrt)[0] == 0:
                list_B.append(int(sqrt))

    print('Список: {} '.format(list_A))
    print('Целые корни элементов списка: {} '.format(list_B))

    print('\n')


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# print(pytils.dt.ru_strftime(u"%d %B %Y", inflected=True, date=datetime.datetime.now()))

def obj_2():
    print('Результаты - Задача №2:\n')

    day_list = ['первое', 'второе', 'третье', 'четвёртое',
                'пятое', 'шестое', 'седьмое', 'восьмое',
                'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое']

    # Какие-то проблемы с локалью, поэтому %E выдает ошибку, решил другим способом
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    r_date = random_date().strftime('%d.%m.%Y')
    in_date = datetime.datetime.strptime(r_date, '%d.%m.%Y')
    f_day = day_list[int(in_date.strftime('%d'))-1]
    f_date = month_list[int(in_date.strftime('%m'))-1]

    print('Случайная дата: {}'.format(r_date))
    print('форматированная дата: {} {} {}-го года'.format(f_day, f_date, in_date.strftime('%Y')))

    print('\n')


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

def obj_3():
    print('Результаты - Задача №3:\n')

    answer = input('Сколько сделать элементов в списке: ')
    if answer.isdecimal():
        answer = int(answer)
    else:
        print('Я вас не понял, использую значение по умолчанию = 10')
        answer = 10

    list_A = [random.randint(-100, 100) for i in range(answer)]
    print('Список: {} '.format(list_A))

    print('\n')


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

def obj_4():
    print('Результаты - Задача №4:\n')

    list_A = [random.randint(0, 20) for i in range(10)]
    list_B = []
    set_A = set(list_A)
    print('Исходных список: {} '.format(list_A))
    print('Список уникльных элементов: {} '.format(set_A))

    for item in list_A:
        if list_A.count(item) < 2:
            list_B.append(item)

    print('Список элементов не имещих дублей: {} '.format(list_B))

    print('\n')


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