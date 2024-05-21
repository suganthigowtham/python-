#[10,501,22,37,100,999,87,351]#

class Shape:
    def __init__(self, *sides):
        self.sides = sides

    @classmethod
    def calculate_area(cls, *sides):
        if len(sides) != 2:
            raise ValueError("Area can only be calculated for shapes with two sides (e.g., rectangle).")
        return sides[0] * sides[1]

    @classmethod
    def calculate_perimeter(cls, *sides):
        return sum(sides)

# list:
sides_list = [10, 50, 22, 37, 100, 999, 87, 351]

rectangles = [(sides_list[i], sides_list[i+1]) for i in range(0, len(sides_list), 2)]

for rectangle in rectangles:
    area = Shape.calculate_area(*rectangle)
    perimeter = Shape.calculate_perimeter(*rectangle)
    print("Rectangle with sides", rectangle, "has area:", area, "and perimeter:", perimeter)