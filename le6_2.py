'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        self.weight = 25
        self.tickness = 5
        asphalt_mass = self._length * self._width * self.weight * self.tickness / 1000
        print(f'Need {asphalt_mass} ton for the building')

road_to_village = Road(20, 5000)
road_to_village.asphalt_mass()
