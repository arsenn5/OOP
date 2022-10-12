from homewr1 import Hero


class Air(Hero):
    strength = 23

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def Brand_phrase(self, br):
        self.fly = True
        print(f'fly in the {self.fly}_phrase')

    def Gen_x(self):
        pass


class earthly(Hero):
    strength = 34

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def Brand_phrase(self, br):
        self.fly = True
        print(f'fly in the {self.fly}_phrase')

    def Gen_x(self):
        pass


class space(Hero):
    strength = 88

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def Brand_phrase(self, br):
        self.fly = True
        print(f'fly in the {self.fly}_phrase')

    def Gen_x(self):
        pass


sd = Air("Bob", 'IH', 34, 56)
print(sd.name, sd.hp, sd.damage, sd.nickname)
sd.Brand_phrase(Air)
ds = earthly('Gam', 'ER_67', 300, 50)
print(ds.name, ds.hp, ds.damage, ds.nickname)
ds.Brand_phrase(earthly)
dr = space('Jui', 'HG-65', 60, 10)
print(dr.name, dr.hp, dr.damage, dr.nickname)
dr.Brand_phrase(space)
