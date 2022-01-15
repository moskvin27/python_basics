# Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/час')

    def go(self):
        print(f'{self.name} в движении')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        if direction == 'right':
            print(f'{self.name} повернула направо')
        elif direction == 'left':
            print(f'{self.name} повернула налево')

class TownCar(Car):

    def capacity(self, passengers):
        self.passengers = passengers
        print(f'{self.passengers} пассажиров в {self.name}')

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')

class SportCar(Car):

    def nitro(self, boost):
        self.boost = boost
        print(f'Ускорение {self.boost} км/час')

class WorkCar(Car):

    def trailer(self):
        print(f'{self.name} имеет прицеп')

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')

class PoliceCar(Car):

    def robocop(self):
        self.is_police = True
        print(f'Орут сирены!')

car1 = TownCar(70, 'Black', 'Tram', False).go()
car2 = TownCar(70, 'Black', 'Tram', False).show_speed()
car3 = WorkCar(60, 'Green', 'Man', False).trailer()
car4 = SportCar(110, 'Red', 'Camaro', False).nitro(20)
car5 = PoliceCar(130, 'Blue', 'Ferrari', True).robocop()
