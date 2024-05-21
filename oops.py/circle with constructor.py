#[10,501,22,37,100,999,87,351]#

import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = []
        for radius in self.radius_list:
            area = math.pi * (radius ** 2)
            areas.append(area)
        return areas

    def calculate_circumference(self):
        circumferences = []
        for radius in self.radius_list:
            circumference = 2 * math.pi * radius
            circumferences.append(circumference)
        return circumferences


radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)
areas = circle.calculate_area()
circumferences = circle.calculate_circumference()

print("Areas:", areas)
print("Circumferences:", circumferences)