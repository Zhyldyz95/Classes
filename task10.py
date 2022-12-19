class Adeel:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        if name == 'Адиль' or name == 'Adil' or name == 'Adeel':
            self.name = name
        # elif name != 'Адиль' or name != 'Adil' or name != 'Adeel':
        #     print(f'Я не {self.name}. Я {self.name}')
        else:
            print(f'Я не {name}, а Адиль!')
        self.age = age



name = input('Введите имя: ')
a = Adeel(name, 6)



