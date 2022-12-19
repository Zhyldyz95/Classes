# class Car:
#     def __init__(self, model, color, year):
#         self.model= model
#         self.color = color
#         self.year = year
#
#     def __len__(self):
#         return len(self.model)
#
#     def __str__(self):
#         return f'Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}'
#
#
# Toyota = Car('Camry', 'white', '2015')
# print(len(Toyota))

class Car:
    def __init__(self, model, color, year):
        self.model= model
        self.color = color
        self.year = year

    def __len__(self):
        return len(self.model)

    def __str__(self):
        #return f'Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}'
        return 'Toyota'

Toyota = Car('Camry', 'white', '2015')
print(Toyota.__dict__)



# class Car:
#     def __init__(self, model, color, year):
#         self.model= model
#         self.color = color
#         self.year = year
#
#     def __len__(self):
#         return len(self.model)
#
#     def __str__(self):
#         return f'Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}'
#
#
# Toyota = Car('Camry', 'white', '2015')
# print(dir(Toyota))



# class Car:
#     def __init__(self, model, color, year):
#         self.model= model
#         self.color = color
#         self.year = year
#
#     def __len__(self):
#         return len(self.model)
#
#     def __dir__(self):
#         return ['model', 'color', 'year']
#
#     def __str__(self):
#         return f'Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}'
#
# Toyota = Car('Camry', 'white', '2015')
# print(dir(Toyota))




# class Car:
#     def __init__(self, model, color, year):
#         self.model= model
#         self.color = color
#         self.year = year
#
#     def __len__(self):
#         return len(self.model)
#
#     def __dir__(self):
#         return ['model', 'color', 'year']
#
#
#     def __str__(self):
#         return f'Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}'
#
#
# Toyota = Car('Camry', 'white', '2015')
# Audi = Car('A8', 'black', '2008')
# print(Toyota)
# print(Audi)



# class Car:
#     def __init__(self, model, color, year):
#         self.model= model
#         self.color = color
#         self.year = year
#
#
#     def getinfo(self):
#         print({
#             'Модель машины': self.model,
#             'Цвет машины': self.color,
#             'Год машины': self.year
#         })
#
#
#     def __len__(self):
#         return len(self.model)
#
#     def __dir__(self):
#         return ['model', 'color', 'year']
#
#
#     def __str__(self):
#         return f'Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}'
#
#
# Toyota = Car('Camry', 'white', '2015')
# Audi = Car('A8', 'black', '2008')
# Toyota.getinfo()
# print(Audi)