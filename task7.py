class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
    def show(self):
        return f'Name: {self.name}, Group: {self.group}'
    def __del__(self):
        print('Объект удален')

a = Student('Zhyldyz', 'Python')
print(a.show())
del Student