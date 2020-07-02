class VolumeCalculatorMixin:
    def calculate(self):
        volume = self.length ** 3
        print('volume:', volume)
        return volume

class Square:
    def show(self):
        print('length:', self.length)

class Cube(Square, VolumeCalculatorMixin):
    def __init__(self, length):
        self.length = length

    # def calculate(self):
    #     super().calculate()
    #     VolumeCalculatorMixin.calculate(self)


cube = Cube(3)
cube.show()
# Cube.show(cube)
cube.calculate()