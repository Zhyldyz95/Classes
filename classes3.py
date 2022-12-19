# class Cat:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#
#     def __del__(self):
#         print('Объект удален')
#
# cat = Cat('Casper', 'Siam', 2)
# #print(cat.breed)
# del cat


# class ClassName:
#     def __new__(cls, *args, **kwargs):
#         print('__new__')
#         return super(ClassName, cls).__new__(cls, *args, **kwargs)
#
#     def __init__(self):
#         print('__init__')
#
# v1 = ClassName
# v2 = ClassName


# class Database:
#     def __init__(self, login, passsword, port):
#         self.login = login
#         self.passsword = passsword
#         self.port = port
#
#     def connect(self):
#         return f'Connect with db: {self.login}, {self.passsword}, {self.port}'
#
# db = Database('login', 'pass', 50)
# print(db.connect())
#
# db2 = Database('logitn', 'paswws', 40)
# print(db2.connect())


# class Database:
#     __instance = None  # Ссылка на экземпляр класса
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, login, password, port):
#         self.login = login
#         self.password = password
#         self.port = port
#
#     def connect(self):
#         return f'Connect with db: {self.login}, {self.password}, {self.port}'
#
#
# db = Database('login', 'pass', 50)
# db2 = Database('logitn', 'paswws', 40)
# print(db.connect())
# print(db2.connect())
# print(id(db), id(db2))


class Qwe:
    def __init__(self, arg):
        self.arg = arg

    def ret(self):
        print(self.arg)

    def __call__(self, *args, **kwargs):
        print(args)
        if not isinstance(args[0], str):
            return "Значение должно быть строкой"
        return args[0].strip(self.arg)
s = Qwe('1234567890')
s.ret()
re = s('12Hello34')
print(re)
#s1.__call__(123456) так можно вызвать метод
#repr() тоже самое как __str__ возвпащает метод представоения класса, вместо __str__ можно использовать
#__str__