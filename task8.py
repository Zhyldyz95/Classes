conf = {
    "exam_max": 30,
    "lab_max": 7,
    "lab_num": 10,
    "k": 0.61
}


class Student:
    def init(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs
        self.lab_num = [0] * self.kwargs.get("lab_num")
        self.exam = 0.0

    def make_lab(self, m, n):
        v = n - 1
        if v >= self.kwargs.get("lab_num"):
            return n
        if m > self.kwargs.get("lab_max"):
            m = self.kwargs.get("lab_max")
        self.lab_num[v] = m
        return self

    def make_exam(self, m):
        if m > self.kwargs.get("exam_max"):
            m = self.kwargs.get("exam_max")
        self.exam = m
        return self

    def is_certified(self):
        summ = self.exam + sum(self.lab_num)
        kef = ((self.kwargs.get("lab_max")*(self.kwargs.get("lab_num")))+self.kwargs.get("exam_max"))*self.kwargs.get("k")
        if summ >= kef:
            return f"{summ}, True"
        else:
            return f"{summ}, False"


s = Student('Zhyldyz', **conf)
print(s.lab_num)
s.make_lab(7, 3)
s.make_lab(7, 2)
s.make_lab(7, 6)
s.make_lab(7, 1)
s.make_lab(7, 7)
print(s.lab_num)
s.make_exam(30)
print(s.is_certified())