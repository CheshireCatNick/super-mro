class A: 
    def hi(self):
        print('A')

class B:
    def hi(self):
        print('B')

class C:
    def hi(self):
        print('C')

class D(A, B):
    def hi(self):
        # directly using super() will fail since __class__ will be the original D in class namespace
        # https://docs.python.org/3/reference/datamodel.html#creating-the-class-object
        super(self.__class__, self).hi()


print(D.mro())
d = D()
d.hi()

D = type('D', (B, A), dict(D.__dict__))
print(D.mro())
d = D()
d.hi()

# no longer supported in python3
D.__bases__ = (C, B, A)
print(D.mro())
d = D()
d.hi()
