class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = color
        self.filled = False
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        return  all(0 <= i <= 255 for i in (r, g, b))
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(i > 0 for i in sides)
    def get_sides(self):
        if self.sides_count == 12:
            return [self.__sides[0]] * self.sides_count
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
class Circle(Figure):
    sides_count = 1
    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__radius = radius
    def get_square(self):
        return 3.14 * self.__radius ** 2
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, side1, side2, side3):
        super().__init__(color, side1, side2, side3)
        self.__side1, self.__side2, self.__side3 = side1, side2, side3
    def get_square(self):
        half_perimeter = len(self) / 2
        return (half_perimeter * (half_perimeter - self.__side1) * (half_perimeter - self.__side2) * (half_perimeter - self.__side3))
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        super().__init__(color, side)
        self.__side = side
    def get_volume(self):
        return self.__side ** 3

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# # Проверка объёма (куба):
print(cube1.get_volume())


