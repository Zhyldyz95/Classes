# class Employee:
#     salary = 0
#     count = 0
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#
#     def add_salary(self, a):
#         Employee.salary += a
#         return Employee.salary
#
#     def full_name(self):
#         return f'{self.name} {self.last_name}'
#
#
# per1 = Employee('John', 'Snow')
# per2 = Employee('Sam', 'Smit')
#
# per1.add_salary(1000)
# per1.salary += 1000
# print(per1.salary)
# print(per2.salary)


class Employee:
    salary = 0
    count = 0

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def add_salary(self, a):
        self.salary += a
        return f'{self.name} получает прибавку в размере {a} {Employee.salary}'

    def full_name(self):
        return f'full name: {self.name} {self.last_name}'


per1 = Employee('John', 'Snow')
per2 = Employee('Sam', 'Smit')
per2.add_salary(100)
print(per1.add_salary(1000))
print(per1.salary)
print(per2.salary)