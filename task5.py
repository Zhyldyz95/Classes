class Zoo:
    def __init__(self):
        self.animal_1 = "Тигр"
        self.animal_2 = "Бегемот"
        self.animal_3 = "Жираф"



a = Zoo()
print(a.animal_1)
a.animal_1 = "Лев"
print(a.animal_1)
print(a.animal_2)
print(a.animal_3)
a.animal_3 = "Змея"
print(a.animal_3 )
a.animal_4 = [a.animal_2, a.animal_3]
print(a.animal_4)


