# class TriangleChecker:
#     def __init__(self, sideA, sideB, sideC):
#         self.sideA = sideA
#         self.sideB = sideB
#         self.sideC = sideC
#
#     def is_triangle(self):
#         side_a = float(input('Введите длину стороны a: '))
#         side_b = float(input('Введите длину стороны b: '))
#         side_c = float(input('Введите длину стороны c: '))
#         if side_a + side_b >= side_c and side_b + side_c >= side_a and side_c + side_a >= side_b:
#             print('Ура, можно построить треугольник!')
#         elif side_a < 0 and side_b < 0 and side_c < 0:
#             print('С отрицательными числами ничего не выйдет!')
#         elif side_a == str and side_b != str and side_c != str:
#             print('Нужно вводить только числа!')
#         else:
#             print('Жаль, но из этого треугольник не сделать.')
#
# Form_triangle = TriangleChecker('side_a', 'side_b', 'side_c')
# Form_triangle.is_triangle()



class TriangleChecker:
    def __init__(self, sideA, sideB, sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def is_triangle(self):
        if not isinstance(self.sideA, str) and not isinstance(self.sideB, str) and not isinstance(self.sideC, str):
            if self.sideA > 0 and self.sideB > 0 and self.sideC > 0:
                if self.sideA + self.sideB > self.sideC or self.sideB + self.sideC > self.sideA or self.sideC + self.sideA > self.sideB:
                    print('Ура, можно построить треугольник!')
                else:
                    print('Жаль, но из этого треугольник не сделать.')
            else:
                print('С отрицательными числами ничего не выйдет!')
        else:
            print('Нужно вводить только числа!')

        # def __str__(self):
        #     return self.sideA, self.sideB, self.sideC

Form_triangle = TriangleChecker(1, 66, '6')
Form_triangle.is_triangle()






