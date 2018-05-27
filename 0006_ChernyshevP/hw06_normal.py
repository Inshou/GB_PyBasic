from hw_default_libs import clear
from hw_default_libs import interface

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Man:

    def __init__(self, id, first_name, second_name, middle_name, sex, parents=[], date_of_birth='0.00.0000'):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.middle_name = middle_name
        self.sex = sex
        self.parents = parents
        self.date_of_birth = date_of_birth

    @property
    def full_name(self):
        return self.second_name + ' ' + self.first_name + ' ' + self.middle_name

    @property
    def short_name(self):
        return self.second_name + ' ' + self.first_name[0] + '.' + self.middle_name[0] + '.'

class Student(Man):
    def __init__(self, id, first_name, second_name, middle_name, sex, parents, tclass, date_of_birth='0.00.0000'):
         Man.__init__(self, id, first_name, second_name, middle_name, sex, parents, date_of_birth)
         self.tclass = tclass


class Parent(Man):
     def __init__(self, id, first_name, second_name, middle_name, sex, parents, childrens=[], date_of_birth='0.00.0000'):
         Man.__init__(self, id, first_name, second_name, middle_name, sex, parents, date_of_birth)
         self.childrens = childrens


class Teacher(Man):
    def __init__(self, id, first_name, second_name, middle_name, sex, desceplines=[], tclasses=[]):
        Man.__init__(self, id, first_name, second_name, middle_name, sex)
        self.desceplines = desceplines
        self.tclasses = tclasses


def print_classes(students):
    list_of_classes = []
    for student in students:
        if student.tclass not in list_of_classes:
            list_of_classes.append(student.tclass)
    print(f'Список классов школы: {list_of_classes}\n')


def print_students(students):
    tclass = input('Укажите номер и литеру класса (оставте поле пустым, чтобы получить полный список учеников): ')
    print(f'\nСписок учеников {tclass}:')
    for student in students:
        if student.tclass == tclass or tclass == '':
            print(f'{student.id} {student.short_name}')
    print()


def get_descepline_list(teachers, tclass):
    result = []
    for teacher in teachers:
        if tclass in teacher.tclasses:
            for descipline in teacher.desceplines:
                if descipline not in result:
                    result.append(descipline)
    return result


def print_desceplines(students, teachers):
    student_ident = input('Укажите ID ученика: ')
    try:
        int(student_ident)
    except ValueError:
        print('Вы ввели неверные данные')
    else:
        for student in students:
            if student.id == int(student_ident):
                print(f'\nУченик: {student.full_name}\nКласс: {student.tclass}')
                descepline_list = get_descepline_list(teachers, student.tclass)
                print(f'Список предметов: {descepline_list}\n')


def print_parents(students, parents):
    student_ident = input('Укажите ID ученика: ')
    try:
        int(student_ident)
    except ValueError:
        print('Вы ввели неверные данные')
    else:
        for student in students:
            if student.id == int(student_ident):
                print(f'\nУченик: {student.full_name}\nКласс: {student.tclass} \n'
                      'Родители:')
                for parent in parents:
                    if parent.id in student.parents:
                        print('\t' + parent.full_name)
                print()


def print_teachers(teachers):
    tclass = input('Укажите номер и литеру класса (оставте поле пустым, чтобы получить полный список учитилей): ')
    print(f'\nСписок преподавателей {tclass}:')
    for teacher in teachers:
        if tclass in teacher.tclasses or tclass == '':
            print(f'{teacher.id} {teacher.full_name}')
    print()



clear()

students = [Student(1, 'Александр', 'Пушкин', 'Артёмович', 'M', [1, 2], '9А', '10.10.2000'),
            Student(2, 'Сергей', 'Сидоренко', 'Витальевич', 'M', [3, 4], '9А', '7.12.1999'),
            Student(3, 'Алефтина', 'Пушкина', 'Артёмовна', 'Ж', [1, 2], '8Б', '1.04.2001'),
            Student(4, 'Иван', 'Матросов', 'Геннадьевич', 'М', [5, 6], '8Б', '12.02.2001'),
            Student(5, 'Галина', 'Матросова', 'Геннадьевна', 'Ж', [5, 6], '8А', '20.11.2000'),
            Student(6, 'Михаил', 'Задумов', 'Алексеевич', 'М', [7], '9Б'),
            Student(7, 'Мария', 'Пельмяшова', 'Антоновна', 'Ж', [8, 9], '9Б'),
            Student(8, 'Юрий', 'Амосов', 'Сергеевич', 'М', [10], '8Б'),
            Student(9, 'Олег', 'Амосов', 'Сергеевич', 'М', [10], '8Б'),
            Student(10, 'Виталий', 'Кашков', 'Александрович', 'М', [11, 12], '10А'),
            Student(11, 'Павел', 'Сучков', 'Степанович', 'М', [13, 14], '10А'),
            Student(12, 'Алексей', 'Ефимов', 'Алексеевич', 'М', [15], '10А'),
            Student(13, 'Елена', 'Головач', 'Георгиевна', 'Ж', [16], '10А'),
            Student(14, 'Дарья', 'Головач', 'Георгиевна', 'Ж', [16], '9А'),
            Student(15, 'Жанна', 'Фриски', 'Генадьевна', 'Ж', [17, 18], '9Б'),
            Student(16, 'Степан', 'Портнов', 'Васильевич', 'М', [19, 20], '8Б'),
            Student(17, 'Василий', 'Портнов', 'Васильевич', 'М', [19, 20], '10В'),
            Student(18, 'Евгения', 'Портнова', 'Васильевна', 'Ж', [19, 20], '9А'),
            ]


parents = [Parent(1, 'Сергей', 'Пушки', 'Федорович', 'M', [], [1, 3, 19, 21]),
           Parent(2, 'Анастасия', 'Пушкина', 'Сергеевна', 'Ж', [], [1, 3, 19, 21]),
           Parent(3, 'Виталий', 'Сидоренко', 'Петрович', 'М', [], [2, 20]),
           Parent(4, 'Елена', 'Сидоренко', 'Михайловна', 'Ж', [], [2, 20]),
           Parent(5, 'Геннадий', 'Матросов', 'Александрович', 'М', [], [4, 5]),
           Parent(6, 'Анна', 'Матросова', 'Павловна', 'Ж', [], [4, 5]),
           Parent(7, 'Мария', 'Задумова', 'Васильевна', 'Ж', [], [6]),
           Parent(8, 'Антон', 'Пельмяшов', 'Леонидович', 'М', [], [7]),
           Parent(9, 'Антонина', 'Пельмяшова', 'Максимовна', 'Ж', [], [7]),
           Parent(10, 'Сергей', 'Амосов', 'Сереевич', 'М', [], [8, 9]),
           Parent(11, 'Александр', 'Кашков', 'Андреевич', 'М', [], [10]),
           Parent(12, 'Александра', 'Кашкова', 'Валерьевна', 'Ж', [], [10]),
           Parent(13, 'Степан', 'Сучков', 'Иванович', 'М', [], [11]),
           Parent(14, 'Агафья', 'Сучкова', 'Прохоровна', 'Ж', [], [11]),
           Parent(15, 'Александра', 'Ефимова', 'Сергееввна', 'Ж', [], [12]),
           Parent(16, 'Георгий', 'Головач', 'Фёдорович', 'М', [], [13, 14]),
           Parent(17, 'Геннадий', 'Фуфелов', 'Патапович', 'М', [], [15]),
           Parent(18, 'Александра', 'Фуфелова', 'Андреевна', 'Ж', [], [15]),
           Parent(19, 'Василий', 'Портнов', 'Иваночи', 'М', [16, 17, 18]),
           Parent(20, 'Василиса', 'Портнова', 'Фёдоровна', 'Ж', [16, 17, 18])
           ]

teachers = [Teacher(1, 'Альберт', 'Офонькин', 'Карлович', 'М', ['математика'], ['8А', '8Б', '9А', '9Б']),
            Teacher(2, 'Алёна', 'Говорун', 'Павловна', 'Ж', ['алгебра', 'геометрия'], ['10А', '10В']),
            Teacher(3, 'Алефтина', 'Мозговая', 'Георгиевна', 'Ж', ['русский языык', 'литература'], ['8А', '8Б', '9А', '9Б', '10А', '10В']),
            Teacher(4, 'Марат', 'Маркелов', 'Леонидович', 'Ж', ['география'], ['8А', '8Б', '9А', '9Б', '10А']),
            Teacher(5, 'Светлана', 'Умнова', 'Сергеевна', 'Ж', ['биология'], ['8А', '8Б', '9А', '9Б', '10А'])
]

commands = {'0': 'Список классов школы',
            '1': 'Список учеников указанного класса школы',
            '2': 'Список предметов ученика',
            '3': 'ФИО родителей ученика',
            '4': 'Список учителей класса'
            }

tasks = {'0': print_classes,
         '1': print_students,
         '2': print_desceplines,
         '3': print_parents,
         '4': print_teachers
         }

args = {'0': [students],
        '1': [students],
        '2': [students, teachers],
        '3': [students, parents],
        '4': [teachers]
        }

interface(commands, tasks, args)