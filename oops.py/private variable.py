class Circle:
    def __init__(self, radius):
        self.__pi = 3.141  # private member variable
        self.radius = radius

    def area(self):
        return self.__pi * (self.radius ** 2)

    def circumference(self):
        return 2 * self.__pi * self.radius


circle = Circle(10)
print("Area of the circle:", circle.area())
print("Circumference of the circle:", circle.circumference())