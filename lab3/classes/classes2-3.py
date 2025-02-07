class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Площадь фигуры по умолчанию:", 0)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        area_value = self.length ** 2
        print("Площадь квадрата:", area_value)


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        area_value = self.length * self.width
        print("Площадь прямоугольника:", area_value)



shape = Shape()
shape.area()  

square = Square(5)
square.area()  

rectangle = Rectangle(4, 6)
rectangle.area()  