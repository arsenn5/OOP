class Human:
    instance = None

    def __new__(cls, name, age, growth):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

            cls.instance.name = name
            cls.instance.age = age
            cls.instance.growth = growth

            return cls.instance
        else:
            print("Экземпляр уже есть")

my_obj = Human('Asyl', 56, 178)
print(my_obj.name)
obj2 = Human("ASSA", 15, 176)