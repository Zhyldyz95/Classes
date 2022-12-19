# class People:
#
#     def can_walk(self):
#         print('Can walk')
#
#     def can_talk(self):
#         print('Can talk')
#
#
# class Teacher:
#     def can_teach(self):
#         print('Can teach')
#
#     def can_walk(self):
#         print('Can walk')
#
#     def can_talk(self):
#         print('Can talk')
# a = People()
# a.can_walk()


# class People:
#
#     def can_walk(self):
#         print('Can walk')
#
#     def can_talk(self):
#         print('Can talk')
#
#
# class Teacher(People):
#     def can_teach(self):
#         print('Can teach')
#
#
# class Driver(People):
#     def can_drive(self):
#         print('Can drive')
#
# Bob = Teacher()
# Bob.can_talk()
# a = Driver()
# a.can_walk()



class People:

    def can_walk(self):
        print('Can walk')

    def can_talk(self):
        print('Can talk')


class Teacher(People):
    def can_teach(self):
        print('Can teach')


class Driver(Teacher):
    def can_drive(self):
        print('Can drive')



class Qwe(Driver):
    def qwer(self):
        pass

Bob = Teacher()
Bob.can_talk()
a = Driver()
a.can_teach()
b = Qwe()
b.can_talk()