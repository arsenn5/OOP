class A:
    def __init__(self):

        def __add__(self, other):


class B:
    def __sub__(self, other):


class C:
    def __mul__(self, other):


class D:
    def __truediv__(self, other):


class calculator(A, B, C, D):
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
