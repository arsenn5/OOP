class Col:
    nomber1 = int(input('Введите число1 '))
    namber2 = int(input('Введите число2 '))
    def __init__(self, sun1=nomber1, sun2=namber2):
        self.sun1 = sun1
        self.sun2 = sun2


class Add(Col):
    def __add__(self):
        return self.sun1 + self.sun2


class Sub(Col):
    def __sub__(self):
        return self.sun1 - self.sun2


class Mul(Col):
    def __mul__(self):
        return self.sun1 * self.sun2


class Truediv(Col):
    def __truediv__(self):
        return self.sun1 / self.sun2

sd = Add()
print(sd.__add__())

se = Sub()
print(se.__sub__())

ji = Mul()
print(ji.__mul__())

ko = Truediv()
print(ko.__truediv__())
