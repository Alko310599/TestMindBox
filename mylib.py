import math
from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def calculate_area(self):
        pass
    @staticmethod
    def choose_shape():
        print("Выберите тип фигуры:")
        print("1. Круг")
        print("2. Треугольник")
    
        choice = input("Введите номер выбранной фигуры: ")

        shape_dict = {
            '1': lambda: print(f"Площадь фигуры: ", Circle(float(input("Введите радиус круга: "))).calculate_area()),
            '2': lambda: print(f"Площадь фигуры: ", Triangle(
                float(input("Введите длину первой стороны треугольника: ")),
                float(input("Введите длину второй стороны треугольника: ")),
                float(input("Введите длину третьей стороны треугольника: "))
            ).calculate_area())
        }

        shape_function = shape_dict.get(choice)
        if shape_function:
            shape_function()
        else:
            raise ValueError("Некорректный выбор")
    
    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2
        
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Радиус должен быть неотрицательным числом")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("Длины сторон треугольника должны быть неотрицательными числами")
        if not self.is_triangle(side1, side2, side3):
            raise ValueError("Треугольник с такими сторонами не существует")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_triangle(self, side1, side2, side3):
        return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area
    
    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2

def calculate_area(shape):
    if not isinstance(shape, Shape):
        raise ValueError("Аргумент должен быть объектом класса Shape или его потомком")
    return shape.calculate_area()

if __name__ == "__main__":
    # Выбор фигуры
    Shape.choose_shape()
    # Пример использования
    """
    shapes = [Circle(5), Triangle(3, 4, 5)]
    for shape in shapes:
        print(f"Площадь фигуры: {calculate_area(shape)}")
    """

    