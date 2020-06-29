class AreaCalculatorMixin:
    def calculate(self):
        area = self.length * self.length
        print('area:', area)
        return area


class SquareMixin:
    def show(self):
        print('length:', self.length)


class Cube(AreaCalculatorMixin, SquareMixin):
    def __init__(self, length):
        self.length = length

    # def calculate(self):
    #     #volume = self.length * self.calculate()
    #     #volume = self.length * AreaCalculatorMixin.calculate(self)
    #     #volume = self.length * super().calculate()
    #     print('cube:', volume)
    #     return volume


cube = Cube(3)
cube.show()
cube.calculate()