# class Cat:
#     __name = {
#         'breed': 'siam',
#         'color': 'grey'
#     }
#
#     def __init__(self):
#         self.__dict__ = self.__name
#
#
# s = Cat()
# d = Cat()
# d.name = 'qwert'
# d.color = 'black'
# d.__dict__
# s.__dict__
# print(s.__dict__)
# print(d.__dict__)
# #print(id(s) == id(d)) экземпляр не одинаковый

# attribute slots не позволяет создать другие объекты
class Cat:
    __slots__ = ['name', 'color', 'breed']
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        return f'Name: {self.name}, Color: {self.color}'

s = Cat('Casper', 'grey')
s.breed = 'Siam'
print(s.show())
print(s.breed)

