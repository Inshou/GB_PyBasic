

def clear():
    """
    Функция для очистки консоли перед выводом/вводом данных
    """
    print("\n" * 100)


clear()

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    try:
        float(number)
        int(ndigits)
    except ValueError:
        print('Не верно введены данные, проверьте используете ли вы правильный раздилитель')
        return False
    else:
        if int(ndigits) >= 0:
            number = str(number)
            if number.find('.') >= 0:
                int_index = number.index('.')
                int_number = number[0:int_index]
                int_remain = number[int_index+1:len(number)]
                if len(int_remain) > int(ndigits):
                    int_remain = int_remain[0:int(ndigits)]
                result = str(int_number) + '.' + str(int_remain)
                return result
            else:
                print('Число {} и так целое'.format(number))
            return True
        else:
            print('Не верно указано количество знаков для округления')
            return False


def obj_1():
    print('Результаты - Задача №1:\n')

    print('Округление числа 2.1234567, до 5-го знака: {}'.format(my_round(2.1234567, 5)))
    print('Округление числа 2.1999967, до 5-го знака: {}'.format(my_round(2.1999967, 5)))
    print('Округление числа 2.9999967, до 5-го знака: {}\n'.format(my_round(2.9999967, 5)))

    number = input('Введите число: ')
    ndigits = input('До какого знака округлить? ')
    answer = my_round(number, ndigits)

    if answer :
        print('Округление числа {}, до {}-го знака: {}'.format(number, ndigits, answer))
        pass

    print('\n')

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    try:
        int(ticket_number)
    except:
        return 'Ошибка не верные данные'
    else:
        if len(str(ticket_number)) != 6:
            return 'Не верное количество символов'
        else:
            num_a = str(ticket_number)[:3]
            num_b = str(ticket_number)[3:]
            luck_a = 0
            luck_b = 0
            for num in num_a:
                luck_a += int(num)
            for num in num_b:
                luck_b += int(num)
            if luck_a == luck_b:
                return f'Число А {num_a} и число b {num_b} совпадают, билет счастливый'
            else:
                return f'Число А {num_a} и число b {num_b} не совпадают, билет не счастливый'


def obj_2():
    print('Результаты - Задача №2:\n')

    print(lucky_ticket(123006))
    print(lucky_ticket(12321))
    print(lucky_ticket(436751))

    print('\n')

# Интерфейс

alert = """
[1] Задача №1
[2] Задача №2
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
    elif answer in ('a', 'A'):
        obj_1()
        obj_2()

print('Спасибо, за использования нашего программного обеспечения, удачи.')