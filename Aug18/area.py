class Circle():


    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


class Rectangle():


    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width


NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
