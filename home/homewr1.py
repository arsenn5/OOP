class Hero:
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def Heal(self, heal):
        print(self.hp + 120)

    def Damage2(self, damage2):
        print(self.damage * 2)

    def Greetins(self, gritins):
        print('my name is', self.name)

    def Brand_phrase(self, br):
        print(f'good will win')

H = Hero(name='ulugbek', nickname='Ulugnir',hp=120,damage=50)
BlackAdam = Hero('Blid', 'Jiro', 200, 100)
DeadPool = Hero('Whaet', 'RIP', +9999, 78)
Blaed = Hero('Piter', 'Vampir', 230, 90)

print(H.name, H.damage, H.nickname, H.hp)
H.Brand_phrase(Hero)

print(Blaed.name, Blaed.damage, Blaed.nickname, Blaed.hp)
Blaed.Greetins(Hero)

print(DeadPool.name, DeadPool.damage, DeadPool.nickname, DeadPool.hp)
DeadPool.Heal(Hero)

print(BlackAdam.name, BlackAdam.damage, BlackAdam.nickname, BlackAdam.hp)
BlackAdam.Damage2(Hero)
