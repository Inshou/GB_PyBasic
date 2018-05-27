import math
from hw_default_libs import clear
from hw_default_libs import interface


class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # Коэффиценты линейной функции Аx + By + C = 0
        self.abc = {
            'a': self.y1 - self.y2,
            'b': self.x2 - self.x1,
            'c': self.x1 * self.y2 - self.x2 * self.y1}
        # Угловой коэффицент
        self.k = - self.abc['a'] / self.abc['b']
        # Длинна отрезка
        self.length = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def get_sides(self):
        side = {}
        side[0] = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2))
        side[1] = math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3))
        side[2] = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1))
        return side

    def space(self):
        half_p = (self.perimeter())/2
        space = math.sqrt(abs(half_p * (half_p - self.get_sides()[0])
                              * (half_p - self.get_sides()[1])
                              * (half_p - self.get_sides()[2])))
        return space

    def print_space(self):
        print('Площадь треугольника: A({} {}) B({} {}) C({} {}) = {}\n'.format(self.x1, self.y1,
                                                                               self.x2, self.y2,
                                                                               self.x3, self.y3,
                                                                               self.space()))

    def height(self):
        line_ab = Line(self.x1, self.y1, self.x2, self.y2)
        height = abs( line_ab.abc['a'] * self.x3 + line_ab.abc['b'] * self.y3 + line_ab.abc['c']) \
                 / math.sqrt(line_ab.abc['a'] ** 2 + line_ab.abc['b'] ** 2)
        return height

    def print_height(self):
        print('Высота треугольника: A({} {}) B({} {}) C({} {}) из точки С на сторону АБ = {}\n'.format(self.x1, self.y1,
                                                                                                   self.x2, self.y2,
                                                                                                   self.x3, self.y3,
                                                                                                   self.height()))

    def perimeter(self):
        result = self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2]
        return result

    def print_perimeter(self):
        print(f"Периметр треугольника: A({self.x1} {self.y1}) B({self.x2} {self.y2}) C({self.x3} {self.y3}) = 0"
              f"{self.perimeter()}\n")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class EquilateralTrapezoid:
    """
    Класс равнобокой трапеции заданной последовательностью координат x и y
    x1, y1, x2, y2, x3, y3, x4, y4 - соответственно
    """

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.line_ab = Line(self.x1, self.y1, self.x2, self.y2)
        self.line_bc = Line(self.x2, self.y2, self.x3, self.y3)
        self.line_cd = Line(self.x3, self.y3, self.x4, self.y4)
        self.line_da = Line(self.x4, self.y4, self.x1, self.y1)
        self.perimeter = self.line_ab.length + self.line_bc.length + self.line_cd.length + self.line_da.length
        if self.check() == 'ab-cd':
            self.side_lenght = self.line_bc.length
        elif self.check() == 'bc-da':
            self.side_lenght = self.line_ab.length



    def check(self):
        if self.line_ab.k == self.line_cd.k \
                and self.line_bc.k != self.line_da.k \
                and self.line_bc.length == self.line_da.length:
            return 'ab-cd'
        elif self.line_bc.k == self.line_da.k \
                and self.line_ab.k != self.line_cd.k \
                and self.line_ab.length == self.line_cd.length:
            return 'bc-da'
        else:
            return False

    def print_check(self):
        if self.check() == 'ab-cd':
            result = 'Это равнобокая трапеция, с боками BC и DA'
        elif self.check() == 'bc-da':
            result = 'Это равнобокая трапеция, с боками AB и CD'
        print(f"Трапеция A({self.x1} {self.y1}) B({self.x2} {self.y2}) "
              f"C({self.x3} {self.y3}) D({self.x4} {self.y4}): {result}\n")

    def space(self):
        if self.check() == 'ab-cd':
            midline_lenght = (self.line_ab.length + self.line_cd.length) / 2
            height = math.sqrt(self.line_cd.length ** 2 - (self.line_ab.length - self.line_cd.length) ** 2)
            space = height * midline_lenght
            return space
        elif self.check() == 'bc-da':
            midline_lenght = (self.line_bc.length + self.line_da.length) / 2
            height = math.sqrt(self.line_ab.length ** 2 - (self.line_bc.length - self.line_da.length) ** 2)
            space = height * midline_lenght
            return space
        else:
            return False

    def print_space(self):
        print(f"Площадь равнобокой трапеции: A({self.x1} {self.y1}) B({self.x2} {self.y2}) "
              f"C({self.x3} {self.y3}) D({self.x4} {self.y4}) = {self.space()}\n")

    def print_side_sizes(self):
        print(f"Длины сторон трапеция: A({self.x1} {self.y1}) B({self.x2} {self.y2}) "
              f"C({self.x3} {self.y3}) D({self.x4} {self.y4}) \n"
              f"Длина АБ: {self.line_ab.length} \n"
              f"Длина BC: {self.line_bc.length} \n"
              f"Длина CD: {self.line_cd.length} \n"
              f"Длина DA: {self.line_da.length} \n")

    def print_perimeter(self):
        print(f"Длина периметра трапеция: A({self.x1} {self.y1}) B({self.x2} {self.y2}) = {self.perimeter} \n")


clear()

triangle_a = Triangle(-5, 3, 10, -2, 4, 3)
trapezoid = EquilateralTrapezoid(0, 0, 2, 4, 6, 4, 8, 0)

commands = {'0': 'Площадь треугольника',
            '1': 'Высота треугольника',
            '2': 'Периметр треугольника',
            '3': 'Проверка равнобокой трапеции',
            '4': 'Площадь равнобокой трапеции',
            '5': 'Длины сторон трапеции',
            '6': 'Периметр трапеции'
            }

tasks = {'0': triangle_a.print_space,
         '1': triangle_a.print_height,
         '2': triangle_a.print_perimeter,
         '3': trapezoid.print_check,
         '4': trapezoid.print_space,
         '5': trapezoid.print_side_sizes,
         '6': trapezoid.print_perimeter
         }

interface(commands, tasks)