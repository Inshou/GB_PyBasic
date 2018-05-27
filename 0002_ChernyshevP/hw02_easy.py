import random


# Функция для очистки консоли перед выводом/вводом данных
def clear():
    print("\n" * 100)


# Функция генерации рандомного списка
def random_list(count, random_el='123456789QWERTYUIOPASDFGHJKLZXCVBNM', len=2):
    random_el = list(random_el)
    result = []
    for i in range(0, count):
        random.shuffle(random_el)
        rndstr = ''.join([random.choice(random_el) for x in range(len)])
        result.append(rndstr)

    return result


# очистка экрана при запуске
clear()


# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


def obj_1():
    print('Результаты - Задача №1:\n')

    fruits = ['яблоко', 'банан', 'киви', 'арбуз']
    i = 0
    max_item_len = len(max(fruits, key=len))  # вычисление самого длинного элемента, для корректного выравнивания

    for fruit in fruits:
        i += 1
        print('{0}. {1:>{2}}'.format(i, fruit, max_item_len))

    print('\n')


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


def obj_2():
    print('Результаты - Задача №2:\n')

    list_A = random_list(100)
    list_B = random_list(100)
    list_C = [x for x in list_A if x not in list_B]
    list_D = [x for x in list_B if x in list_A]

    print('Список А: {} '.format(list_A))
    print('Список B: {} \n'.format(list_B))
    print('Список A - B: {} '.format(list_C))
    print('Совпадения: {} \n'.format(list_D))

    print('\n')


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


def obj_3():
    print('Результаты - Задача №3:\n')

    list_A = random_list(10, '012345689', 3)
    list_A = [int(x) for x in list_A]
    list_B = []

    for el in list_A:
        if el % 2 == 0:
            out = el * 4
        else:
            out = el * 2
        list_B.append(out)

    print('Список А: {} '.format(list_A))
    print('Список B: {} \n'.format(list_B))

# Интерфейс

alert = """
[1] Задача №1
[2] Задача №2
[3] Задача №3
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
    elif answer in ('a', 'A'):
        obj_1()
        obj_2()
        obj_3()

print('Спасибо, за использования нашего программного обеспечения, удачи.')
