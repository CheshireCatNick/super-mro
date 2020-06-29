class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def show(self):
        print(f'length: {self.length}, width: {self.width}')

    def calculate(self):
        print('area:', self.length * self.width)
    
        
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


square = Square(3)
square.show()
square.calculate()


