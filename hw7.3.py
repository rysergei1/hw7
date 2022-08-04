'''3. Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет),
type (тип), year (год). Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится
сообщение «Автомобиль заведен». Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
Пятый — присвоение автомобилю цвета.'''

class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def finish(self):
        print('Автомобиль заглушен')

    def change_year(self, new_year):
        self.year = new_year

    def change_type(self, new_type):
        self.type = new_type

    def change_color(self, new_color):
        self.color = new_color

    def __repr__(self):
        return f'Car: {self.color} {self.type} {self.year}'

if __name__ == '__main__':
    car = Car('Yellow', 'Hatchback', '2007')
    print(car)
    car.change_year('2020')
    car.change_type('Sedan')
    car.change_color('Red')
    car.start()
    car.finish()
    print(car)
