class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def display_func(self):
        return self.x, self.y, self.width, self.height


rect_1 = Rectangle(x=int(input('x= ')), y=int(input('y= ')), width=int(input('width= ')), height=int(input('height= ')))

print('Rectangle', rect_1.display_func())