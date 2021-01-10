'''
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print('Сумма z1 и z2 равна')
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        print('Произведение z1 и z2 равно')
        return ComplexNumber(self.a * other.a, self.b * other.b)

    def __str__(self):
        return f'Объект с параметрами ({self.a}, {self.b})'


z_1 = ComplexNumber(10, 20)
z_2 = ComplexNumber(30, 40)
print(z_1 + z_2)
print(z_1 * z_2)
