#!/usr/bin/python3

import random

"""
Успел до начала урока сделать только это
но хочу закончить полностью 
"""

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

class Card:

    def __init__(self, user):
        try:
            self.nums
        except AttributeError:
            self.newCard()
        self.user = user

    def newCard(self):
        nums = []
        while len(nums) < 15:
            value = random.randint(1, 91)
            if value not in nums:
                nums.append(value)
        self.nums = {a: 0 for a in range(27)}
        while len(nums) > 0:
            pos = random.randint(0, 26)
            if self.nums[pos] == 0:
                line = pos // 9
                count = 0
                for x in range(9):
                    if self.nums[x+line*9] == 0:
                        count += 1
                if count > 4:
                    self.nums[pos] = nums.pop()

    def show(self):
        print(f'Карточка игрока: {self.user}')
        print('------------------------------------')
        for x in range(3):
            line = list(self.nums.values())[x * 9:x * 9 + 9]
            print('{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} '.format(*line))
        print('------------------------------------\n')

    def check_keg(self, keg):
        for ind in self.nums:
            if keg == self.nums[ind]:
                print(f'Найдено совпадение у игрока {self.user} => {keg}\n')
                self.nums[ind] = '-'

    def check_win(self):
        for ind in self.nums:
            try:
                int(self.nums[ind])
                if int(self.nums[ind]) > 0:
                    return False
            except ValueError:
                if str(self.nums[ind]) != '-':
                    return False
        return True

class Kegs:

    def __init__(self):
        try:
            self.kegs
        except AttributeError:
            self.kegs = [a for a in range(1, 91)]
            random.shuffle(self.kegs)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.kegs) > 0:
            return self.kegs.pop()
        else:
            raise StopIteration

    def __int__(self):
        return self

    def show(self):
        print(self.kegs)


def clear():
    """
    Функция для очистки консоли перед выводом/вводом данных
    """
    print("\n" * 100)


kegs = Kegs()
user_card = Card('Пользователь')
comp_card = Card('Компьютер')
showen = ''

for keg in kegs:
    clear()
    showen = str(keg) + ' ' + showen
    comp_card.check_keg(keg)
    user_card.check_keg(keg)

    print(f'Открытые бочонки: {showen}\n')

    comp_card.show()
    user_card.show()

    if user_card.check_win():
        print('!!!!!!Вы выиграли!!!!!!')
        break
    elif comp_card.check_win():
        print('!!!!!!Вы проиграли!!!!!!')
        break
    else:
        turn = input('Следующий ход? (Нажмите Enter, \"q\" - для выхода): ')
        if turn == 'q':
            print('Спасибо за игру, приходите еще!\n')
            break
