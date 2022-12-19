class Factory:

    def engine(self):
        print('Двигатель создан')
    def bridge(self):
        print('Ходовая часть создана')

class Toyota(Factory):

    def wheels(self):
        print('Колёса готовы')
    def windows(self):
        print('Стёкла готовы')

a = Toyota()
a.engine()
a.bridge()
a.wheels()
a.windows()