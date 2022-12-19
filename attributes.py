# class Cat:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#
# class Dog(Cat):
#     def can_bark(self):
#         pass
#
# a = Cat('Casper', 'Siam', 2)
# print(a.name)
# a.name = 'Whiskas'
# print(a.name)
# a.weight = 10
# a.weight = 20
# b = Dog()
# b.

class Cat:
    def __init__(self, name, breed, age):
        self.__name = name
        self.breed = breed
        self.age = age

    def __can_meow(self):
        return "Meow"
    def __str__(self):
        return self.__name
class Dog(Cat):
    def can_bark(self):
        pass

a = Cat('Casper', 'Siam', 2)
print(dir(a))
print(a._Cat__name)
print(a._Cat__can_meow())
