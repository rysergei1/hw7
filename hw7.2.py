'''2. Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition — сложение,
multiplication — умножение, division — деление, subtraction — вычитание. При передаче в методы параметров a и b
с ними нужно производить соответствующие действия и печатать ответ.'''

class Math:

    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def addition(self, a, b):
        print(f'{a} + {b} = ', a + b)

    def multiplication(self, a, b):
        print(f'{a} * {b} = ', a * b)

    def division(self, a, b):
        print(f'{a} : {b} = ', round((a / b),2))

    def subtraction(self, a, b):
        print(f'{a} - {b} = ', a - b)

if __name__ == "__main__":
    c = Math()
    c.addition(4,3)
    c.multiplication(4, 3)
    c.division(4, 3)
    c.subtraction(4, 3)